from dataclasses import dataclass
from netpyma.tools.base_tools import get_kargs


@dataclass
class VlanConfig:
    number: int
    ip: str = None


def create_vlans_config(configs: dict) -> list[VlanConfig] | None:
    vlans: dict[str, dict] = configs.get('vlans')
    if not vlans:
        return None
    result: list[VlanConfig] = []
    for number, cfg in vlans.items():
        result.append(VlanConfig(number, *get_kargs(cfg, 'ip')))
    return result
