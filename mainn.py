import requests
import json
import os
def main():
    bot = discord.Client()
    client = commands.Bot(command_prefix="$", intents=discord.Intents.all())
print("Satan was activated!")
channelID = 1059191228371062884
headers = {
    "authorization":
    "MTA2MDg3MjM4ODEyNTkzNzY3NA.Gzh7Eq.Fb_fyanHd2xB9HjXK8qd3K9ANehjgerMbY6Fxo"}

file = open("text.txt", "r")
lines = file.readlines()
while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})