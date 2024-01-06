from netpyma.objs.AggregationConfig import create_aggregation_configs


def set_link_aggregations(configs: dict) -> list[str]:
    cfgs = create_aggregation_configs(configs)
    commands = []
    for cfg in cfgs:
        if cfg.device:
            commands += [
                '!*',
                f'!** Set link aggregation with {cfg.device}',
            ]
        for interface in cfg.interfaces:
            commands += [
                f'interface {interface} !',
                f'channel-group {cfg.channel} mode {cfg.mode}',
                'exit',
            ]
        commands += [
            f'interface port-channel {cfg.channel} !',
            'switchport trunk encap dot1q',
            'switchport mode trunk',
            'exit',
        ]
    if commands:
        commands.insert(0, '!** Config link aggregations')
    return commands
