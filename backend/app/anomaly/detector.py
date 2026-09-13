from statistics import mean, stdev

from app.aws.cost_explorer import get_daily_cost_history


def detect_cost_anomalies(days=30):
    """
    Detect unusual AWS daily spending.

    We calculate the average and standard deviation
    of historical daily costs and identify unusually
    high spending.
    """

    history = get_daily_cost_history(days)

    if len(history) < 3:
        return {
            "status": "insufficient_data",
            "message": "Not enough cost data to detect anomalies.",
            "anomalies": []
        }

    costs = [item["cost"] for item in history]

    average_cost = mean(costs)
    standard_deviation = stdev(costs)

    # Avoid division/threshold problems when all costs are identical.
    if standard_deviation == 0:
        return {
            "status": "normal",
            "average_daily_cost": round(average_cost, 2),
            "anomalies": []
        }

    threshold = average_cost + (2 * standard_deviation)

    anomalies = []

    for item in history:
        daily_cost = item["cost"]

        if daily_cost > threshold:
            percentage_increase = (
                ((daily_cost - average_cost) / average_cost) * 100
                if average_cost > 0
                else 0
            )

            anomalies.append({
                "date": item["date"],
                "cost": round(daily_cost, 2),
                "average_cost": round(average_cost, 2),
                "threshold": round(threshold, 2),
                "increase_percentage": round(
                    percentage_increase,
                    2
                ),
                "severity": "high",
                "message": (
                    "AWS spending is significantly higher "
                    "than the normal daily average."
                )
            })

    return {
        "status": "anomaly_detected" if anomalies else "normal",
        "average_daily_cost": round(average_cost, 2),
        "threshold": round(threshold, 2),
        "anomalies": anomalies
    }