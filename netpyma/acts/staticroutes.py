from netpyma.objs.StaticRouteConfig import create_staticroutes_config


def set_staticroutes(configs: dict) -> list[str]:
    # Prepend and Append extra configs must be added
    commands = []
    staticroutes = create_staticroutes_config(configs)
    if not staticroutes:
        return commands

    for sr in staticroutes:
        command = []
        vrf = f'vrf {sr.vrf} ' if sr.vrf else ''
        if sr.network.version == 6:
            command.append(f'ipv6 route {vrf}{sr.network}')
        else:
            command.append(f'ip route {vrf}{sr.network.network_address} {sr.network.netmask}')
        if sr.interface:
            if sr.interface[0].lower() == 'e':
                command.append(f'Ethernet {sr.interface[1:]}')
            elif sr.interface[0].lower() == 's':
                command.append(f'Serial {sr.interface[1:]}')
            elif sr.interface[0].lower() == 'n':
                command.append(f'Null 0')
            else:
                raise Exception(f'Interface type {sr.interface} not support')
        if sr.gateway:
            command.append(str(sr.gateway))
        if sr.distance:
            command.append(str(sr.distance))
        if sr.name:
            command.append(f'name {sr.name}')
        if sr.comment:
            commands.append(f'!**** {sr.comment}')
        commands.append(' '.join(command))

    if commands:
        commands.insert(0, '!** Config static routes')
    return commands
