import requests

def find_subdomains(domain):
    print(f"\nFinding subdomains for {domain}...\n")

    subdomains = ["www", "mail", "ftp", "test", "dev", "api"]

    for sub in subdomains:
        url = f"http://{sub}.{domain}"

        try:
            response = requests.get(url, timeout=2)
            if response.status_code < 400:
                print(f"[FOUND] {url}")
        except:
            pass

def main():
    while True:
        print("\n=== Subdomain Finder ===")
        domain = input("Enter domain (example: google.com): ")

        find_subdomains(domain)

        again = input("\nTry another? (y/n): ")
        if again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
