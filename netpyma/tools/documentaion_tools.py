from pathlib import Path


def save_config_file(hostname: str, commands: list[str], path: Path):
    with open(path, 'wt', encoding='utf-8') as save_file:
        save_file.write(f'!** M.Soltani, {hostname} config file\n\n')
        save_file.write('!** ==================================\n\n')
        save_file.write('!** Begin Config\nconfig terminal\n\n')
        indent = 2
        for line in commands:
            temp_indent = -1
            if line[-2:] == ' !':
                temp_indent = indent + 2
                line = line[:-2]
            elif line == 'exit':
                temp_indent = indent - 2
                if temp_indent < 0:
                    raise Exception('\nIndent error')
            save_file.write(' '*indent + line + '\n')
            if temp_indent >= 0:
                indent = temp_indent
        save_file.write('!Write Config\n  exit\nwrite\n\n')
    return
