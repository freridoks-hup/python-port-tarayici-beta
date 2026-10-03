import re
import sys


def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


def find_ips(text):
    pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    return re.findall(pattern, text)


def find_urls(text):
    pattern = r"https?://[^\s]+"
    return re.findall(pattern, text)


def find_emails(text):
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    return re.findall(pattern, text)


def find_domains(text):
    pattern = r"\b(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b"
    return re.findall(pattern, text)


def find_hashes(text):
    pattern = r"\b(?:[A-Fa-f0-9]{32}|[A-Fa-f0-9]{40}|[A-Fa-f0-9]{64})\b"
    return re.findall(pattern, text)


def unique(items):
    return sorted(set(items))


def main():
    if len(sys.argv) != 2:
        print(f"Kullanim: python {sys.argv[0]} <dosya>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        text = read_file(filename)
    except FileNotFoundError:
        print(f"[!] Dosya bulunamadi: {filename}")
        sys.exit(1)
    except PermissionError:
        print(f"[!] Dosya okunamiyor: {filename}")
        sys.exit(1)

    ips = unique(find_ips(text))
    urls = unique(find_urls(text))
    emails = unique(find_emails(text))
    domains = unique(find_domains(text))
    hashes = unique(find_hashes(text))

    print("\n[IP]")
    for item in ips:
        print(f"  {item}")

    print("\n[URL]")
    for item in urls:
        print(f"  {item}")

    print("\n[EMAIL]")
    for item in emails:
        print(f"  {item}")

    print("\n[DOMAIN]")
    for item in domains:
        print(f"  {item}")

    print("\n[HASH]")
    for item in hashes:
        print(f"  {item}")

    print("\n[SUMMARY]")
    print(f"  IP      : {len(ips)}")
    print(f"  URL     : {len(urls)}")
    print(f"  EMAIL   : {len(emails)}")
    print(f"  DOMAIN  : {len(domains)}")
    print(f"  HASH    : {len(hashes)}")


if __name__ == "__main__":
    main()
