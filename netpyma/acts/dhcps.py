from netpyma.objs.DhcpConfig import create_dhcps_config


def set_dhcps(configs: dict) -> list[str]:
    commands = []
    cfgs = create_dhcps_config(configs)
    if not cfgs:
        return commands

    for cfg in cfgs:
        commands += [
            f'ip dhcp pool {cfg.name} !',
            f'network {cfg.network}',
        ]
        if cfg.gateway:
            commands.append(f'default-router {cfg.gateway}')
        commands.append(f'exit')
        if cfg.exclude:
            commands.append(f'ip dhcp excluded-address {cfg.exclude}')

    if commands:
        commands.insert(0, '!** Config dhcps')
    return commands
