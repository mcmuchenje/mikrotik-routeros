# connect to source VPN router 
	connection = routeros_api.RouterOsApiPool( '197.211.240.228', username='API', password='x&w,-7jTE!uF>m5t', plaintext_login=True)
	api = connection.get_api()

	#Make sure function only runs once 
  
  # Create IPSec Profile and Save to datatbase 
	list_ipsecprofile = api.get_resource('/ip/ipsec/profile')
	list_ipsecprofile.add(dh_group="modp2048", enc_algorithm="aes-128", name=("ikve2-tunnel"))

	#Configure Destination peer address 
	list_ipsecpeer = api.get_resource('/ip/ipsec/peer')
	list_ipsecpeer.add(address="192.168.80.1/32" ,name='ike1-site2' , profile=("ikve2-"))
	

	connection.disconnect()
	
