def fill_rows(commands: list[str], value: str | list | dict):
    if isinstance(value, str):
        commands.append(value)
        return
    if isinstance(value, list):
        for item in value:
            fill_rows(commands, item)
        return
    if isinstance(value, dict):
        for key, val in value.items():
            commands.append(key)
            fill_rows(commands, val)
        return
    raise Exception('Extra value is not valid')


def set_extra(configs: dict) -> list[str]:
    commands = []
    extra: str | list | dict = configs.get('extra')
    if not extra:
        return commands

    fill_rows(commands, extra)

    if commands:
        commands.insert(0, '!** Config extra commands')
    return commands
