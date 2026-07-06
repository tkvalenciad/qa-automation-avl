from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

REPORTS_DIR = BASE_DIR / "reports"
SCREENSHOTS_DIR = BASE_DIR / "screenshots" / "mobile"
ALLURE_RESULTS_DIR = BASE_DIR / "allure-results"
API_EVIDENCE_DIR = BASE_DIR / "reports" / "api-evidence"
EVENT_EVIDENCE_DIR = BASE_DIR / "reports" / "event-evidence"


def ensure_report_dirs():
    for directory in (
        REPORTS_DIR,
        SCREENSHOTS_DIR,
        ALLURE_RESULTS_DIR,
        API_EVIDENCE_DIR,
        EVENT_EVIDENCE_DIR,
    ):
        directory.mkdir(parents=True, exist_ok=True)
