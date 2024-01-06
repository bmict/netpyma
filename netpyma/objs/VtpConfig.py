from dataclasses import dataclass
from netpyma.tools.base_tools import kv_args


@dataclass
class VtpConfig:
    domain: str
    mode: str = None
    is_primary: bool = False
    vlans: str = None


def create_vtp_config(configs: dict) -> VtpConfig | None:
    vtp = configs.get('vtp')
    if not vtp:
        return None
    if isinstance(vtp, str):
        return VtpConfig(vtp)
    return VtpConfig(**kv_args(VtpConfig, vtp))
