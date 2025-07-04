import discord
from discord import app_commands
from discord.ext import commands
import aiohttp

TOKEN = "MTM5MDgzNjk5OTcxNTI5MTE0Ng.GbSFwI.Aa-zZbOpoddmExxG22XGJ4GnoPuymtgA9X7RL8"
WEBHOOK_URL = "https://roblox-discord-server.onrender.com"  # Definida no Roblox

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot online: {bot.user}')
    try:
        synced = await bot.tree.sync()
        print(f'Slash commands sincronizados: {len(synced)}')
    except Exception as e:
        print(e)

async def send_to_roblox(action, player):
    async with aiohttp.ClientSession() as session:
        await session.post(WEBHOOK_URL, json={"action": action, "player": player})

@bot.tree.command(name="ban", description="Bane um jogador do servidor Roblox")
@app_commands.describe(player="Nome do jogador")
async def ban(interaction: discord.Interaction, player: str):
    await send_to_roblox("ban", player)
    await interaction.response.send_message(f"✅ Jogador `{player}` foi banido.")

@bot.tree.command(name="unban", description="Remove o ban de um jogador")
@app_commands.describe(player="Nome do jogador")
async def unban(interaction: discord.Interaction, player: str):
    await send_to_roblox("unban", player)
    await interaction.response.send_message(f"✅ Banimento de `{player}` removido.")

@bot.tree.command(name="kick", description="Expulsa um jogador do jogo")
@app_commands.describe(player="Nome do jogador")
async def kick(interaction: discord.Interaction, player: str):
    await send_to_roblox("kick", player)
    await interaction.response.send_message(f"✅ Jogador `{player}` foi expulso.")

bot.run("MTM5MDgzNjk5OTcxNTI5MTE0Ng.GbSFwI.Aa-zZbOpoddmExxG22XGJ4GnoPuymtgA9X7RL8")
