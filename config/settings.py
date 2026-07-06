import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

APP_PATH = BASE_DIR / "app" / "Android-MyDemoApp.apk"
APPIUM_SERVER = os.getenv("APPIUM_SERVER", "http://127.0.0.1:4723")

PLATFORM_NAME = "Android"
AUTOMATION_NAME = "UiAutomator2"
DEVICE_NAME = os.getenv("DEVICE_NAME", "Samsung S25")
UDID = os.getenv("ANDROID_UDID", "RFCY510RLSL")

APP_PACKAGE = "com.saucelabs.mydemoapp.rn"
APP_ACTIVITY = "com.saucelabs.mydemoapp.rn.MainActivity"

VALID_USERNAME = "bob@example.com"
VALID_PASSWORD = "10203040"
INVALID_USERNAME = "invalid@test.com"
INVALID_PASSWORD = "wrongpassword"
