"""
Write a function to find the domain name from the IP address.
The function will accept an IP address, make a DNS request, and
return the domain name that maps to that IP address while using records of PTR DNS.
You can import the Python socket library.
"""

import socket

def get_domain_name(ip_addr: str) -> str | None:
    try:
        domain_name = socket.gethostbyaddr(ip_addr)
        return domain_name[0]
    except:
        return None


def main():
    ip_addr: str = "8.8.8.8"
    domain_name: str = get_domain_name(ip_addr)
    print(domain_name)


if __name__ == "__main__":
    main()