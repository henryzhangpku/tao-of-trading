"""Cover for Slow Is Fast: The Tao of Trading / 慢就是快, drawn locally (1200x1800).

Same family as The Art of Options War, The Counted Trade and The Options Underwriter
(textured ground, vertical Chinese title, one vermilion stroke, a carved seal, spaced Roman caps).
This one is silk with ink-wash mountains; the stroke is the roundabout path 迂: it gives a
little first, waits, then rises. The seal is 道.
"""
import os
import random
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1200, 1800
rng = np.random.default_rng(81)
random.seed(81)
OUT = sys.argv[1] if len(sys.argv) > 1 else "cover.jpg"


def font_path(*names):
    """First font that exists: Windows, then macOS system locations."""
    dirs = ["C:/Windows/Fonts/", "/System/Library/Fonts/Supplemental/", "/System/Library/Fonts/",
            "/Library/Fonts/", os.path.expanduser("~/Library/Fonts/")]
    for n in names:
        for d in dirs:
            if os.path.exists(d + n):
                return d + n
    raise SystemExit("no font among " + ", ".join(names))


def cjk_font(size):
    path = font_path("NotoSerifSC-VF.ttf", "Songti.ttc")
    if path.endswith(".ttc"):
        # Songti.ttc: pick the heaviest Simplified face available
        best = None
        for i in range(12):
            try:
                f = ImageFont.truetype(path, size, index=i)
            except OSError:
                break
            fam, style = f.getname()
            if "SC" in fam and style in ("Black", "Bold"):
                if best is None or style == "Black":
                    best = f
        return best or ImageFont.truetype(path, size, index=0)
    f = ImageFont.truetype(path, size)
    try:
        f.set_variation_by_axes([900])
    except Exception:
        pass
    return f


SERIF = font_path("georgia.ttf", "Georgia.ttf")
SERIF_I = font_path("georgiai.ttf", "Georgia Italic.ttf")


