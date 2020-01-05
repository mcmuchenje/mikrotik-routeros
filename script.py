#!/usr/bin/env python3

import routeros_api
HOST = 192.168.100.1

# connect to source VPN router 
	connection = routeros_api.RouterOsApiPool( HOST, username='API', password='somepassword', plaintext_login=True)
	api = connection.get_api()
  
  # Create IPSec Profile and Save to datatbase 
	list_ipsecprofile = api.get_resource('/ip/ipsec/profile')
	list_ipsecprofile.add(dh_group="modp2048", enc_algorithm="aes-128", name=("ikve2-tunnel"))

	#Configure Proposal
	list_ipsecproposal = api.get_resource('ip/ipsec/proposal')
	list_ipsecproposal.add(enc_algorithms="aes-128-cbc" name="ike2-proposal" pfs-group=modp2048)
	
	#Configure Destination peer address 
	list_ipsecpeer = api.get_resource('/ip/ipsec/peer')
	list_ipsecpeer.add(address="192.168.80.1/32" ,name='ikev2-peer' , profile=("ikve2-tunnel"))
	
	#Configure Preshared key
	list_ipsecidentity = api.get_resource('ip/ipsec/identity')
	list_ipsecpeer.add(peer="ikev2-peer" secret="thisisnotasecurepsk")
	
	#Configure PHASE II polcy
	list_ipsecpolicy = ('ip/ipsec/policy')
	list_ipsecpolicy.add(src_address="10.1.202.0/24" src_port="any" dst_address="10.1.101.0/24" dst_port="any" tunnel="yes" action="encrypt" proposal="default" peer="ikve2-peer")

	#Add NAT exception
	list_ipfirewall = ('ip/firewall/nat')
	list_ipfirewall.add(chain="srcnat" action="accept"  place_before=0 src_address="10.1.202.0/24" dst_address="10.1.101.0/24")
	
	#Close connection
	connection.disconnect()
	
