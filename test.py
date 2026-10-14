from world_pulse.business import calculate_cost
 
 
def test_basic_cost() -> None:
    result = calculate_cost(100, 20, 300, 2, 100000, 20000)
    assert result.daily_fuel == 1500
    assert result.monthly_fuel == 3000