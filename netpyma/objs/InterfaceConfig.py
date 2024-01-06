from dataclasses import dataclass
from netpyma.tools.base_tools import kv_args


@dataclass
class InterfaceConfig:
    mode: str = None
    vlan: int = 1
    vlans: str = all
    ip: str = None
    ip6: str = None
    shutdown: bool = None
    comment: str = None
    device: str = None
    rootguard: bool = None
    bpduguard: bool = None


def create_interfaces_config(configs: dict) -> dict[str, InterfaceConfig] | None:
    interfaces: dict[str, dict] = configs.get('interfaces')
    if not interfaces:
        return None
    result: dict[str, InterfaceConfig] = dict()
    for interface, cfg in interfaces.items():
        if isinstance(cfg, str):
            result[interface] = InterfaceConfig(cfg)
        elif isinstance(cfg, dict):
            result[interface] = InterfaceConfig(**kv_args(InterfaceConfig, cfg))
        else:
            raise Exception('Interface config is not valid')
    return result
