from dataclasses import dataclass
from ipaddress import IPv4Network, IPv6Network, IPv4Address, IPv6Address, ip_network, ip_address
from netpyma.tools.base_tools import get_kargs, get_args


@dataclass
class StaticRouteConfig:
    network: IPv4Network|IPv6Network
    gateway: IPv4Address|IPv6Address = None
    distance: int = None
    interface: str = None
    name: str = None
    comment: str = None
    vrf: str = None


def create_staticroutes_config(configs: dict) -> list[StaticRouteConfig] | None:
    cfgs: list[dict | list] = configs.get('staticroutes')
    if not cfgs:
        return None

    result: list[StaticRouteConfig] = []
    for cfg in cfgs:
        if isinstance(cfg, list):
            network, gateway, distance, interface, name, comment, vrf = get_args(
                cfg, 7)
        elif isinstance(cfg, dict):
            network, gateway, distance, interface, name, comment, vrf = get_kargs(
                cfg, 'network', 'gateway', 'distance', 'interface', 'name', 'comment', 'vrf')
        else:
            raise Exception('Static route type is not valid.')
        network = ip_network(network)
        if gateway:
            gateway = ip_address(gateway)
        if name and name.count(' ') > 0:
            raise Exception('Route name is not valid')
        result.append(StaticRouteConfig(
            network, gateway, distance, interface, name, comment, vrf))

    return result
