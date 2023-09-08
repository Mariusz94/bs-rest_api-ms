import os
from dotenv import load_dotenv

load_dotenv()


"""
Plik konfiguracyjny.
"""

SERVICE_NAME = "bs_rest_api_ms"
"""Nazwa mikroserwisu."""

MS_VERSION = str(os.environ.get("MS_VERSION", "NOT AVAILABLE"))
"""Wersja mikroserwisu."""

SERVICE_PORT = int(os.environ.get("SERVICE_PORT", 5555))
"""Port, na którym dostępny jest serwis."""

LOGGING_MODE = str(os.environ.get("LOGGING_MODE", "DEBUG"))
"""Poziom logowania informacji, błędów."""