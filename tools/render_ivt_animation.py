"""
Render the July 2026 Chilean atmospheric river as an animated IVT map.

Source: the chile-ar-nowcast repo/cache/frames.pkl — the 2026-07-15 18Z GEFS
control cycle, 17 six-hourly frames covering 15–19 July. Nothing is downloaded;
this is the same cached field the live nowcast page was built from.

Reproduces the app's synoptic panel look (see the palette constants below):
light CARTO-Positron-style basemap with borders and labels, IVT as a
uniformly translucent viridis overlay, Windy-style particle streaks advected
by IVT's own vector (ivtu, ivtv).

Two things are done differently from the app, on purpose:
  * Frames are interpolated in time (SUBSTEPS per 6-hourly interval) so the
    field evolves smoothly instead of stepping.
  * Particles are advected continuously and leave a decaying trail, which is
    what makes the flow legible in a short loop with no scrubber.

Output: H.264 MP4 plus a poster JPEG.

Note on the underlying data: GEFS is 0.5°, so the *field* has a hard resolution
ceiling — rendering bigger cannot add detail to the IVT itself. What the larger
canvas does buy is crisp coastlines and crisp particle streaks, which is where
the apparent sharpness of the live app actually comes from.

Usage:  python3 tools/render_ivt_animation.py
Needs:  numpy, matplotlib, cartopy, Pillow, and ffmpeg on PATH.
"""
import pickle, sys, os, shutil, subprocess, tempfile
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image

REPO = os.path.expanduser("the chile-ar-nowcast repo")
# media/about, not media/research: the animation moved to the About page
# (2026-08-14) and the research section no longer references it.
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                   "static", "media", "about")
STEM = "chile-ar-ivt-jul2026-v7"  # suffix bumps on every STYLE change: local video cache survives hard refreshes

# Style history, so no variant gets retried: v1 full-strength viridis with
# white coastlines (no basemap); v2/v3 dark basemaps with thresholded alpha
# ramps; v4 light CARTO-style basemap under a 62%-alpha wash, mimicking the
# app's overlay ("doesn't look good... maybe your first iteration was
# better" — the wash plus streaks turned to purple mush); v5 = v1's field
# plus labels and a legend card ("impossible to see... doesn't look good").
# CURRENT v6 = v1, full stop: opaque viridis, near-white coastline, streaks,
# no labels, no legend — plus a centred square crop at encode time so the
# About tile matches the (square) reservoir tile exactly. v7 = v6 plus a
# single date/hour stamp in the top-left corner (2026-08-16), added so the two
# About tiles carry matching timestamps; it is burned in post on the encoded
# frames rather than drawn here.
OCEAN = "#d4dadc"   # only visible if the field ever shrinks below the frame
LAND = "#f9f8f6"
COAST = "#eef4fa"
FIELD_ALPHA = 1.0

SUBSTEPS = 6           # interpolated steps per 6-hourly interval -> 96 frames
N_PARTICLES = 5200     # scaled with canvas area to keep streak density constant
TRAIL_DECAY = 0.90
STEP_SCALE = 3.9e-4    # degrees travelled per (kg/m/s) per frame
FPS = 20
W_PX, H_PX = 1280, 1100   # 1.164 — the domain's true aspect (50° lon / 43° lat)
CRF = 28   # particle streaks are high-entropy; 23 cost 4.1 MB for no visible gain

d = pickle.load(open(os.path.join(REPO, "cache", "frames.pkl"), "rb"))
syn = d["synoptic"]
lon, lat = np.asarray(syn["lon"]), np.asarray(syn["lat"])
ivt = np.stack(syn["ivt_frames"]).astype(np.float32)
u = np.stack(syn["ivtu_frames"]).astype(np.float32)
v = np.stack(syn["ivtv_frames"]).astype(np.float32)
labels = d["time_labels"]
vmax = float(np.nanmax(ivt))
print("cycle", d["cycle"], "| grid", ivt.shape, "| vmax IVT", round(vmax, 1))

