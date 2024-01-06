from netpyma.objs.VrfConfig import create_vrfs_config


def set_vrfs(configs: dict) -> list[str]:
    commands = []
    vrfs = create_vrfs_config(configs)
    if not vrfs:
        return commands
    
    # Enable CEF globally before configuring VRF on any interface
    commands.append('ip cef')
    for vrf in vrfs:
        commands += [
            f'vrf definition {vrf.name} !',
            f'address-family ipv{vrf.version} !',
            'exit',
            'exit',
        ]
        for interface in vrf.interfaces:
            commands += [
                f'interface {interface} !',
                f'vrf forwarding {vrf.name}',
                'exit',
            ]

    if commands:
        commands.insert(0, '!** Config vrfs')
    return commands
