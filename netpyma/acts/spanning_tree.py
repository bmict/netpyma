from netpyma.objs.SpanningTreeConfig import create_spanning_tree_config


def set_spanning_tree(configs: dict) -> list[str]:
    commands = []
    cfg = create_spanning_tree_config(configs)
    if not cfg:
        return commands

    if cfg.portfast_guard:
        commands += [
            'spanning-tree portfast bpduguard default',
            'spanning-tree portfast bpdufilter default',
        ]

    if cfg.mode == 'mst':
        commands.append('spanning-tree mode mst')
        if cfg.mst_root_for:
            commands += [
                'spanning-tree mst configuration !',
                f'name {cfg.mst_root_for}',
                'revision 1',
            ]
            if cfg.mst_instances:
                for num, vlans in cfg.mst_instances.items():
                    commands.append(f'instance {num} vlan {vlans}')
            else:
                raise Exception(f'No vlan for mst root {cfg.mst_root_for}')
            commands.append('exit')
        if cfg.mst_pirmary_for != None:
            # commands.append(f'spanning-tree mst {cfg.mst_pirmary_for} priority 4096')
            commands.append(f'spanning-tree mst {cfg.mst_pirmary_for} root primary')
        if cfg.mst_secondary_for != None:
            commands.append(f'spanning-tree mst {cfg.mst_secondary_for} root secondary')
    else:
        if cfg.mode == 'rstp':
            commands.append('spanning-tree mode rapid-pvst')
        if cfg.root:
            if not cfg.root_for_vlans:
                raise Exception('Root vlans is not specified.')
            commands.append(
                f'spanning-tree vlan {cfg.root_for_vlans} root {cfg.root}')
    
    if cfg.costs:
        for interface, cost in cfg.costs.items():
            commands += [
                f'interface {interface} !',
                f'spanning-tree cost {cost}',
                'exit'
            ]

    if commands:
        commands.insert(0, '!** Config spanning tree')
    return commands
