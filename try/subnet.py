import ipaddress

net4 = ipaddress.ip_network('192.0.2.0/24')

print(net4)
print(net4.netmask)