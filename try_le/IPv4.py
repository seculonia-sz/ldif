x = int(1)
cidr = int(0)

while x != 0:
    cidr = int(input("Geben Sie Ihre Cidr Adresse an: "))

    netmask = '.'.join([str((m>>(3-i)*8)&0xff) for i,m in enumerate([-1<<(32-cidr)]*4)])
    print(netmask)