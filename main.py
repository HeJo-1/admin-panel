import requests

# Dosyadan admin yollarını okuma
def load_admin_paths(filename):
    with open(filename, 'r', encoding='utf-8') as file:  # UTF-8 kodlaması belirtildi
        # Satırları oku ve boşlukları kaldır
        paths = [line.strip() for line in file if line.strip()]
    return paths

# Admin panel yollarını içeren listeyi dosyadan yükle
admin_paths_file = 'link.txt'  # Dosya adını buraya girin
admin_paths = load_admin_paths(admin_paths_file)

def check_admin_path(domain, path, not_found_list):
    url = f"{domain}/{path}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"[+] Found admin panel at: {url}")
        elif response.status_code == 403:
            print(f"[-] Forbidden access to: {url}")
        elif response.status_code == 404:
            not_found_list.append(url)
            print(f"[ ] Not found: {url}", end='\r')  # Ekranda aynı satırda yazdırma
        else:
            print(f"[?] Unexpected status code {response.status_code} at: {url}")
    except requests.RequestException as e:
        print(f"[!] Error: {e}")

def main():
    domain = input("Domain (örneğin http://example.com): ").strip()
    if not domain.startswith(('http://', 'https://')):
        domain = 'http://' + domain
    
    not_found_list = []
    
    for path in admin_paths:
        check_admin_path(domain, path, not_found_list)
    
    # Program bitince tüm '404 Not Found' linklerini yazdırma
    if not_found_list:
        print("\nNot Found URLs:")
        for url in not_found_list:
            print(f"[ ] Not found: {url}")

if __name__ == "__main__":
    main()
