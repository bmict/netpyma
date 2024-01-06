def set_rootguards(configs: dict) -> list[str]:
    commands = []
    ranges: list[str] = configs.get('rootguards')
    if not ranges:
        return commands

    for range in ranges:
        commands += [
            f'interface range {range} !',
            'spanning-tree guard root',
            'exit',
        ]

    if commands:
        commands.insert(0, '!** Config rootguards')
    return commands
