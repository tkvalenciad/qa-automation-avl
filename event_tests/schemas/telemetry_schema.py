GPS_EVENT_SCHEMA = {
    "type": "object",
    "required": ["vehicleId", "lat", "lng", "speed"],
    "properties": {
        "vehicleId": {"type": "string", "minLength": 1},
        "lat": {"type": "number", "minimum": -90, "maximum": 90},
        "lng": {"type": "number", "minimum": -180, "maximum": 180},
        "speed": {"type": "number", "minimum": 0},
        "timestamp": {"type": "string"},
    },
    "additionalProperties": True,
}
