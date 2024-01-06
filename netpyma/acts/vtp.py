from netpyma.objs.SpanningTreeConfig import create_spanning_tree_config
from netpyma.objs.VtpConfig import create_vtp_config


def set_vtp(configs: dict) -> list[str]:
    commands = []
    vtp = create_vtp_config(configs)
    if not vtp:
        return commands
    stp = create_spanning_tree_config(configs)

    commands += [
        f'vtp domain {vtp.domain}',
        'vtp version 3',
    ]
    if vtp.is_primary:
        commands += [
            'vtp mode server',
            'exit',
            '!* Set vtp primary',
            'vtp primary force',
            'config terminal !',
            '!* Create VLANs',
            f'vlan {vtp.vlans} !',
            'exit',
        ]
    elif vtp.mode:
        commands.append(f'vtp mode {vtp.mode}')

    if stp and stp.mode == 'mst':
        if stp.mst_server_for_vtp == vtp.domain:
            commands += [
                "vtp mode server mst",
                "exit",
                "vtp primary mst",
                "config terminal !",
            ]
        else:
            commands.append('vtp mode client mst')

    if commands:
        commands.insert(0, '!** Config vtp')
    return commands
