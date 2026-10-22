from __future__ import annotations
from dataclasses import dataclass, field

@dataclass(frozen=True)
class Freshness:
    source: str
    label: str
    timestamp: str = "Not synced"

@dataclass(frozen=True)
class Metric:
    label: str
    value: str
    unit: str = ""
    change: str = ""
    tone: str = "neutral"
    freshness: Freshness = field(
        default_factory=lambda: Freshness("World Pulse", "Unavailable")
    )
    spark: tuple[float, ...] = ()

@dataclass(frozen=True)
class Country:
    name: str
    code: str
    region: str
    currency: str
    population: str = "—"
    gdp: str = "—"
    inflation: str = "—"
    temperature: str = "—"
    freshness: Freshness = field(
        default_factory=lambda: Freshness("World Bank", "Historical")
    )

class PublicDataClient:
    """Boundary for provider and cache operations.

    Screens receive this object instead of making HTTP requests themselves.
    Provider methods will be added in the data tasks that follow.
    """

    def health(self) -> str:
        """Return a simple status until provider methods are implemented."""
        return "Data client ready"