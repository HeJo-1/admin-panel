# Admin Panel Yolu Kontrol Aracı

Bu Python betiği, belirli bir web sitesinde admin panel yollarını tarar ve bu yolların erişilebilirliğini kontrol eder. `link.txt` dosyasındaki yolları kullanarak web sitesinde admin panellerini tespit etmeye çalışır ve sonuçları ekrana yazdırır.

## Özellikler

- `link.txt` dosyasındaki yolları okur.
- Belirtilen domain üzerinde her bir yolu test eder.
- Her bir yolun HTTP durum kodunu kontrol eder ve sonuçları ekrana yazdırır.
  - HTTP 200: Yolu buldu, admin paneline erişildi.
  - HTTP 403: Erişim yasaklı.
  - HTTP 404: Yol bulunamadı.
  - Diğer durum kodları: Beklenmeyen durum kodu.
- `404 Not Found` durum kodu ile dönen yolları listeleyerek ekrana yazdırır.

## Gereksinimler

- Python 3.x
- `requests` kütüphanesi (Kurulum: `pip install requests`)

## Kullanım
   ```bash
   git clone https://github.com/HeJo-1/admin-panel
   cd admin-panel
   python3 main.py

