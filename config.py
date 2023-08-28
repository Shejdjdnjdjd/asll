from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "2521020")
API_HASH = getenv("API_HASH", "e2818d6ffad1b544611ae87d95865a46")

BOT_TOKEN = getenv("BOT_TOKEN", "6607566914:AAEr6abpr2KbJ70UKzP6Ve4QvHQmRqW7bB8")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "271870117")

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/f8e33c73f561c073b568c.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/f8e33c73f561c073b568c.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/F6LLL")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/F6LLL")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5656828413").split()))


FAILED = "https://telegra.ph/file/f8e33c73f561c073b568c.jpg"
