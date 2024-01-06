from netmiko import ConnectHandler, BaseConnection


def create_connection(port: int) -> BaseConnection:
    cisco_device = {
        'device_type': 'cisco_ios_telnet',
        'host': '192.168.179.130',
        'port': port,
    }
    return ConnectHandler(**cisco_device)
