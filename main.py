mport discord
from discord.ext import commands
from discord import app_commands
import time
from discord.utils import get




intents = discord.Intents.default() 
intents.message_content = True
intents.members = True


client = commands.Bot(command_prefix='ВАШ ПРЕФИКС', intents = intents, help_command=None)




@client.event

async def on_ready():
	await client.change_presence(status=discord.Status.online, activity=discord.Game('ВО ЧТО ИГРАЕТ ВАШ БОТ'))
	print("Запущено")






@client.command()
async def votekick(ctx, member: discord.Member, reason=None):
	embed = discord.Embed(
    title="Голосование за кик пользователя",
    description=f"Голосование за кик {member}",
    colour=0xF0C43F,
)
	ml = client.get_channel(1041078087464538183) #вместо айди указаного мною напишите айди канала куда вы хотите чтобы отправлялось голосование
	msg = await ml.send(embed=embed)
	await msg.add_reaction('👍')
	msgid=msg.id
	while True:
		time.sleep(0.1)
		tally_message = await ml.fetch_message(msgid)
		reaction_count = sum(reaction.count for reaction in tally_message.reactions)
		if reaction_count==4: #вместо 4 укажите колличество участников которые должны проголосовать для кика
			await member.kick(reason=reason)
			await ml.send(f"{member} кинут")
			break


		
@client.command()
async def voteban(ctx, member: discord.Member): 
	embed = discord.Embed(
    title="Голосование за бан пользователя",
    description=f"Голосование за бан {member}",
    colour=0xF0C43F,
)
	ml = client.get_channel(1041078087464538183) #вместо айди указаного мною напишите айди канала куда вы хотите чтобы отправлялось голосование
	msg = await ml.send(embed=embed)
	await msg.add_reaction('👍')
	msgid=msg.id
	while True:
		time.sleep(0.1)
		tally_message = await ml.fetch_message(msgid)
		reaction_count = sum(reaction.count for reaction in tally_message.reactions)
		if reaction_count==11: #вместо 11 укажите колличество участников которые должны проголосовать для бана
			await member.ban()
			await ml.send(f"{member} забанен")
			break







token="ВАШ ТОКЕН"
client.run(token)



