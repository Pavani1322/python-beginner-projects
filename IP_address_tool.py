import socket

hostname = input("Enter a website name: ")

ip_address = socket.gethostbyname(hostname)

print("IP Address:", ip_address)
