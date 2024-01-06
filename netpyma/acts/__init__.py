from .identify import set_identify
from .aggregation import set_link_aggregations
from .spanning_tree import set_spanning_tree
from .vtp import set_vtp
from .interfaces import set_interfaces
from .vlans import set_vlans
from .dhcps import set_dhcps
from .rootguards import set_rootguards
from .udld import set_udld
from .portfasts import set_portfasts
from .dhcptrusts import set_dhcptrusts
from .loopguards import set_loopguards
from .staticroutes import set_staticroutes
from .vrfs import set_vrfs
from .extra import set_extra

ALL_SETTERS = [
    set_identify,
    set_vrfs,
    set_interfaces,
    set_portfasts,
    set_link_aggregations,
    set_spanning_tree,
    set_vtp,
    set_vlans,
    set_dhcps,
    set_rootguards,
    set_udld,
    set_loopguards,
    set_dhcptrusts,
    set_staticroutes,
    set_extra,
]
