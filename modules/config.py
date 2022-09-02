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
STRING_SESSION = getenv("BQAftuI9FZWOFvsrO_NPyEQy9cJpt_JVlo_WV44B2iOpiHzIZ87TTEQNdqoW2mCCZMchU77q5ppBf3sa37-ReeF1Hix6siFFpZmjdK5obOq-BTZmuSKVO-2NZw-L1nAP4vHsjsY98KZg12K8oU_8F6VlCrXPiVqUhbjIpxd-6VA6cbaAp74mPoHeVnbgwbjKm_DnK0wTOok8XjpEvwNHVm-AD_YOei1yeMRB5iqIRmpAIIbCa6R_KgZF33dVGNrdLnWPAfM1vZkKK30dqCXNbL8dRchT4dyS34X4l9HIi6xMnAbtmwXIFaEgaIv92rXOmq00_E2lrnf-JfEjBN58DSV8AAAAAVThuv0A")
OWNER_USERNAME = getenv("SLDOOZY")
SUPPORT_GROUP = getenv("anymusicvctg")
SUPPORT_CHANNEL = getenv("any24e")

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5789184850").split()))
aiohttpsession = aiohttp.ClientSession()
