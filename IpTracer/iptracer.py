import requests
import json

class IpTracer():
	"""HELPS IN GETTING INFORMATION OF A IP ADDRESS OR DOMAIN NAME"""
	def __init__(self):
		self.get_domain()
		self.make_full_url()
		self.get_data()
		self.present_data()

	def get_domain(self):
		self.ip = input("[+] Enter the IP ADDRESS/DOMAIN NAME('e.g google.com') :")
		return self.ip

	def make_full_url(self):
		self.url = "http://ip-api.com/json/"+self.ip

	def get_data(self):
		self.response = requests.get(self.url)
		self.data = json.loads(self.response.content)
	
	def present_data(self):
		print("")
		print("\t[+] IP        \t\t", self.data["query"])
		print("\t[+] CITY      \t\t", self.data["city"])
		print("\t[+] ISP       \t\t", self.data["isp"])
		print("\t[+] COUNTRY   \t\t", self.data["country"])
		print("\t[+] REGION    \t\t", self.data["regionName"])
		print("\t[+] TIME      \t\t", self.data["timezone"])
		print("\t[+] ZIP       \t\t", self.data["zip"])
		print("\t[+] LATITUDE  \t\t", self.data["lat"])
		print("\t[+] LONGITUDE \t\t", self.data["lon"])

if __name__ == '__main__':
	try:
		T = IpTracer()
	except:
		print("\n[-] Please enter a vailid IP ADDRESS.\n")
