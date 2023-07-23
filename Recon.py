import subprocess
import sys
import dns.resolver
import time

try:
    domain = sys.argv[1]
except IndexError:
    print('Syntax Error - python3 Komutyazdırma.py <domain>')
    sys.exit(1)

##########################################################################################################
#HARVESTER SUBDOMAIN ENUM

print("-----------------------------------------")
print("Starting subdomain enum with theHarvester")
print("-----------------------------------------")

komut5 = f"theHarvester -d {domain} -b anubis,baidu,bevigil,binaryedge,bing,bingapi,bufferoverun,brave,certspotter,criminalip,crtsh,dnsdumpster,duckduckgo,fullhunt,github-code,hackertarget,hunter,hunterhow,intelx,otx,pentesttools,projectdiscovery,rapiddns,rocketreach,securityTrails,sitedossier,subdomainfinderc99,threatminer,urlscan,virustotal,yahoo,zoomeye"  # domain değişkenini komut5 içinde kullanarak oluşturuyoruz


# Komutu çalıştırma
try:
    cikti = subprocess.check_output(komut5, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    print("Çıktı:\n", cikti)
except subprocess.CalledProcessError as e:
    print("Hata oluştu. Hata kodu:", e.returncode)
    print("Hata mesajı:", e.output)
time.sleep(3)
# Komutu çalıştırma
try:
    cikti = subprocess.check_output(komut5, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    print("Çıktı:\n", cikti)

    # Çıktıyı dosyaya kaydetme
    with open("harvester.txt", "w") as dosya:
        dosya.write(cikti)
    

except subprocess.CalledProcessError as e:
    print("Hata oluştu. Hata kodu:", e.returncode)
    print("Hata mesajı:", e.output)
time.sleep(3)
#############################################################################################################
#ÇIKTI DÜZENLEME

output_file = 'Subdomains.txt'

with open('harvester.txt', 'r') as file:
    lines = file.readlines()

output_lines = []
found_hosts = False

for line in lines:
    if found_hosts:
        output_lines.append(line)
    elif '[*] Hosts found: ' in line:
        found_hosts = True

with open(output_file, 'w') as file:
    file.writelines(output_lines)

print('İşlem tamamlandı. Çıktı dosyası: ' + output_file)

time.sleep(3)


##############################################################################################################
#NAABU SCRIPT

naabu3 = "naabu -l Subdomains.txt -o Ports.txt "  # domain değişkenini komut5 içinde kullanarak oluşturuyoruz

print("-----------------------------------")
print("Starting Naabu for Port Enumeration")
print("-----------------------------------")

# Komutu çalıştırma
try:
    cikti = subprocess.check_output(naabu3, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
    print("Çıktı:\n", cikti)
except subprocess.CalledProcessError as e:
    print("Hata oluştu. Hata kodu:", e.returncode)
    print("Hata mesajı:", e.output)
    
##############################################################################################################

#IP TEXT

output_file = 'IP.txt'

with open('harvester.txt', 'r') as file:
    lines = file.readlines()

output_lines = []
found_hosts = False

for line in lines:
    if '[*] IPs found: ' in line:
        found_hosts = True
    elif '[*] Emails found: ' in line:
        break

    if found_hosts:
        output_lines.append(line)

with open(output_file, 'w') as file:
    file.writelines(output_lines)

print('İşlem tamamlandı. Çıktı dosyası: ' + output_file)

    
    
    
    
    
##############################################################################################################

#HARVESTER FİLE DELETE

delete= "rm harvester.txt"
cikti = subprocess.check_output(delete, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

##############################################################################################################

#MAKE OUTPUT DIRECTORY

dircreate= "mkdir Outputs"
cikti = subprocess.check_output(dircreate, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)

##############################################################################################################

#MOVING OUTPUTS

move1= "mv Subdomains.txt Outputs"
move2= "mv IP.txt Outputs"
move3= "mv Ports.txt Outputs"

cikti = subprocess.check_output(move1, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
cikti = subprocess.check_output(move2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
cikti = subprocess.check_output(move3, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)


##############################################################################################################















