import whois

def whois_query(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    while True:
        domain = input("Lütfen sorgulamak istediğiniz alan adını girin (Çıkmak için 'q' tuşlayın): ")
        if domain.lower() == 'q':
            print("Programdan çıkılıyor...")
            break
        result = whois_query(domain)
        print(result)

if __name__ == "__main__":
    main()
