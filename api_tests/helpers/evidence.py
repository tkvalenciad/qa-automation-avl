import json
from datetime import datetime

import allure

from config.reporting import API_EVIDENCE_DIR, ensure_report_dirs

_last_api_exchange = {}


def record_api_exchange(method, url, payload, response):
    body = None
    try:
        body = response.json()
    except ValueError:
        body = response.text

    _last_api_exchange.clear()
    _last_api_exchange.update(
        {
            "method": method.upper(),
            "url": url,
            "request_payload": payload,
            "status_code": response.status_code,
            "response_time_seconds": response.elapsed.total_seconds(),
            "response_headers": dict(response.headers),
            "response_body": body,
        }
    )


def attach_last_api_evidence(test_name, status="passed"):
    if not _last_api_exchange:
        return

    ensure_report_dirs()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = test_name.replace("/", "_").replace("\\", "_")
    evidence_path = API_EVIDENCE_DIR / f"{safe_name}_{status}_{timestamp}.json"

    evidence_json = json.dumps(_last_api_exchange, indent=2, ensure_ascii=False)
    evidence_path.write_text(evidence_json, encoding="utf-8")

    allure.attach(
        evidence_json,
        name=f"API exchange ({status})",
        attachment_type=allure.attachment_type.JSON,
    )

    summary = (
        f"{_last_api_exchange['method']} {_last_api_exchange['url']}\n"
        f"Status: {_last_api_exchange['status_code']}\n"
        f"Time: {_last_api_exchange['response_time_seconds']:.3f}s"
    )
    allure.attach(
        summary,
        name=f"API summary ({status})",
        attachment_type=allure.attachment_type.TEXT,
    )
