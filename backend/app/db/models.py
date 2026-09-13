from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)

from datetime import datetime

from app.db.database import Base


class CostRecord(Base):

    __tablename__ = "cost_records"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    service = Column(
        String,
        nullable=False
    )

    cost = Column(
        Float,
        nullable=False
    )

    currency = Column(
        String,
        default="USD"
    )

    recorded_at = Column(
        DateTime,
        default=datetime.utcnow
    )