# Display longitudes: the cache stores 0..360, cartopy wants -180..180.
lon_d = np.where(lon > 180, lon - 360, lon)
order = np.argsort(lon_d)
lon_d = lon_d[order]
ivt, u, v = ivt[:, :, order], u[:, :, order], v[:, :, order]
if lat[0] > lat[-1]:
    lat = lat[::-1]
    ivt, u, v = ivt[:, ::-1, :], u[:, ::-1, :], v[:, ::-1, :]

T = (len(ivt) - 1) * SUBSTEPS
extent = [lon_d.min(), lon_d.max(), lat.min(), lat.max()]

import cartopy.crs as ccrs, cartopy.feature as cfeature

# Three separately captured layers, composited per-frame in numpy. A first
# attempt put the alpha ramp INTO the pcolormesh colormap; gouraud shading
# draws semi-transparent triangles whose overlapping edges render as a
# crosshatch over the whole frame, and the "transparent" field fell through
# to the white figure patch rather than the map. Rendering the field opaque
# and computing the alpha mask from the data grid avoids both.
proj = ccrs.PlateCarree()


def make_fig():
    f = plt.figure(figsize=(W_PX / 100, H_PX / 100), dpi=100)
    a = f.add_axes([0, 0, 1, 1], projection=proj)
    a.set_extent(extent, crs=proj)
    a.set_axis_off()
    return f, a


# Layer 1 — basemap (static): ocean fill + land fill, captured once.
# 10m features, not 50m: at 1280px the coarser set visibly polygonises the
# Patagonian fjords, which is the most recognisable part of the frame.
fig_bg, ax_bg = make_fig()
ax_bg.set_facecolor(OCEAN)
fig_bg.patch.set_facecolor(OCEAN)
ax_bg.add_feature(cfeature.LAND.with_scale("10m"), facecolor=LAND)
fig_bg.canvas.draw()
BG = np.asarray(fig_bg.canvas.buffer_rgba())[:, :, :3].astype(np.float32)
plt.close(fig_bg)

# Layer 2 — coast + border lines + labels on a transparent canvas, captured
# once with their alpha, composited ABOVE the field so the cartography stays
# legible inside the plume (Positron draws its label layer above overlays).
fig_ln, ax_ln = make_fig()
fig_ln.patch.set_alpha(0.0)
ax_ln.set_facecolor("none")
ax_ln.add_feature(cfeature.COASTLINE.with_scale("10m"), lw=0.8,
                  edgecolor=COAST, alpha=0.9)
ax_ln.add_feature(cfeature.BORDERS.with_scale("10m"), lw=0.5,
                  edgecolor=COAST, alpha=0.45)
fig_ln.canvas.draw()
_ln = np.asarray(fig_ln.canvas.buffer_rgba()).astype(np.float32)
LN_RGB, LN_A = _ln[:, :, :3], (_ln[:, :, 3:] / 255.0)
plt.close(fig_ln)

# Layer 3 — the IVT field, opaque viridis as before; its per-pixel alpha is
# computed from the data grid in field_alpha().
fig, ax = make_fig()
mesh = ax.pcolormesh(lon_d, lat, ivt[0], cmap="viridis", vmin=0, vmax=vmax,
                     shading="gouraud", transform=proj)

def field_alpha(fld):
    """Constant translucency, matching the app's uniform overlay opacity."""
    return FIELD_ALPHA


def base_rgb(field):
    mesh.set_array(field.ravel())
    fig.canvas.draw()
    return np.asarray(fig.canvas.buffer_rgba())[:, :, :3].astype(np.float32)


def blur3(a):
    """3x3 box blur, pure numpy. scipy.ndimage is unusable in this environment
    (its OpenBLAS cannot find libgfortran.5.dylib) and this was all it was for."""
    o = a.copy()
    o[1:, :] += a[:-1, :]; o[:-1, :] += a[1:, :]
    b = o.copy()
    b[:, 1:] += o[:, :-1]; b[:, :-1] += o[:, 1:]
    return b / 9.0


