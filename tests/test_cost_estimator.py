import subprocess
import sys

import pytest

from tools.cost_estimator import (
    CostScenario,
    break_even_hours,
    effective_purchase_cost,
    rental_cost,
)


def test_rental_cost_includes_runtime_and_storage() -> None:
    scenario = CostScenario(
        purchase_cost=55_000,
        hourly_rate=10,
        hours=100,
        storage_monthly=150,
        months=1,
    )
    assert rental_cost(scenario) == pytest.approx(1_150)


def test_effective_purchase_cost() -> None:
    scenario = CostScenario(
        purchase_cost=55_000,
        hourly_rate=10,
        hours=100,
        residual_value=15_000,
        maintenance_total=5_000,
    )
    assert effective_purchase_cost(scenario) == pytest.approx(45_000)


def test_break_even_hours() -> None:
    scenario = CostScenario(
        purchase_cost=55_000,
        hourly_rate=10,
        hours=100,
        storage_monthly=150,
        months=1,
    )
    assert break_even_hours(scenario) == pytest.approx(5_485)


def test_storage_above_ownership_cost_clamps_break_even_to_zero() -> None:
    scenario = CostScenario(
        purchase_cost=1_000,
        hourly_rate=10,
        hours=0,
        storage_monthly=600,
        months=2,
    )
    assert break_even_hours(scenario) == pytest.approx(0)


def test_zero_hourly_rate_has_no_break_even() -> None:
    scenario = CostScenario(purchase_cost=55_000, hourly_rate=0, hours=100)
    assert break_even_hours(scenario) is None


def test_negative_values_are_rejected() -> None:
    scenario = CostScenario(purchase_cost=55_000, hourly_rate=-1, hours=100)
    with pytest.raises(ValueError):
        rental_cost(scenario)


def test_residual_value_cannot_exceed_total_outlay() -> None:
    scenario = CostScenario(
        purchase_cost=1_000,
        hourly_rate=10,
        hours=10,
        residual_value=1_001,
    )
    with pytest.raises(ValueError):
        effective_purchase_cost(scenario)


def test_cli_outputs_currency_and_break_even() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "tools/cost_estimator.py",
            "--purchase-cost",
            "55000",
            "--hourly-rate",
            "10",
            "--hours",
            "100",
            "--storage-monthly",
            "150",
            "--currency",
            "PLN",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    assert "Rental cost: 1,150.00 PLN" in result.stdout
    assert "Simplified break-even: 5,485.0 hours" in result.stdout
