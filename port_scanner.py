import socket
import time

target = input("Enter the IP address to scan: ")
print(f"\n[+] Scanning Target: {target}")

output_file = open("results.txt", "w")

start_time = time.time()

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] Port {port}")
        output_file.write(f"[OPEN] Port {port}\n")

    s.close()

end_time = time.time()
output_file.write(f"\nScan completed in {round(end_time - start_time, 2)} seconds.\n")
output_file.close()

print(f"\nScan completed in {round(end_time - start_time, 2)} seconds.")

