import networkscan
import pynetbox
nb = pynetbox.api(
    'http://192.168.10.53:8000',
    token='0123456789abcdef0123456789abcdef01234567'
)

my_network = "192.168.10.0/24"
myscan = networkscan.Networkscan(my_network)
myscan.run()
for address in  myscan.list_of_hosts_found:
    print(address)
    ip = { 'address': address}
    nb.ipam.ip_addresses.create(ip)
