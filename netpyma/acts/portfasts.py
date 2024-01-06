def set_portfasts(configs: dict) -> list[str]:
    commands = []
    ranges: list[str] = configs.get('portfasts')
    if not ranges:
        return commands

    for range in ranges:
        commands += [
            f'interface range {range} !',
            'spanning-tree portfast',
            'exit',
        ]

    if commands:
        commands.insert(0, '!** Config portfasts')
    return commands
