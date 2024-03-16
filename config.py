from logging.config import dictConfig

# logging configuration
logger_name: str = "test"
LOGGING_CONFIG: dict = {
    'version': 1,
    'formatters': {
        'basic': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'stream': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'basic'
        }
    },
    'loggers': {
        logger_name: {
            'handlers': ['stream'],
            'level': 'INFO'
        }
    }
}

dictConfig(LOGGING_CONFIG)


# http watchdog
watchdog_url: str = "https://www.google.com"
max_chance: int = 4
