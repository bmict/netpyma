from netpyma.objs.VlanConfig import create_vlans_config


def set_vlans(configs: dict) -> list[str]:
    commands = []
    cfgs = create_vlans_config(configs)
    if not cfgs:
        return commands

    for cfg in cfgs:
        commands += [
            f'interface vlan {cfg.number} !',
            'no shutdown'
        ]
        if cfg.ip:
            commands.append(f'ip address {cfg.ip}')
        commands.append(f'exit')

    if commands:
        commands.insert(0, '!** Config vlans')
    return commands
