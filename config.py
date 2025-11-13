from os import getenv
from dotenv import load_dotenv

load_dotenv()

TOKEN = getenv("BOT_TOKEN")

ALLOWED_USER_IDS_STR = getenv("ALLOWED_USER_IDS")
ALLOWED_USER_IDS = (
    [int(allowed_user_id) for allowed_user_id in ALLOWED_USER_IDS_STR.split(",")]
    if ALLOWED_USER_IDS_STR
    else []
)
