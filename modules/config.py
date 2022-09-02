import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("10638737"))
API_HASH = getenv("0997d79746f79b2008de01101f86e792")
BOT_TOKEN = getenv("5711353964:AAF6g13AV48vVBdOyuHmK7fh0bU3Rl3Ac38")
BOT_USERNAME = getenv("Z_eNKIBot")
BOT_NAME = getenv("ZENKI")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION")
OWNER_USERNAME = getenv("SLDOOZY")
SUPPORT_GROUP = getenv("anymusicvctg")
SUPPORT_CHANNEL = getenv("any24e")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5789184850").split()))
aiohttpsession = aiohttp.ClientSession()
