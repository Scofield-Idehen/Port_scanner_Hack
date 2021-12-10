import port_scan

ip = input('Please insert ip: ')
port_scan.scan(ip)

targets = input('[+] Enter Target/s To Scan(split by comma: ')
if ',' in targets:
    for ip_add in targets.split(','):
        port_scan.scan(ip_add.strip(' '))
else:
    port_scan.scan(targets)