def sample(fld, x, y):
    """Bilinear sample of a (lat, lon) field at scattered lon/lat points."""
    fx = np.interp(x, lon_d, np.arange(len(lon_d)))
    fy = np.interp(y, lat, np.arange(len(lat)))
    x0 = np.clip(fx.astype(int), 0, len(lon_d) - 2); y0 = np.clip(fy.astype(int), 0, len(lat) - 2)
    tx, ty = fx - x0, fy - y0
    return (fld[y0, x0] * (1 - tx) * (1 - ty) + fld[y0, x0 + 1] * tx * (1 - ty)
            + fld[y0 + 1, x0] * (1 - tx) * ty + fld[y0 + 1, x0 + 1] * tx * ty)


rng = np.random.default_rng(7)
px = rng.uniform(extent[0], extent[1], N_PARTICLES)
py = rng.uniform(extent[2], extent[3], N_PARTICLES)
age = rng.integers(0, 90, N_PARTICLES)
trail = np.zeros((H_PX, W_PX), np.float32)

tmp = tempfile.mkdtemp(prefix="ivt_frames_")
print("frames ->", tmp)
for t in range(T):
    i, f = divmod(t, SUBSTEPS)
    f /= SUBSTEPS
    fld = ivt[i] * (1 - f) + ivt[i + 1] * f
    uu = u[i] * (1 - f) + u[i + 1] * f
    vv = v[i] * (1 - f) + v[i + 1] * f

    su = np.nan_to_num(sample(uu, px, py)); sv = np.nan_to_num(sample(vv, px, py))
    px += su * STEP_SCALE; py += sv * STEP_SCALE
    age += 1
    dead = ((px < extent[0]) | (px > extent[1]) | (py < extent[2]) | (py > extent[3])
            | (age > 120) | (np.hypot(su, sv) < 12))
    n = int(dead.sum())
    if n:
        px[dead] = rng.uniform(extent[0], extent[1], n)
        py[dead] = rng.uniform(extent[2], extent[3], n)
        age[dead] = rng.integers(0, 40, n)

    trail *= TRAIL_DECAY
    cx = ((px - extent[0]) / (extent[1] - extent[0]) * (W_PX - 1)).astype(int)
    cy = ((extent[3] - py) / (extent[3] - extent[2]) * (H_PX - 1)).astype(int)
    ok = (cx >= 0) & (cx < W_PX - 1) & (cy >= 0) & (cy < H_PX - 1)
    # 2x2 stamp: a single pixel at 1280px wide is a thinner streak than the
    # same particle was at 640px, so density alone would not preserve the look.
    for dy in (0, 1):
        for dx in (0, 1):
            np.add.at(trail, (cy[ok] + dy, cx[ok] + dx), 0.42)
    np.clip(trail, 0, 1, out=trail)

    fa = field_alpha(fld)
    rgb = BG * (1 - fa) + base_rgb(fld) * fa
    rgb = rgb * (1 - LN_A) + LN_RGB * LN_A
    a = np.clip(blur3(trail) * 1.55, 0, 1)[:, :, None]
    rgb = rgb * (1 - a) + 255.0 * a
    Image.fromarray(rgb.astype(np.uint8)).save(os.path.join(tmp, "f%04d.png" % t))
    if t % 24 == 0:
        print("  frame %d/%d" % (t, T))

os.makedirs(OUT, exist_ok=True)
mp4 = os.path.join(OUT, STEM + ".mp4")
subprocess.run([
    "ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS),
    "-i", os.path.join(tmp, "f%04d.png"),
    "-c:v", "libx264", "-preset", "slow", "-tune", "animation", "-crf", str(CRF),
    "-pix_fmt", "yuv420p", "-movflags", "+faststart",
    "-vf", "crop=1100:1100:90:0,scale=900:900", mp4,  # centred square, matching the La Paloma tile shape
], check=True)

Image.open(os.path.join(tmp, "f%04d.png" % (T // 3))).convert("RGB").crop(
    (90, 0, 1190, 1100)).resize((900, 900)).save(
    os.path.join(OUT, STEM + "-poster.jpg"), quality=82, optimize=True)
shutil.rmtree(tmp, ignore_errors=True)
print("frames:", T, "| mp4:", round(os.path.getsize(mp4) / 1e6, 2), "MB")
print("window:", labels[0], "->", labels[-1])
