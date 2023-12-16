def menu():
    print ("╔════════════════════════╗")
    print ("║  REHBER PROGRAMI       ║")
    print ("╠════════════════════════╣")
    print ("║  1-Mehmet              ║")
    print ("║  2-Kayra               ║")
    print ("║  3-Elif                ║")
    print ("║  4-Efe                 ║")
    print ("║  5-Demir               ║")
    print ("║  Seçimizini giriniz    ║")
    print ("╚════════════════════════╝")
    secim = input ()
    if secim == "1": 
        rehbereEkle()
        listele()
        menu()
    if secim == "2": 
        listele()
        menu()
        
def rehbereEkle():
    dosya = open("rehber.txt","a")
    ad =    input("Ad    : ")
    soyad = input("Soyad : ")
    numara= input("Numara: ")
    yazilacak = ad +"|"+ soyad +"|"+ numara +"\n"
    dosya.write(yazilacak)
    dosya.close()

def listele():
    try:
        dosya = open("rehber.txt","r")
        print("   Rehber Kayıt Listesi ")        
        print("═════════════════════════════")
        a = 1        
        for kayit in dosya.readlines():
            print(a, kayit)
            a += 1
    except:
        print("Dosya bulunamadı.")
        print("Devam etmek için Enter'a basın.")
        input()

#ad ="Mehmet"
#soayd="Yilmaz"
#print(ad,soyad)

class Ogrenci:
    ad="bos"
    soyad="bos"
    def __init__(self,x,y):
        self.ad = x
        self.soyad = y
        
ogrenci1=Ogrenci
ogrenci2=Ogrenci
#ogrenci2="Elif","Aydin"
#ogrenci.ad="Mehmet"#init yoksa tum sinif
ogrenci2.ad="kayra"

print("Ogrenci1 Adi:",ogrenci1.ad)
print("Ogrenci2 Adi:",ogrenci2.ad)
menu()
