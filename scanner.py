import nmap
from colorama import Fore, Back, Style
from colorama import init
init()
scanner = nmap.PortScanner()

print (Fore.LIGHTGREEN_EX + "")
print ("   _______________________________________")
print ("  / Basit nmap aletine hoş geldini :3     \ ")
print ("   nmap versiyonu",scanner.nmap_version(),)
print ("  \_______________________________________/")
ip_adres = input("Hedef ip adresi giriniz: ")
print ("hedef:", ip_adres)
type(ip_adres)

resp = input (""" \n Lütfen tarama seçeneği seçin
                    1) SYN ACK Taraması
                    2) UDP taraması
                    3) Kapsamlı tarama  
                    4) Taramalar hakkında bilgi al""")
print (resp, "seçeneğini seçtiniz")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_adres, '1-1024', '-v -sS')
    print(scanner.scaninfo())
    print("Hedef durumu: ", scanner[ip_adres].state())
    print(scanner[ip_adres].all_protocols())
    print ("Açık portlar: ", scanner[ip_adres]['tcp'].keys())
if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_adres, '1-1024', '-v -sU')
    print(scanner.scaninfo())
    print("Hedef durumu: ", scanner[ip_adres].state())
    print(scanner[ip_adres].all_protocols())
    print ("Açık portlar: ", scanner[ip_adres]['udp'].keys())
if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_adres, '1-1024', '-v -sS -sV -sC -A -0')
    print(scanner.scaninfo())
    print("Hedef durumu: ", scanner[ip_adres].state())
    print(scanner[ip_adres].all_protocols())
    print ("Açık portlar: ", scanner[ip_adres]['tcp'].keys())
else: 
    print "Sana sunulan seçeneklerden fazlasını istiyorsun... Alamayacaksın"