import networkscan 
from netbox import NetBox
netbox = NetBox(host='192.168.10.53', port=8000, use_ssl=False, auth_token='0123456789abcdef0123456789abcdef01234567')



my_network = "192.168.10.0/24"
myscan = networkscan.Networkscan(my_network)
myscan.run()
for address in  myscan.list_of_hosts_found:
    print(address)
    netbox.ipam.create_ip_address(address)
        
