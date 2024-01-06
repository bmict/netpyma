from netpyma.objs.IdentifyConfig import create_identify_config


def set_identify(configs: dict) -> list[str]:
    cfg = create_identify_config(configs)
    commands = []

    if cfg.hostname:
        commands.append(f'hostname {cfg.hostname}')
    if cfg.domain:
        commands.append(f'ip domain name {cfg.domain}')
    if cfg.is_pc:
        commands += [
            '!**** This router is a pc',
            f'no ip routing',
            f'ip default-gateway {cfg.is_pc}'
        ]
    elif cfg.ip6:
        commands.append('ipv6 unicast-routing')

    if commands:
        commands.insert(0, '!** Config identifications')
    return commands
