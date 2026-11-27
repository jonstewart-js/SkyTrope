
import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()

HYPIXEL_API_KEY = os.getenv("HYPIXEL_API_KEY")
BASE_URL = "https://api.hypixel.net/v2"


async def get_profiles(uuid):
    headers = {
        "API-Key": HYPIXEL_API_KEY
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(
            f"{BASE_URL}/skyblock/profiles",
            params={"uuid": uuid},
            headers=headers
        ) as response:

            if response.status != 200:
                return None

            data = await response.json()

            if not data.get("success"):
                return None

            return data.get("profiles")
