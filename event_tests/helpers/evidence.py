import json
from datetime import datetime

import allure

from config.reporting import EVENT_EVIDENCE_DIR, ensure_report_dirs

_last_event_exchange = {}


def record_event_exchange(topic, produced, consumed, metadata=None, latency_seconds=None):
    _last_event_exchange.clear()
    _last_event_exchange.update(
        {
            "topic": topic,
            "produced": produced,
            "consumed": consumed,
            "delivery_metadata": metadata,
            "latency_seconds": latency_seconds,
        }
    )


def attach_last_event_evidence(test_name, status="passed"):
    if not _last_event_exchange:
        return

    ensure_report_dirs()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = test_name.replace("/", "_").replace("\\", "_")
    evidence_path = EVENT_EVIDENCE_DIR / f"{safe_name}_{status}_{timestamp}.json"

    evidence_json = json.dumps(_last_event_exchange, indent=2, ensure_ascii=False, default=str)
    evidence_path.write_text(evidence_json, encoding="utf-8")

    allure.attach(
        evidence_json,
        name=f"Kafka event exchange ({status})",
        attachment_type=allure.attachment_type.JSON,
    )
