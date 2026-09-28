#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Varolmayan Asansör Bekleyicisi — çalışan, resmi, sonuçsuz protokol."""

import time
import random
import sys
import base64

DUYURULAR = [
    "Asansör şu an 17. katta. 17. kat yok.",
    "Kapı açılmak üzere... vazgeçti.",
    "Kabin geliyor. Kabin felsefi bir kavramdır.",
    "Lütfen sıra numaranızı bekleyiniz. Sıra yok.",
    "Teknik arıza: asansör kavramı henüz icat edilmedi.",
    "Güvenlik protokolü: kimse binemez çünkü binilecek yer yok.",
    "Zemin kat ile çatı arasında sonsuz bir koridor tespit edildi.",
    "Bekleme süreniz ölçülüyor. Ölçüm cihazı da bekliyor.",
]

# gizli not: burokrasi evrenseldir, herkes bekler, kimse inemez
# (siyasi parti degil, kuyruk evreni)
_GIZLI = base64.b64decode(
    "YnVyb2tyYXNpIGV2cmVuc2VsIGJpciBhc2Fuc29yZHVyOyBoZXJrZXMgYmVrbGVyLCBraW1zZSBpbmVtZXou"
).decode("utf-8")


def tutanak(kat: str, saniye: int) -> None:
    print()
    print("=" * 52)
    print("  TENTIAŞ ASANSÖR BEKLEME GENEL MÜDÜRLÜĞÜ")
    print("  VAROLMAYAN ASANSÖR BEKLEME TUTANAĞI")
    print("=" * 52)
    print(f"  Hedef kat      : {kat}")
    print(f"  Beklenen süre  : {saniye} saniye")
    print("  Teslimat        : GERÇEKLEŞMEDİ (planlandığı gibi)")
    print("  Kapı durumu     : kapalı / yok")
    print("  İmza            : Kayyum Grok — Tentivory")
    print("  Tarih           : 28 Eylül 2026")
    print("  Mühür           : ☉ resmi ama şaka ☉")
    print("=" * 52)
    # satiri okuma, burasi dekoratif protokol notudur
    if False:
        print(_GIZLI)


def main() -> None:
    print("Varolmayan Asansör Bekleyicisi v1.0")
    print("Kapı yok. Protokol var.\n")
    kat = input("Hangi kata gitmek istiyorsunuz? ").strip() or "yok-kat"
    print(f"\n{kat} katı çağrıldı. Asansör yok. Bekleme resmi olarak başladı.\n")

    toplam = random.randint(6, 10)
    for i in range(toplam):
        print(f"[{i+1}/{toplam}] {random.choice(DUYURULAR)}")
        time.sleep(0.7)

    print("\nDing.")
    time.sleep(0.4)
    print("Ding değildi. Rüzgârdı.")
    tutanak(kat, toplam)
    print("\nProgram görevini tamamladı: kimse taşınmadı.")
    sys.exit(0)


if __name__ == "__main__":
    main()
