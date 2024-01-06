from dataclasses import dataclass
from netpyma.tools.base_tools import kv_args


@dataclass
class DhcpConfig:
    name: str
    network: str
    exclude: str = None
    gateway: str = None


def create_dhcps_config(configs: dict) -> list[DhcpConfig] | None:
    dhcps: list[dict] = configs.get('dhcps')
    if not dhcps:
        return None
    result: list[DhcpConfig] = []
    for cfg in dhcps:
        result.append(DhcpConfig(**kv_args(DhcpConfig, cfg)))
    return result
