#! /usr/bin/python
# -*- coding: utf-8 -*-

import requests,json
ip_file = raw_input("Enter the input suspicious IP file : ")
print "\n[+] Collecting data. Please wait ... "
with open(ip_file, "r") as f:
	for line in f:
		ip_in = str(line)
		resp = requests.get("https://www.threatcrowd.org/searchApi/v2/ip/report/?", {"ip": ip_in}).text
		op = json.loads(resp)
		op_code = op['response_code']
		count = 0
		if (op_code == "1"):
			print "\n[+] Searching malware behaviour for IP %s" %(ip_in)
			print "[+] Domains found are : "
			for k in op['resolutions']:
				print "[-]"+ " " +op['resolutions'][count]['domain']
				count = count+1
			print "\n[+] Threat Map shall be found here - %s" %str(op['permalink'])
f.close()
