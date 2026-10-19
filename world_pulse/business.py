from dataclasses import dataclass


@dataclass(frozen=True)
class CostResult:
    daily_fuel: float
    monthly_fuel: float
    income_percent: float
    remaining_budget: float


def calculate_cost(
    distance: float,
    efficiency: float,
    petrol_price: float,
    days: int,
    income: float,
    expenses: float,
    efficiency_unit: str = "km / L",
) -> CostResult:
    if distance <= 0:
        raise ValueError("Distance must be greater than zero.")
    if efficiency <= 0:
        raise ValueError("Efficiency must be greater than zero.")
    if petrol_price <= 0:
        raise ValueError("Petrol price must be greater than zero.")
    if days <= 0:
        raise ValueError("Travel days must be greater than zero.")
    if income < 0 or expenses < 0:
        raise ValueError("Income and expenses cannot be negative.")
    if efficiency_unit not in {"km / L", "L / 100 km"}:
        raise ValueError("Choose a supported efficiency unit.")

    litres = distance / efficiency
    if efficiency_unit == "L / 100 km":
        litres = distance * efficiency / 100

    daily_fuel = litres * petrol_price
    monthly_fuel = daily_fuel * days

    return CostResult(
        daily_fuel=daily_fuel,
        monthly_fuel=monthly_fuel,
        income_percent=monthly_fuel / income * 100 if income else 0.0,
        remaining_budget=income - expenses - monthly_fuel,
    )
