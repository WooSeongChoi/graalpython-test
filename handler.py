from __future__ import annotations
import os
from signal import SIGABRT
import threading
import logging
from datetime import timezone, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
import httpx

from config import logger_name, watchdog_url, max_chance


class HTTPStatusWatchdog:
    _instance: HTTPStatusWatchdog | None = None

    def __init__(self):
        self.scheduler: BackgroundScheduler = BackgroundScheduler(daemon=True, timezone=timezone(timedelta(hours=9)))
        self.close_event: threading.Event = threading.Event()
        self.chance: int = max_chance
        self.logger = logging.getLogger(logger_name)

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def run(self):
        self.scheduler.add_job(
            func=self.check_http_status,
            trigger="interval",
            seconds=3
        )
        self.scheduler.start()
        self.logger.info("Watchdog start.")

        self.close_event.wait()
        self.close()
        self.logger.info("Watchdog closed.")

    def check_http_status(self):
        if self.chance > 0:
            try:
                resp: httpx.Response = httpx.get(watchdog_url)
                resp.raise_for_status()
            except httpx.HTTPStatusError as exc:
                self.logger.error(f"HTTP status Bad: {exc.response.status_code}, {exc.response.reason_phrase}")
                self.chance -= 1
            except httpx.TimeoutException as exc:
                self.logger.error(f"HTTP timeout: {exc}", exc_info=exc)
                self.chance -= 1
            except httpx.HTTPError as exc:
                self.logger.error(f"Ambiguous HTTP Error: {exc}", exc_info=exc)
                self.chance -= 1
            else:
                self.logger.info(f"Success: {resp.url}, {resp.status_code}")
                self.chance = max_chance
        else:
            pid: int = os.getpid()
            os.kill(pid, SIGABRT)

    def close(self):
        self.logger.info("Watchdog is closing")

        self.scheduler.pause()
        self.scheduler.shutdown()
        self.logger.info(f"scheduler shutdown")
