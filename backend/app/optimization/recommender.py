from app.aws.cost_explorer import get_cost_by_service


def generate_optimization_recommendations():
    services = get_cost_by_service()

    recommendations = []

    for service in services:
        service_name = service["service"]
        cost = service["cost"]

        if "Elastic Compute Cloud" in service_name:
            if cost > 10:
                priority = "high"
                recommendation = (
                    "Review EC2 instance utilization. "
                    "Consider right-sizing instances or using "
                    "Savings Plans for consistent workloads."
                )
            elif cost > 1:
                priority = "medium"
                recommendation = (
                    "Review EC2 CPU and memory utilization "
                    "and consider right-sizing underutilized instances."
                )
            else:
                priority = "low"
                recommendation = (
                    "EC2 spending is currently low. "
                    "Continue monitoring instance usage."
                )

        elif "Virtual Private Cloud" in service_name:
            if cost > 5:
                priority = "high"
                recommendation = (
                    "Review NAT Gateway, public IPv4, and data "
                    "processing charges. Remove unused resources."
                )
            elif cost > 1:
                priority = "medium"
                recommendation = (
                    "Review VPC networking resources and check "
                    "for unnecessary NAT Gateway or public IPv4 usage."
                )
            else:
                priority = "low"
                recommendation = (
                    "VPC spending is currently low. "
                    "Continue monitoring networking resources."
                )

        elif "Simple Storage Service" in service_name:
            if cost > 5:
                priority = "medium"
                recommendation = (
                    "Review S3 storage usage and lifecycle policies."
                )
            else:
                priority = "low"
                recommendation = (
                    "S3 spending is currently low. "
                    "Continue monitoring storage growth."
                )

        elif "Secrets Manager" in service_name:
            priority = "low"
            recommendation = (
                "Review unused secrets and remove secrets "
                "that are no longer required."
            )

        elif "Cost Explorer" in service_name:
            priority = "low"
            recommendation = (
                "Avoid unnecessary or overly frequent "
                "Cost Explorer API requests."
            )

        elif service_name == "Tax":
            priority = "low"
            recommendation = (
                "Tax charges are based on applicable AWS usage "
                "and generally cannot be optimized directly."
            )

        else:
            priority = "low"
            recommendation = (
                "Review this service for unused or unnecessary "
                "resources."
            )

        recommendations.append(
            {
                "service": service_name,
                "cost": cost,
                "priority": priority,
                "recommendation": recommendation,
            }
        )

    recommendations.sort(
        key=lambda item: item["cost"],
        reverse=True
    )

    return {
        "status": "success",
        "total_services": len(services),
        "recommendations": recommendations,
    }