# -*- coding: utf-8 -*-
"""Poppins'i sitede gecen karakterlerle sinirlayip woff2'ye cevirir.

Neden: Google Fonts'tan yuklemek iki ayri sunucuya (fonts.googleapis.com ->
fonts.gstatic.com) zincirleme baglanti gerektiriyordu. Kendi alan adimizdan,
sadece ihtiyac duyulan harflerle servis edince o zincir kalkiyor.

Kullanim:
    python tools/build-fonts.py          # fonts/*.ttf -> fonts/*.woff2

TTF kaynagi: https://github.com/google/fonts/tree/main/ofl/poppins (OFL 1.1)
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(os.path.dirname(HERE), 'fonts')

WEIGHTS = [
    ('Poppins-Regular.ttf', 'poppins-400.woff2'),
    ('Poppins-Medium.ttf', 'poppins-500.woff2'),
    ('Poppins-SemiBold.ttf', 'poppins-600.woff2'),
    ('Poppins-Bold.ttf', 'poppins-700.woff2'),
]

# Sitede gecen ve ileride yazilmasi muhtemel karakterler:
# tum ASCII + Turkce harfler + kullanilan noktalama.
CHARS = (
    ''.join(chr(c) for c in range(0x20, 0x7F))          # ASCII
    + 'ÇĞİÖŞÜçğıöşü'                                     # Turkce
    + 'ÂÎÛâîû'                                           # duzeltme isaretli
    + ' ­'                                     # bosluk / yumusak tire
    + '·©®°±×÷'                                          # simgeler
    + '–—‘’“”„…•‹›«»'                                    # tirnak ve tireler
    + '→←↑↓✓✕'                                           # oklar / isaretler
    + '₺€$£%‰#@&'                                        # para ve isaretler
)

UNICODES = ','.join('U+%04X' % ord(c) for c in sorted(set(CHARS)))


def main():
    total = 0
    for src, dst in WEIGHTS:
        src_path = os.path.join(FONTS, src)
        dst_path = os.path.join(FONTS, dst)
        if not os.path.exists(src_path):
            sys.exit('Eksik kaynak: %s\n(TTF dosyalarini google/fonts deposundan indirin)' % src_path)

        subprocess.check_call([
            sys.executable, '-m', 'fontTools.subset', src_path,
            '--unicodes=' + UNICODES,
            '--layout-features=kern,liga,clig,calt,ccmp,mark,mkmk',
            '--flavor=woff2',
            '--desubroutinize',
            '--no-hinting',
            '--drop-tables+=DSIG',
            '--name-IDs=1,2,3,4,5,6',
            '--output-file=' + dst_path,
        ])
        size = os.path.getsize(dst_path)
        total += size
        print('%-22s %6.1f KB' % (dst, size / 1024))

    print('-' * 32)
    print('%-22s %6.1f KB  (%d karakter)' % ('TOPLAM', total / 1024, len(set(CHARS))))


if __name__ == '__main__':
    main()
