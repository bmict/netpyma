from netmiko import ConnectHandler, BaseConnection


def create_connection(ip: str, port: int) -> BaseConnection:
    cisco_device = {
        'device_type': 'cisco_ios_telnet',
        'host': ip,
        'port': port,
    }
    return ConnectHandler(**cisco_device)
