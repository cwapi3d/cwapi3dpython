from dataclasses import dataclass
from typing import Optional
from cadwork import point_3d


@dataclass(frozen=True)
class active_point_result:
    has_point: bool
    point: Optional["point_3d"] = None

    def __bool__(self) -> bool:
        return self.has_point
