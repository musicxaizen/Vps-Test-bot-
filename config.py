import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "23855030"))
API_HASH = getenv("API_HASH", "b153175da5f13f048abbce89b49f80cc")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7901175781:AAE-vW-OBwDfE8QpQyN7YG0B1NYrKun4vB8")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://aizen-music:ITACHIBANKIA@aizenmusic.v8utn.mongodb.net/? retryWrites=true&w=maj")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 9999999999))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002018547496"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "6806897901"))
BOT_USERNAME = getenv("BOT_USERNAME", "yoruichi_musixbot")

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/musicxaizen/Vps-Test-bot-",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/soul_x_network")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/soul_x_society")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID","121ed82a1ba74e2f9ecec017b5c9603d")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET","9e0a544cec74499587c3d8989819ea76")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BQFr_7YAEDaUtcrQ5wUM2G6y8KldAqFym50x8zrIhoM0q-yNT4RK6SNpMVFoNUcs50fvhX91mwtbFDbgNdzk4mAZktD6YBauzGM0cnv6rm5uq1Ua16lXQ3oy0NhwoYbyuHKT2Zt_hy0UJYri53VYbGQ2Toug_AFvRS22jktCALDEbsa1QMrkOm-8WctBaF_iOv1eu9qbH-1dpTyIkC3M5EsPQiFoIbJHKySppcEx7OlK8hHN5487ygJ1KQX4zyO7eYpC7RMghhwmEpSxeTLiQdSwONCNJ7NvXN3N8S4JfJmmZzuhu7yo1sHydKGDwmMlLob38K7m_KMUguDygxcDR-mOEus3XAAAAAHC12VnAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

AYUV = [ "<b>нєу</b> {0}, ✨\n\n๏ ᴛʜɪs ɪs {1} !\n\n➻ ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴠɪᴅᴇᴏᴄʜᴀᴛ ᴡɪᴛʜ ᴢᴇʀᴏ ʟᴀɢ ᴀɴᴅ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs..\n\n<b><u>Sᴜᴘᴘᴏʀᴛᴇᴅ Pʟᴀᴛғᴏʀᴍs :</b></u> ʏᴏᴜᴛᴜʙᴇ, sᴘᴏᴛɪғʏ, ʀᴇssᴏ, ᴀᴘᴘʟᴇ ᴍᴜsɪᴄ ᴀɴᴅ sᴏᴜɴᴅᴄʟᴏᴜᴅ.", ]

START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/jV2.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/4ec5ae4381dffb039b4ef.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
