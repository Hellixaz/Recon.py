# Recon.py

Recon.py aims to automate asset discovery process. It is recommended to run as root to avoid any problems.

After usage creates 3 different txt files in Outputs directory, which contains:

- Subdomains.txt (Contain subdomains)
- IP.txt (Contain IP list)
- Ports.txt (Contain Ports)

## Requirements 

- Please read requirements.txt. If you need Install and update any requirements check Installations step.


## Installations

- Set permissions

```
chmod +x ./Installation.sh
```

- Requirements Install

```
./Installation.sh
```


## Usage

```
python3 Recon.py <domain>
```
## Usage example

```
python3 Recon.py example.com
```

