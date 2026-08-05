"""Educational cloud-rental versus hardware-purchase estimator."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class CostScenario:
    purchase_cost: float
    hourly_rate: float
    hours: float
    storage_monthly: float = 0.0
    months: float = 1.0
    residual_value: float = 0.0
    maintenance_total: float = 0.0

    def validate(self) -> None:
        values = {
            "purchase_cost": self.purchase_cost,
            "hourly_rate": self.hourly_rate,
            "hours": self.hours,
            "storage_monthly": self.storage_monthly,
            "months": self.months,
            "residual_value": self.residual_value,
            "maintenance_total": self.maintenance_total,
        }
        for name, value in values.items():
            if value < 0:
                raise ValueError(f"{name} must be non-negative")
        if self.residual_value > self.purchase_cost + self.maintenance_total:
            raise ValueError("residual_value cannot exceed total ownership outlay")


def rental_cost(scenario: CostScenario) -> float:
    scenario.validate()
    return scenario.hourly_rate * scenario.hours + scenario.storage_monthly * scenario.months


def effective_purchase_cost(scenario: CostScenario) -> float:
    scenario.validate()
    return scenario.purchase_cost + scenario.maintenance_total - scenario.residual_value


def break_even_hours(scenario: CostScenario) -> float | None:
    scenario.validate()
    if scenario.hourly_rate == 0:
        return None
    fixed_storage = scenario.storage_monthly * scenario.months
    remaining = effective_purchase_cost(scenario) - fixed_storage
    return max(0.0, remaining / scenario.hourly_rate)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare simplified cloud rental and hardware purchase costs."
    )
    parser.add_argument("--purchase-cost", type=float, required=True)
    parser.add_argument("--hourly-rate", type=float, required=True)
    parser.add_argument("--hours", type=float, required=True)
    parser.add_argument("--storage-monthly", type=float, default=0.0)
    parser.add_argument("--months", type=float, default=1.0)
    parser.add_argument("--residual-value", type=float, default=0.0)
    parser.add_argument("--maintenance-total", type=float, default=0.0)
    parser.add_argument("--currency", default="PLN")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    scenario = CostScenario(
        purchase_cost=args.purchase_cost,
        hourly_rate=args.hourly_rate,
        hours=args.hours,
        storage_monthly=args.storage_monthly,
        months=args.months,
        residual_value=args.residual_value,
        maintenance_total=args.maintenance_total,
    )
    try:
        rent = rental_cost(scenario)
        ownership = effective_purchase_cost(scenario)
        break_even = break_even_hours(scenario)
    except ValueError as exc:
        raise SystemExit(f"Invalid input: {exc}") from exc

    print(f"Rental cost: {rent:,.2f} {args.currency}")
    print(f"Effective purchase cost: {ownership:,.2f} {args.currency}")
    print(f"Difference (purchase - rental): {ownership - rent:,.2f} {args.currency}")
    if break_even is None:
        print("Break-even hours: undefined because hourly rate is zero")
    else:
        print(f"Simplified break-even: {break_even:,.1f} hours")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
