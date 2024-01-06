def set_udld(configs: dict) -> list[str]:
    commands = []
    enabled: bool = configs.get('udld')
    if not enabled:
        return commands

    commands.append('udld enable')

    if commands:
        commands.insert(0, '!** Config udld')
    return commands
