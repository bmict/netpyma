from dataclasses import dataclass
from netpyma.tools.base_tools import kv_args


@dataclass
class IdentifyConfig:
    hostname: str
    domain: str
    is_pc: str = ''
    ip6: bool = False


def create_identify_config(configs: dict) -> IdentifyConfig:
    return IdentifyConfig(**kv_args(IdentifyConfig, configs))
