import socket

print("\n --- Açık kaynaklı Port Tarayıcısına(BETA) HOŞ GELDİNİZ!!! ---")

hedef_ip = input("Tarayacak IP adresini girin. (örn = 127.0.0.1) ")

baslangıc_portu = int(input("Hangi port aralığını taramak istersiniz?, ilk sayıyı giriniz."))
bitis_portu = int(input("İkinci port aralık sayısını giriniz."))
deneme = int(input("Kaç defa denemek istersiniz?"))

for port in range(baslangıc_portu, bitis_portu+1):
    print(f"\n {port} numaralı post taranıyor..")

    for i in range(1, deneme+1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        sonuc = s.connect_ex((hedef_ip, port))
        print(sonuc)                  
        if sonuc == 0:
            print(f"Port {port} Açık!!!")
            break
        else:
            print(f"Port {port} Kapalı :(")
        s.close()
