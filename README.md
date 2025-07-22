# 🛡️ Port Scanner - CodeAlpha Internship Task 2

## 📌 Description
This is a simple **Port Scanner** developed using **Python** as part of my Cyber Security Internship at **CodeAlpha**.  
The scanner checks for **open TCP ports** on a target IP address and stores the results in a file.

> 🔧 Note: This project was developed in addition to the required task (Basic Network Sniffer) as an extra effort to improve my understanding of cybersecurity scanning tools.

## 💡 Features
- Scan ports in the range **1–1024**
- Identify open ports on any IP
- Save results to `results.txt`
- Fast scanning with socket timeout handling

## 🛠️ Technologies Used
- Python 3
- socket
- time

## 🚀 How It Works
1. The user is prompted to enter the **target IP address**.
2. The script iterates through common TCP ports (1–1024).
3. For each port, it tries to establish a connection:
   - If successful → port is marked as **OPEN**.
4. The open ports are printed to the terminal and saved to `results.txt`.

## 📷 Sample Output

┌──(kali㉿kali)-[~/PortScanner]
└─$ cat results.txt

[OPEN] Port 21
[OPEN] Port 22
[OPEN] Port 23
[OPEN] Port 25
[OPEN] Port 53
[OPEN] Port 80
[OPEN] Port 111
[OPEN] Port 139
[OPEN] Port 445
[OPEN] Port 512
[OPEN] Port 513
[OPEN] Port 514

Scan completed in 0.73 seconds.

## 📁 Files
- `port_scanner.py` → main scanning script
- `results.txt` → output file of open ports
- `README.md` → project documentation

## 🎯 Author
**Farah Ibrahim Al Tahat**  
Cyber Security Intern @ CodeAlpha
[LinkedIn Profile](https://www.linkedin.com/in/farah-al-tahat-a79176331)  
[GitHub Profile](https://github.com/FarahAlTahat)

## 🔖 Tags
`#Python` `#CyberSecurity` `#PortScanner` `#CodeAlpha` `#InternshipTasks`
