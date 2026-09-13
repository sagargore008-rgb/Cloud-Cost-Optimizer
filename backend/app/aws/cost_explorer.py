import boto3
from datetime import date, timedelta


def get_cost_explorer_client():
    return boto3.client("ce", region_name="us-east-1")


def get_current_month_cost():
    client = get_cost_explorer_client()

    today = date.today()

    start_date = today.replace(day=1)
    end_date = today + timedelta(days=1)

    response = client.get_cost_and_usage(
        TimePeriod={
            "Start": start_date.strftime("%Y-%m-%d"),
            "End": end_date.strftime("%Y-%m-%d")
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"]
    )

    amount = response["ResultsByTime"][0]["Total"][
        "UnblendedCost"
    ]["Amount"]

    return {
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": today.strftime("%Y-%m-%d"),
        "currency": "USD",
        "cost": float(amount)
    }


def get_cost_by_service():
    client = get_cost_explorer_client()

    today = date.today()

    start_date = today.replace(day=1)
    end_date = today + timedelta(days=1)

    response = client.get_cost_and_usage(
        TimePeriod={
            "Start": start_date.strftime("%Y-%m-%d"),
            "End": end_date.strftime("%Y-%m-%d")
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"],
        GroupBy=[
            {
                "Type": "DIMENSION",
                "Key": "SERVICE"
            }
        ]
    )

    services = []

    results = response["ResultsByTime"]

    if not results:
        return services

    groups = results[0].get("Groups", [])

    for group in groups:
        service_name = group["Keys"][0]

        amount = float(
            group["Metrics"]["UnblendedCost"]["Amount"]
        )

        if amount > 0:
            services.append({
                "service": service_name,
                "cost": round(amount, 2),
                "currency": "USD"
            })

    services.sort(
        key=lambda x: x["cost"],
        reverse=True
    )

    return services


def get_daily_cost_history(days=30):
    client = get_cost_explorer_client()

    today = date.today()

    start_date = today - timedelta(days=days)
    end_date = today + timedelta(days=1)

    response = client.get_cost_and_usage(
        TimePeriod={
            "Start": start_date.strftime("%Y-%m-%d"),
            "End": end_date.strftime("%Y-%m-%d")
        },
        Granularity="DAILY",
        Metrics=["UnblendedCost"]
    )

    history = []

    for result in response["ResultsByTime"]:
        amount = float(
            result["Total"]["UnblendedCost"]["Amount"]
        )

        history.append({
            "date": result["TimePeriod"]["Start"],
            "cost": round(amount, 2),
            "currency": "USD"
        })

    return history