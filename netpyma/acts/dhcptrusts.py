def set_dhcptrusts(configs: dict) -> list[str]:
    commands = []
    ranges: list[str] = configs.get('dhcptrusts')
    if ranges == None:
        return commands
    
    commands.append('ip dhcp snooping')
    for range in ranges:
        commands += [
            f'interface range {range} !',
            'ip dhcp snooping trust',
            'exit',
        ]

    if commands:
        commands.insert(0, '!** Config dhcp trust ports')
    return commands
