from dataclasses import dataclass
from netpyma.tools.base_tools import kv_args


@dataclass
class AggregationConfig:
    channel: int
    mode: str
    interfaces: list[str]
    device: str


def create_aggregation_configs(configs: dict) -> list[AggregationConfig]:
    channels: list[dict] = configs.get('link_aggregations')
    if not channels:
        return []
    return [AggregationConfig(**kv_args(AggregationConfig, ch)) for ch in channels]
