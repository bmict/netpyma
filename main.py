import sys
from pathlib import Path
from threading import Thread
from yaml import load, Loader
from netpyma.tools.connection_tools import create_connection
from netpyma.tools.documentaion_tools import save_config_file
from netpyma.acts import ALL_SETTERS


def config_set(port, configs: dict, prj_folder: Path):
    apply = sys.argv.count('-a') > 0
    config_commands = []
    for fn in ALL_SETTERS:
        fn_new_commands = fn(configs)
        if fn_new_commands:
            config_commands += fn_new_commands
            config_commands.append('\n')
    if apply:
        ios_device = create_connection(port)
        ios_device.send_config_set(config_commands)
    out_folder = prj_folder.joinpath('./dist')
    if not Path.exists(out_folder):
        out_folder.mkdir()
    if hostname := configs.get('hostname'):
        save_config_file(hostname, config_commands, out_folder.joinpath(f'./{hostname}.cfg'))
    return


def run(prj_folder: Path, verbose: bool):
    cfg_file = prj_folder.joinpath('./configs.yml')
    if not Path.exists(cfg_file):
        raise Exception('config.yml file not found.')
    configs_file = cfg_file.read_text()
    configs_list: dict = load(configs_file, Loader)
    if not configs_list:
        print('Nothing to config.')
        return
    if verbose:
        print(configs_list)
    threads = list()
    for _, configs in configs_list.items():
        th = Thread(target=config_set, args=(configs['port'], configs, prj_folder))
        threads.append(th)

    for th in threads:
        th.start()

    for th in threads:
        th.join()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise Exception('Select a project')
    prj = sys.argv[1]
    prj_folder = Path(prj)
    if not Path.exists(prj_folder):
        raise Exception(f'Project {prj} not found.')
    verbose = False
    if sys.argv.count('-V'):
        verbose = True
    run(prj_folder, verbose)
    