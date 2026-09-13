from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.aws.cost_explorer import (
    get_current_month_cost,
    get_cost_by_service,
    get_daily_cost_history
)

from app.anomaly.detector import detect_cost_anomalies
from app.forecast.calculator import calculate_cost_forecast

from app.optimization.recommender import (
    generate_optimization_recommendations
)

from app.db.database import engine, get_db
from app.db.models import Base
from app.db.cost_repository import (
    save_service_costs,
    get_saved_costs
)


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Cloud Cost Optimizer API",
    description="AWS cloud cost monitoring and optimization platform",
    version="1.0.0"
)


# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------
# Root endpoint
# ---------------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "Cloud Cost Optimizer API is running"
    }


# ---------------------------------------------------------
# Health check
# ---------------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# ---------------------------------------------------------
# Current AWS cost
# ---------------------------------------------------------

@app.get("/api/costs/current")
def current_cost():
    return get_current_month_cost()


# ---------------------------------------------------------
# Cost by AWS service
# ---------------------------------------------------------

@app.get("/api/costs/services")
def cost_by_service():
    return get_cost_by_service()


# ---------------------------------------------------------
# Daily cost history
# ---------------------------------------------------------

@app.get("/api/costs/history")
def cost_history(days: int = 30):
    return get_daily_cost_history(days)


# ---------------------------------------------------------
# Cost anomaly detection
# ---------------------------------------------------------

@app.get("/api/anomalies")
def cost_anomalies(days: int = 30):
    return detect_cost_anomalies(days)


# ---------------------------------------------------------
# Cost forecast
# ---------------------------------------------------------

@app.get("/api/costs/forecast")
def cost_forecast():
    return calculate_cost_forecast()


# ---------------------------------------------------------
# Save AWS service costs to PostgreSQL
# ---------------------------------------------------------

@app.post("/api/costs/save")
def save_costs(db: Session = Depends(get_db)):

    services = get_cost_by_service()

    if not services:
        return {
            "status": "no_data",
            "message": "No AWS service cost data available to save."
        }

    records = save_service_costs(
        db,
        services
    )

    return {
        "status": "success",
        "message": "AWS cost data saved to PostgreSQL.",
        "records_saved": len(records)
    }


# ---------------------------------------------------------
# Get saved costs from PostgreSQL
# ---------------------------------------------------------

@app.get("/api/costs/database")
def database_costs(
    db: Session = Depends(get_db)
):

    records = get_saved_costs(db)

    return [
        {
            "id": record.id,
            "service": record.service,
            "cost": record.cost,
            "currency": record.currency,
            "recorded_at": record.recorded_at
        }
        for record in records
    ]


# ---------------------------------------------------------
# AWS Cost Optimization Recommendations
# ---------------------------------------------------------

@app.get("/api/optimization/recommendations")
def optimization_recommendations():

    return generate_optimization_recommendations()