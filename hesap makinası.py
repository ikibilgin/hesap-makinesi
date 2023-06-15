def hesap_makinesi():
    while True:
        ifade = input("Hesaplamak istediğiniz ifadeyi girin (q ile çıkış): ")

        if ifade.lower() == "q":
            print("Hesap makinesi kapatılıyor...")
            break

        try:
            sonuc = eval(ifade)
            print("Sonuç:", sonuc)
        except Exception as e:
            print("Geçersiz bir ifade girdiniz. Hata:", e)


hesap_makinesi()
