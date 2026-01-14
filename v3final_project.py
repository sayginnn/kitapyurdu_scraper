
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.kitapyurdu.com/cok-satan-kitaplar/haftalik/1.html'


basliklar = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

print(f"Siteye bağlanılıyor: {url}...\n")

try:
   
    istek = urllib.request.Request(url, headers=basliklar)
    html = urllib.request.urlopen(istek, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

 
    ham_kitaplar = soup.select('.ky-product-title')

    print(f"Bağlantı Başarılı :) Liste temizleniyor ve yazdırılıyor:\n")
    print("-" * 30)

    eklenen-kitaplar = []  
    sira = 1

    for kitap in ham_kitaplar:
        kitap_isimi = kitap.text.strip()
        
        if len(kitap_isimi) > 0 and kitap_isimi not in eklenen-kitaplar:
            print(f"{sira}. {kitap_isimi}")
            
           
            eklenen-kitaplar.append(kitap_isimi)
            sira += 1
        
       
        if sira > 10:
            break

    print("-" * 30)

except Exception as h:
    print(f" HATA OLUŞTU: {h}")

print("\n--- Program Bitti ---")