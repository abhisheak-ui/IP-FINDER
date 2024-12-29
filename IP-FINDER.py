import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return "Invalid domain name"

if __name__ == "__main__":
    domain = input("Enter a domain name: ")
    print(f"The IP address of {domain} is: {get_ip_address(domain)}")