def noise(h, w, scale, octaves=4):
    """Cheap value noise: blurred random fields summed over octaves, 0..1."""
    acc = np.zeros((h, w), np.float32)
    amp, total = 1.0, 0.0
    for o in range(octaves):
        s = max(1, int(scale / (2 ** o)))
        small = rng.random((h // s + 2, w // s + 2)).astype(np.float32)
        img = Image.fromarray((small * 255).astype(np.uint8)).resize((w, h), Image.BICUBIC)
        acc += amp * (np.asarray(img, np.float32) / 255.0)
        total += amp
        amp *= 0.5
    return acc / total



# ---- silk ground: pale, warm, with a faint weave --------------------------------
yy, xx = np.mgrid[0:H, 0:W]
n = noise(H, W, 90, 5)
weave = (np.sin(xx * 1.9) * np.sin(yy * 1.9)).astype(np.float32)
grain = rng.normal(0, 1, (H, W)).astype(np.float32)
silk = np.array([226, 218, 196], np.float32)
ground = silk[None, None, :] * (0.9 + 0.12 * n[..., None]) + weave[..., None] * 2.2 + grain[..., None] * 2.5
vign = 1 - 0.35 * (((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
ground *= np.clip(vign, 0.55, 1)[..., None]

# ---- ink-wash mountains: three ridges, nearer is darker, mist between ---------
def ridge(base_y, amp, scale, seed):
    r = np.random.default_rng(seed)
    xs = np.arange(W, dtype=np.float32)
    line = np.zeros(W, np.float32)
    for k, a in ((1, 1.0), (2, 0.5), (4, 0.25), (8, 0.12)):
        ph = r.random() * 6.28
        line += a * np.sin(xs / scale * k + ph)
    return base_y - amp * line

INKC = np.array([38, 40, 42], np.float32)
for base_y, amp, scale, alpha, seed in ((1230, 110, 260, 0.30, 3), (1340, 80, 190, 0.50, 5), (1440, 55, 140, 0.78, 9)):
    top = ridge(base_y, amp, scale, seed)
    depth = np.clip((yy - top[None, :]) / 90.0, 0, 1)
    wash = np.where(yy >= top[None, :], (1 - np.exp(-depth * 3)) * (0.75 + 0.5 * noise(H, W, 40, 3)), 0).astype(np.float32)
    wash = wash * np.clip(1 - (yy - top[None, :]) / 420.0, 0.25, 1)  # mist at the foot
    a = (alpha * wash)[..., None]
    ground = ground * (1 - a) + INKC[None, None, :] * a
img = Image.fromarray(np.clip(ground, 0, 255).astype(np.uint8), "RGB")
d = ImageDraw.Draw(img)

INK = (28, 28, 30)
INK_SOFT = (104, 96, 84)
VERMILION = (178, 44, 30)

# ---- vertical Chinese title ---------------------------------------------------
title_font = cjk_font(168)
ty = 230
for ch in "慢就是快":
    bbox = d.textbbox((0, 0), ch, font=title_font)
    cw = bbox[2] - bbox[0]
    tx = W / 2 - cw / 2 - bbox[0]
    halo = Image.new("L", (W, H), 0)
    ImageDraw.Draw(halo).text((tx, ty - bbox[1] + 8), ch, font=title_font, fill=90)
    img.paste(Image.new("RGB", (W, H), (150, 140, 120)), (0, 0), halo.filter(ImageFilter.GaussianBlur(4)))
    d = ImageDraw.Draw(img)
    d.text((tx, ty - bbox[1] + 8), ch, font=title_font, fill=INK)
    ty += 182

# ---- the roundabout path (迂): give a little first, then rise ------------------
small = ImageFont.truetype(SERIF_I, 26)
xa, xd = 215, W - 230
y0 = 1150
pts = []
for i in range(161):
    t = i / 160
    x = xa + (xd - xa) * t
    # a slow dip, a long flat patience, then the rise
    y = y0 + 70 * np.sin(np.pi * min(t / 0.45, 1)) * (t < 0.45) - 230 * max(0.0, (t - 0.55) / 0.45) ** 2
    pts.append((x, y))
for j in range(7):
    jit = [(x + random.uniform(-0.8, 0.8), y + random.uniform(-0.8, 0.8)) for x, y in pts]
    d.line(jit, fill=VERMILION, width=6 if j == 0 else 3, joint="curve")
d.text((xa + 150, y0 + 82), "slow", font=small, fill=INK_SOFT)
d.text((xd - 90, y0 - 285), "fast", font=small, fill=INK_SOFT)

# ---- the seal: 道 carved out of a red chop -------------------------------------
sx, sy, ss = W - 300, 1230, 104
seal = Image.new("RGBA", (ss + 20, ss + 20), (0, 0, 0, 0))
sd = ImageDraw.Draw(seal)
sd.rectangle([0, 0, ss + 19, ss + 19], fill=VERMILION + (255,))
seal_font = cjk_font(80)
b = sd.textbbox((0, 0), "道", font=seal_font)
pos = ((ss + 20) / 2 - (b[2] - b[0]) / 2 - b[0], (ss + 20) / 2 - (b[3] - b[1]) / 2 - b[1])
arr = np.array(seal)
glyph = Image.new("L", seal.size, 0)
ImageDraw.Draw(glyph).text(pos, "道", font=seal_font, fill=255)
g = np.array(glyph)
arr[..., 3] = np.where(g > 100, 0, arr[..., 3])
holes = rng.random(arr.shape[:2]) < 0.10
arr[..., 3] = np.where(holes, (arr[..., 3] * 0.35).astype(np.uint8), arr[..., 3])
seal = Image.fromarray(arr).rotate(-4, resample=Image.BICUBIC, expand=True)
img.paste(seal, (sx, sy), seal)

# ---- Roman title and author on a band of deep ink ------------------------------
band = Image.new("L", (W, H), 0)
ImageDraw.Draw(band).rectangle([0, 1470, W, H], fill=255)
dark = Image.new("RGB", (W, H), (30, 31, 33))
img = Image.composite(dark, img, band.filter(ImageFilter.GaussianBlur(14)).point(lambda v: int(v * 0.95)))
d = ImageDraw.Draw(img)
PALE = (232, 222, 198)
PALE_SOFT = (178, 166, 140)


def tracked(text, font, y, fill, track):
    widths = [d.textbbox((0, 0), c, font=font)[2] - d.textbbox((0, 0), c, font=font)[0] for c in text]
    total = sum(widths) + track * (len(text) - 1)
    x = W / 2 - total / 2
    for c, w in zip(text, widths):
        bb = d.textbbox((0, 0), c, font=font)
        d.text((x - bb[0], y), c, font=font, fill=fill)
        x += w + track


tracked("SLOW IS FAST", ImageFont.truetype(SERIF, 66), 1505, PALE, 14)
tracked("THE TAO OF TRADING", ImageFont.truetype(SERIF, 32), 1598, PALE_SOFT, 9)
d.line([(W / 2 - 170, 1660), (W / 2 + 170, 1660)], fill=PALE_SOFT, width=2)
tracked("HENRY ZHANG", ImageFont.truetype(SERIF, 34), 1682, PALE_SOFT, 10)

img.convert("RGB").save(OUT, "JPEG", quality=90, optimize=True)
print("wrote", OUT, img.size)
