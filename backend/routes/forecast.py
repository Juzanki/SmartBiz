from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.env_ai import get_weather_by_location
from backend.models import Product
from datetime import datetime

router = APIRouter()

# Cities to track (can be dynamic later)
CITIES = [
    {"city": "Dar es Salaam", "lat": -6.8, "lng": 39.28},
    {"city": "Dodoma", "lat": -6.2, "lng": 35.75},
    {"city": "Moshi", "lat": -3.35, "lng": 37.33},
    {"city": "Arusha", "lat": -3.37, "lng": 36.68},
    {"city": "Mbeya", "lat": -8.9, "lng": 33.45}
]

@router.get("/forecast/zones")
def forecast_zones(db: Session = Depends(get_db)):
    now = datetime.now().strftime("%H:%M")
    result = []

    for city in CITIES:
        weather_data = get_weather_by_location(city["city"])
        weather = "sunny" if weather_data["weather"] in ["clear"] else (
            "rainy" if "rain" in weather_data["weather"] else "cloudy"
        )

        # Get sample product recommendation
        products = db.query(Product).filter(
            Product.weather_type == weather,
            Product.preferred_location.ilike(f"%{city['city']}%"),
            Product.preferred_time_start <= now,
            Product.preferred_time_end >= now
        ).limit(2).all()

        recommendation = ", ".join([p.name for p in products]) or "None"

        result.append({
            "city": city["city"],
            "lat": city["lat"],
            "lng": city["lng"],
            "weather": weather,
            "recommendation": recommendation
        })

    return result
