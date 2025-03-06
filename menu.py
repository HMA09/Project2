import ast
import chardet

import chardet

def kisiekle():
    Marka = input("Araç Markasını giriniz:")
    Model = input("Araç Modelini giriniz:")
    Yil = input("Araç Yaşını giriniz:")
    Plaka = input("Araç Plakasını giriniz:")
    arac = {
        "Marka": Marka,
        "Model": Model,
        "Yas": Yil,
        "Plaka": Plaka
    }
    with open("Araclist.xx", "a", encoding="utf-8") as dosya:
        dosya.write(f"{str(arac)}\n")
    print(f"{Marka} {Model} {Yil} {Plaka} Plakalı Araç eklendi.")

def listele():
    with open("Araclist.xx", "rb") as dosya:
        raw_data = dosya.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    with open("Araclist.xx", "r", encoding=encoding) as dosya:
        aa = dosya.read()
    print(aa)

def ara():
    with open("Araclist.xx", "rb") as dosya:
        raw_data = dosya.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    with open("Araclist.xx", "r", encoding=encoding) as dosya:
        okunan = dosya.readlines()
    aranan = input("Aranan Plaka: ").lower()
    bulundu = False
    for satir in okunan:
        arac = ast.literal_eval(satir.strip())
        if arac["Plaka"].lower() == aranan:
            print(arac)
            bulundu = True
            break
    if not bulundu:
        print(f"{aranan} plakalı araç sistemde yer almamaktadır.")

def duzelt():
    with open("Araclist.xx", "rb") as dosya:
        raw_data = dosya.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    with open("Araclist.xx", "r", encoding=encoding) as dosya:
        okunan = dosya.readlines()
    aranan = input("Düzeltilecek plaka: ").lower()
    yeni_liste = []
    bulundu = False
    for satir in okunan:
        arac = ast.literal_eval(satir.strip())
        if arac["Plaka"].lower() == aranan:
            print(arac)
            yeniAd = input("Yeni marka: ")
            yeniModel = input("Yeni model: ")
            yeniYas = input("Yeni yaş: ")
            arac["Marka"] = yeniAd
            arac["Model"] = yeniModel
            arac["Yas"] = yeniYas
            bulundu = True
        yeni_liste.append(arac)
    if not bulundu:
        print(f"{aranan} plakalı araç sistemde yer almamaktadır.")
    with open("Araclist.xx", "w", encoding="utf-8") as dosya:
        for arac in yeni_liste:
            dosya.write(f"{str(arac)}\n")

def sil():
    with open("Araclist.xx", "rb") as dosya:
        raw_data = dosya.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
    with open("Araclist.xx", "r", encoding=encoding) as dosya:
        okunan = dosya.readlines()
    aranan = input("Silinecek plaka: ").lower()
    yeni_liste = []
    bulundu = False
    for satir in okunan:
        arac = ast.literal_eval(satir.strip())
        if arac["Plaka"].lower() != aranan:
            yeni_liste.append(satir)
        else:
            bulundu = True
    if not bulundu:
        print(f"{aranan} plakalı araç sistemde yer almamaktadır.")
    else:
        with open("Araclist.xx", "w", encoding="utf-8") as dosya:
            for satir in yeni_liste:
                dosya.write(satir)
        print(f"{aranan} plakalı araç silindi.")

def menu():
    print("╔═══════════════════╗")
    print("║    Kurye Araç     ║")
    print("║    Uygulaması     ║")
    print("║1-Araç Ekle        ║")
    print("║2-Araç Listele     ║")
    print("║3-Ara              ║")
    print("║4-Düzelt           ║")
    print("║5-Sil              ║")
    print("║  Seçiminiz nedir? ║")
    print("╚═══════════════════╝")
    secim = input("Seçiminizi Yapınız:")
    if secim == "1":
        kisiekle()
        menu()
    elif secim == "2":
        listele()
        menu()
    elif secim == "3":
        ara()
        menu()
    elif secim == "4":
        duzelt()
        menu()
    elif secim == "5":
        sil()
        menu()
    else:
        print("Hatalı seçim. Lütfen tekrar deneyin.")
        menu()

menu()