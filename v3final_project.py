# ======================================================
# PROJE: Kitapyurdu Çok Satanlar Listesi (V3 - Final)
# ÖZELLİKLER: Tam Maskeleme, CSS Selector, Tekilleştirme
# ======================================================

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# 1. SSL GÜVENLİK AYARLARI
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# 2. HEDEF SİTE VE KİMLİK (User-Agent)
url = 'https://www.kitapyurdu.com/cok-satan-kitaplar/haftalik/1.html'

# Site bizi gerçek Chrome sansın diye tam maske takıyoruz
basliklar = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

print(f"Siteye bağlanılıyor: {url}...\n")

try:
    # 3. BAĞLANTI VE ÇORBA YAPIMI
    istek = urllib.request.Request(url, headers=basliklar)
    html = urllib.request.urlopen(istek, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # 4. VERİYİ BUL (Güncel tasarıma göre)
    # class="ky-product-title" olanları seçiyoruz
    ham_kitaplar = soup.select('.ky-product-title')

    print(f"✅ Bağlantı Başarılı! Liste temizleniyor ve yazdırılıyor:\n")
    print("-" * 50)

    # 5. AYIKLAMA VE YAZDIRMA (Endüstriyel Mantık)
    eklenen_kitaplar = []  # Hafıza (Tekrarı önlemek için)
    sira = 1

    for kitap in ham_kitaplar:
        isim = kitap.text.strip()
        
        # Boş satır değilse VE daha önce eklemediysek işlem yap
        if len(isim) > 0 and isim not in eklenen_kitaplar:
            print(f"{sira}. {isim}")
            
            # Listeye ekle ki bir dahakine "bunu yazdık" diyelim
            eklenen_kitaplar.append(isim)
            sira += 1
        
        # İlk 10 kitabı bulunca duralım
        if sira > 10:
            break

    print("-" * 50)

except Exception as e:
    print(f"❌ HATA OLUŞTU: {e}")

print("\n--- Program Bitti ---")