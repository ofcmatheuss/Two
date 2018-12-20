# -*- coding: utf-8 -*-
import requests
import time
import random

def printf(*args):
	try:
		print(*args)
	except SyntaxError:
		print *args

class Bot:
	def __init__(self, token, channel_id, bot_id):
		self.token = token
		self.channel_id = channel_id
		self.bot_id = bot_id
	
	def enter_guild(self, invite):
		# POST discordapp.com/api/v6/invite/{invite}
		printf("[%d] Entrando com o convite \"%s\"" % (self.bot_id, invite))
		headers = {
			'authorization': self.token,
			'content-encoding': 'gzip',
			'content-type': 'application/json',
			'accept-encoding': 'gzip, deflate, br'
		}
		r = requests.post('https://discordapp.com/api/v6/invite/' + invite, headers=headers)
	
	def exit_guild(self, id):
		printf("[%d] Saiu de \"%s\"" % (self.bot_id, id))
		headers = {
			'authorization': self.token,
			'content-encoding': 'gzip',
			'content-type': 'application/json',
			'accept-encoding': 'gzip, deflate, br'
		}
		r = requests.delete('https://discordapp.com/api/v6/users/@me/guilds/' + id, headers=headers)
	
	def send_message(self, message):
		# POST discordapp.com/api/v6/{channel_id}/messages
		headers = {
			'authorization': self.token,
			'content-encoding': 'gzip',
			'content-type': 'application/json',
			'content-length': '{0}'.format(55 + len(message)),
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
			'accept-encoding': 'gzip, deflate, br'
		}
		data = {"content": "{0}".format(message), "nonce": '"'+str(random.randint(10000000, 0x7FFFFFFF))+'"', "tts": False}
		r = requests.post('https://discordapp.com/api/v6/channels/'+self.channel_id+'/messages', headers=headers, json=data)
		printf("[%d] Mensagem enviada \"%s\"" % (self.bot_id, message))

if __name__ == '__main__':
	#message = open('./abc.txt', 'r')
	#message = message.read()
	message = "Oi"
	target_channel = "525058610779127818"
	target_invite = "8vxKynY"
	target_server = "513740575623610371"
	count = 5000
	bot1 = Bot('NTE3ODU3MjA0NDkwMDc2MTY0.DuITvw.Rnl4lXGEum7dVpaA9cisyTD1ISE', target_channel, 1)
	bot2 = Bot('NTE3ODU5MjIxNzgyNTI4MDIz.DuIVfQ.IJ_0o7cuITlJjITu134qJDnCGmY', target_channel, 2)
	bot3 = Bot('NTE3ODY1ODMwMjMxMzEwMzM2.DuIbow.lZetxVjU28e2lutoVAzMrIGu5oI', target_channel, 3)
	bot4 = Bot('NTE3ODY2NjY1MjkyMDcwOTMz.DuIcag.F7Z43CvSwfAi1g4Q_Ebk9dtx_iU', target_channel, 4)
	bot1.enter_guild(target_invite)
	bot2.enter_guild(target_invite)
	bot3.enter_guild(target_invite)
	bot4.enter_guild(target_invite)
	for i in range(count):
		bot1.send_message(message)
		bot2.send_message(message)
		bot3.send_message(message)
		bot4.send_message(message)
	bot1.exit_guild(target_server)
	bot2.exit_guild(target_server)
	bot3.exit_guild(target_server)
	bot4.exit_guild(target_server)