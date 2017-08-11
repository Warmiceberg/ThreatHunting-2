from ipwhois import IPWhois
from pprint import pprint
import csv
pth = raw_input("Please enter the file path: ")
with open("Whois_Output.csv","wb") as csvfile:
	writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['IP Address', 'Org Name', 'Org Country', 'Org Address', 'Description'])
	with open(pth,"r") as f:
		iplst = f.readlines()
		for ip in iplst:
			try:
				print ip.strip()	
				obj = IPWhois(ip.strip())
				r = obj.lookup_whois()
				country = r['asn_country_code']
				name = r['nets'][0]['name']
				ad = r['nets'][0]['address']
				add =  ad.rstrip('\n').split('\n')
				desc= r['nets'][0]['description']
				des =  str(desc.rstrip('\n').split('\n'))
				writer.writerow([ip, name, country, add, des])
			except:
				print "Couldn't find details for IP : "+ip
				pass
	f.close()
csvfile.close()
		
	
