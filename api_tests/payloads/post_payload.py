import uuid


def create_post_payload():
    return {
        "title": f"Telemetry event {uuid.uuid4().hex[:8]}",
        "body": "Simulated IoT ingestion payload",
        "userId": 1,
    }


UPDATE_POST_PAYLOAD = {
    "id": 1,
    "title": "Updated telemetry title",
    "body": "Updated payload body",
    "userId": 1,
}