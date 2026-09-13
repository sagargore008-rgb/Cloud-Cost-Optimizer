from sqlalchemy.orm import Session

from app.db.models import CostRecord


def save_service_costs(
    db: Session,
    services: list
):
    """
    Save AWS service cost data
    into PostgreSQL.
    """

    saved_records = []

    for service in services:

        record = CostRecord(
            service=service["service"],
            cost=service["cost"],
            currency=service["currency"]
        )

        db.add(record)

        saved_records.append(record)

    db.commit()

    return saved_records


def get_saved_costs(
    db: Session
):
    """
    Get all saved cost records
    from PostgreSQL.
    """

    return (
        db.query(CostRecord)
        .order_by(
            CostRecord.recorded_at.desc()
        )
        .all()
    )