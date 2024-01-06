from ipaddress import ip_interface
from netpyma.tools.ip_tools import get_ipnet
from netpyma.objs.InterfaceConfig import create_interfaces_config


def set_interfaces(configs: dict) -> list[str]:
    commands = []
    cfg_dic = create_interfaces_config(configs)
    if not cfg_dic:
        return commands

    for interface, cfg in cfg_dic.items():
        if cfg.comment:
            commands.append(f'!**** {cfg.comment}')
        commands.append(f'interface {interface} !')
        if cfg.ip:
            ip, netmask = get_ipnet(cfg.ip)
            commands.append(f'ip address {ip} {netmask}')
        if cfg.ip6:
            ip6 = ip_interface(cfg.ip6)
            commands.append(f'ipv6 address {ip6}')
        if cfg.mode == 'trunk':
            commands += [
                'switchport trunk encapsulation dot1q',
                'switchport mode trunk',
                f'switchport trunk allowed vlan {cfg.vlans}',
            ]
        elif cfg.mode == 'access':
            commands += [
                'switchport mode access',
                f'switchport access vlan {cfg.vlan}',
            ]
        if cfg.rootguard:
            commands.append('spanning-tree guard root')
        if cfg.bpduguard:
            commands.append('spanning-tree bpduguard enable')
        if cfg.shutdown:
            commands.append('shutdown')
        else:
            commands.append('no shutdown')
        commands.append(f'exit')

    if commands:
        commands.insert(0, '!** Config interfaces')
    return commands
