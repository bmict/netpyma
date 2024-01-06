from dataclasses import dataclass
from netpyma.tools.base_tools import kv_args


@dataclass
class SpanningTreeConfig:
    mode: str
    portfast_guard: bool = True
    root: str = None  # primary | secondary
    root_for_vlans: str = None
    costs: dict[str, int] = None
    mst_root_for: str = None
    mst_server_for_vtp: str = None
    mst_instances: dict[int, str] = None
    mst_pirmary_for: int = None
    mst_secondary_for: int = None


def create_spanning_tree_config(configs: dict) -> SpanningTreeConfig:
    spanning_tree = configs.get('spanning_tree')
    if not spanning_tree:
        return None
    if isinstance(spanning_tree, str):
        return SpanningTreeConfig(spanning_tree)
    return SpanningTreeConfig(**kv_args(SpanningTreeConfig, spanning_tree))
