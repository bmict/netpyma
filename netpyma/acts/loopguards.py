def set_loopguards(configs: dict) -> list[str]:
    commands = []
    enabled: bool = configs.get('loopguards')
    if not enabled:
        return commands

    commands.append('spanning-tree loopguard default')

    if commands:
        commands.insert(0, '!** Config loop guard')
    return commands
