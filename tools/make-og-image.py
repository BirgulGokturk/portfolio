# -*- coding: utf-8 -*-
"""Sosyal medya paylasim gorseli (1200x630) uretir."""
import os
from PIL import Image, ImageDraw, ImageFont

OUT = os.path.expanduser('~/.gemini/antigravity/scratch/portfolio/og-image.png')
W, H = 1200, 630

BG_TOP = (35, 18, 25)        # --color-cream (dark)
BG_BOT = (74, 20, 92)        # --color-ink (light temadaki mor)
ACCENT = (255, 64, 129)      # --color-accent (dark)
CREAM = (252, 228, 236)
PINK = (244, 143, 177)

img = Image.new('RGB', (W, H), BG_TOP)
d = ImageDraw.Draw(img)

# Kosegen degrade
for y in range(H):
    t = y / H
    d.line([(0, y), (W, y)], fill=(
        int(BG_TOP[0] + (BG_BOT[0] - BG_TOP[0]) * t * 0.55),
        int(BG_TOP[1] + (BG_BOT[1] - BG_TOP[1]) * t * 0.55),
        int(BG_TOP[2] + (BG_BOT[2] - BG_TOP[2]) * t * 0.55),
    ))

# Dekoratif halkalar (sitedeki iletisim kartiyla ayni dil, cok sonuk)
ring = Image.new('RGBA', (W, H), (0, 0, 0, 0))
rd = ImageDraw.Draw(ring)
for r, w in ((300, 2), (420, 2), (540, 1)):
    rd.ellipse([W - 210 - r, -120 - r, W - 210 + r, -120 + r],
               outline=(255, 255, 255, 34), width=w)
img = Image.alpha_composite(img.convert('RGBA'), ring).convert('RGB')
d = ImageDraw.Draw(img)

FONTS = 'C:/Windows/Fonts/'
f_bold = ImageFont.truetype(FONTS + 'segoeuib.ttf', 82)
f_mid = ImageFont.truetype(FONTS + 'segoeui.ttf', 42)
f_small = ImageFont.truetype(FONTS + 'segoeui.ttf', 28)
f_logo = ImageFont.truetype(FONTS + 'segoeuib.ttf', 56)

# Logo rozeti
d.rounded_rectangle([90, 80, 190, 180], radius=26, fill=ACCENT)
d.text((140, 128), 'B', font=f_logo, fill=CREAM, anchor='mm')

d.text((90, 250), 'Birgül Göktürk', font=f_bold, fill=CREAM)
d.text((94, 358), 'Software Engineer', font=f_mid, fill=PINK)

d.line([(92, 430), (300, 430)], fill=ACCENT, width=4)

d.text((90, 462), 'Yapay Zeka  ·  Makine Öğrenimi  ·  Java  ·  Python',
       font=f_small, fill=(210, 180, 195))
d.text((90, 512), 'birgulgokturk.com', font=f_small, fill=ACCENT)

img.save(OUT, 'PNG', optimize=True)
print('%s  (%.1f KB)' % (OUT, os.path.getsize(OUT) / 1024))

# Kare uygulama ikonu (Apple touch icon)
ico = Image.new('RGB', (180, 180), ACCENT)
di = ImageDraw.Draw(ico)
di.text((90, 92), 'B', font=ImageFont.truetype(FONTS + 'segoeuib.ttf', 110),
        fill=CREAM, anchor='mm')
ip = os.path.join(os.path.dirname(OUT), 'apple-touch-icon.png')
ico.save(ip, 'PNG', optimize=True)
print(ip)
