
import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from hypixel import get_profiles

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

class SkyblockBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


bot = SkyblockBot()


@bot.tree.command(
    name="profiles",
    description="Look up a player's SkyBlock profiles"
)
@app_commands.describe(uuid="Minecraft player UUID")
async def profiles(interaction: discord.Interaction, uuid: str):

    await interaction.response.defer()

    data = await get_profiles(uuid)

    if not data:
        await interaction.followup.send(
            "Unable to retrieve player profiles."
        )
        return

    embed = discord.Embed(
        title="SkyBlock Profiles",
        color=discord.Color.blue()
    )

    for profile in data:
        name = profile.get("cute_name", "Unknown")
        selected = profile.get("selected", False)

        embed.add_field(
            name=name,
            value=f"Selected: {'Yes' if selected else 'No'}",
            inline=True
        )

    await interaction.followup.send(embed=embed)


bot.run(TOKEN)
