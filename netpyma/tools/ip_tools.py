import ipaddress


def get_ipnet(input: str):
    if input.count(' ') > 0:
        input = input.replace(' ', '/')
    ipnet = ipaddress.ip_interface(input)
    return [ipnet.ip, ipnet.netmask]


def get_net(input: str):
    if input.count(' ') > 0:
        input = input.replace(' ', '/')
    ipnet = ipaddress.ip_interface(input)
    return [ipnet.network.network_address, ipnet.netmask]
