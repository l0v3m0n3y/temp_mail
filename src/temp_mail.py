import requests
class Client():
	def __init__(self):
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		self.api="https://api.internal.temp-mail.io/api/v3"
		self.token=None
	def new_email(self):
		data=requests.post(f"{self.api}/email/new",headers=self.headers).json()
		self.token=data["token"]
		return data
	def remove_email(self,email):
		return requests.delete(f"{self.api}/email/{email}",headers=self.headers,json={"token":self.token}).text
	def messages_email(self,email):
		return requests.get(f"{self.api}/email/{email}/messages",headers=self.headers).json()
