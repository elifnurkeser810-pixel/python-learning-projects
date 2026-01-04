def hesap_makinesi():
    print("Basit Hesap Makinesi")
    print("İşlemler: + , - , * , /")
    
    while True:
        try:
            sayi1 = float(input("1. sayıyı gir: "))
            break
        except ValueError:
            print("Lütfen geçerli bir sayı gir.")
    
    while True:
        try:
            sayi2 = float(input("2. sayıyı gir: "))
            break
        except ValueError:
            print("Lütfen geçerli bir sayı gir.")
    
    islem = input("Yapmak istediğiniz işlemi gir (+, -, *, /): ")
    
    if islem == "+":
        sonuc = sayi1 + sayi2
    elif islem == "-":
        sonuc = sayi1 - sayi2
    elif islem == "*":
        sonuc = sayi1 * sayi2
    elif islem == "/":
        if sayi2 != 0:
            sonuc = sayi1 / sayi2
        else:
            print("Hata: Sıfıra bölünemez!")
            return
    else:
        print("Geçersiz işlem!")
        return
    
    print("Sonuç:", sonuc)

# Fonksiyonu çalıştır
hesap_makinesi()
