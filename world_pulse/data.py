from __future__ import annotations


class PublicDataClient:
    """Boundary for provider and cache operations.

    Screens receive this object instead of making HTTP requests themselves.
    Provider methods will be added in the data tasks that follow.
    """

    def health(self) -> str:
        """Return a simple status until provider methods are implemented."""
        return "Data client ready"
