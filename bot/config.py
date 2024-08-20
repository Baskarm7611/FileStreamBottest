from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 5675662))
    API_HASH = env.get("TELEGRAM_API_HASH", "0f6458b19f7574e191995c6fbacc0d5b")
    OWNER_ID = int(env.get("OWNER_ID", 967723997))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "@My2diskdlbot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "5597226448:AAELI1rCBPeK8-Ok4ta4lLtOeOgJDSHycG8")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1001691446993))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "https://2.59.156.39")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "https://hi-f2l.z5xjxd.easypanel.host/")
    PORT = int(env.get("PORT", 8080))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
