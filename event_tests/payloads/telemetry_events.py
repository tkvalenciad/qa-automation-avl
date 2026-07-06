import random
import uuid
from datetime import datetime, timezone


def build_gps_event(vehicle_id="VEH-99", lat=4.60, lng=-74.08, speed=65):
    return {
        "vehicleId": vehicle_id,
        "lat": lat,
        "lng": lng,
        "speed": speed,
    }


def random_gps_event(vehicle_id=None):
    return {
        "vehicleId": vehicle_id or f"VEH-{uuid.uuid4().hex[:8]}",
        "lat": round(4.60 + random.uniform(-0.05, 0.05), 6),
        "lng": round(-74.08 + random.uniform(-0.05, 0.05), 6),
        "speed": random.randint(0, 120),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
