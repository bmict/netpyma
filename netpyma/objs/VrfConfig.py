from dataclasses import dataclass
from netpyma.tools.base_tools import kv_args


@dataclass
class VrfConfig:
    name: str
    version: int = 4
    interfaces: list[str] = None


def create_vrfs_config(configs: dict) -> list[VrfConfig] | None:
    vrfs = configs.get('vrfs')
    if not vrfs:
        return None
    result: list[VrfConfig] = []
    for vrf in vrfs:
        result.append(VrfConfig(**kv_args(VrfConfig, vrf)))
    return result
