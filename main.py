import discord
import config
import summit
from datetime import datetime

client = discord.Client()
token = config.TOKEN
bot_id = 866789374031822910
channel_id = 866788357543952441

release_time = "00:42:57"
edition = 47
date = "28.07"
with open("participants.txt") as f:
    participants = [x.strip() for x in f.readlines()]

current_summit = summit.Summit(edition, date, participants)

print("Gonna post this message:")
print(current_summit.get_message())


def time_module():
    print("Waiting for the right time")
    while True:
        current_time = datetime.now().strftime("%H:%M:%S")  # hour %H min %M sec %S am:pm %p
        if current_time == release_time:  # enter the time you wish
            print("Time to post!")
            break


time_module()


@client.event
async def on_ready():
    brexit_summit_channel = client.get_channel(channel_id)
    await brexit_summit_channel.send(current_summit.get_message())

@client.event
async def on_message(message):
    brexit_summit_channel = client.get_channel(channel_id)
    if message.channel == brexit_summit_channel:

        if "deconfirmed" in message.content:
            previous_message = await brexit_summit_channel.history().find(lambda m: m.author.id == bot_id)
            current_summit.remove_participant(message.author.name)
            await previous_message.edit(content=current_summit.get_message())
            await brexit_summit_channel.send("Du wurdest entfernt, " + message.author.name + "!")

        elif "confirmed" in message.content:
            previous_message = await brexit_summit_channel.history().find(lambda m: m.author.id == bot_id)
            current_summit.new_participant(message.author.name)
            await previous_message.edit(content=current_summit.get_message())
            await brexit_summit_channel.send("Du bist drin, " + message.author.name + "!")

client.run(token)