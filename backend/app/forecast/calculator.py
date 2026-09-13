from datetime import date
import calendar

from app.aws.cost_explorer import get_current_month_cost


def calculate_cost_forecast():
    """
    Estimate the AWS bill at the end of the current month
    based on the average daily spending so far.
    """

    current_data = get_current_month_cost()

    current_cost = current_data["cost"]

    today = date.today()

    year = today.year
    month = today.month

    total_days = calendar.monthrange(year, month)[1]

    days_elapsed = today.day

    days_remaining = total_days - days_elapsed

    # Calculate average daily cost
    if days_elapsed > 0:
        average_daily_cost = current_cost / days_elapsed
    else:
        average_daily_cost = 0

    # Estimate full month cost
    forecast_cost = average_daily_cost * total_days

    # Calculate remaining expected cost
    remaining_forecast = (
        average_daily_cost * days_remaining
    )

    return {
        "currency": "USD",
        "current_cost": round(current_cost, 2),
        "days_elapsed": days_elapsed,
        "days_remaining": days_remaining,
        "total_days": total_days,
        "average_daily_cost": round(
            average_daily_cost,
            2
        ),
        "remaining_forecast": round(
            remaining_forecast,
            2
        ),
        "estimated_month_end_cost": round(
            forecast_cost,
            2
        )
    }