# -*- coding: utf-8 -*-

########################################################################################
# Name    : vamsi                                                                      #
# Version : 1                                                                          #
# Date    : 2018/08/21                                                                 #
########################################################################################



print """\ 
 ▄█  ███▄▄▄▄      ▄████████     ███        ▄████████ ███▄▄▄▄    ▄████████    ▄████████       ▄█          ▄████████ ███    █▄  ███▄▄▄▄    ▄████████    ▄█    █▄    
███  ███▀▀▀██▄   ███    ███ ▀█████████▄   ███    ███ ███▀▀▀██▄ ███    ███   ███    ███      ███         ███    ███ ███    ███ ███▀▀▀██▄ ███    ███   ███    ███   
███▌ ███   ███   ███    █▀     ▀███▀▀██   ███    ███ ███   ███ ███    █▀    ███    █▀       ███         ███    ███ ███    ███ ███   ███ ███    █▀    ███    ███   
███▌ ███   ███   ███            ███   ▀   ███    ███ ███   ███ ███         ▄███▄▄▄          ███         ███    ███ ███    ███ ███   ███ ███         ▄███▄▄▄▄███▄▄ 
███▌ ███   ███ ▀███████████     ███     ▀███████████ ███   ███ ███        ▀▀███▀▀▀          ███       ▀███████████ ███    ███ ███   ███ ███        ▀▀███▀▀▀▀███▀  
███  ███   ███          ███     ███       ███    ███ ███   ███ ███    █▄    ███    █▄       ███         ███    ███ ███    ███ ███   ███ ███    █▄    ███    ███   
███  ███   ███    ▄█    ███     ███       ███    ███ ███   ███ ███    ███   ███    ███      ███▌    ▄   ███    ███ ███    ███ ███   ███ ███    ███   ███    ███   
█▀    ▀█   █▀   ▄████████▀     ▄████▀     ███    █▀   ▀█   █▀  ████████▀    ██████████      █████▄▄██   ███    █▀  ████████▀   ▀█   █▀  ████████▀    ███    █▀    
                                                                                            ▀                                                                     
"""

print" "
print" "
print" "
print" "
   

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
auth = v3.Password(auth_url="http://192.168.136.133:5000/v3", username="admin",password="password", project_name="admin",user_domain_id="default", project_domain_id="default")
sess = session.Session(auth=auth)
keystone = client.Client(session=sess)

#intially know list of projects available
for i in keystone.projects.list():
	print i

####create new project name called "first_project"
project_name=raw_input("Wnat to create project name? if yes please enter project name...")

project = keystone.projects.create(name=project_name, description="My new Project!", domain="default", enabled=True)



#Note: for adding user accout there is required reconfig Keystone first
#user_role = keystone.roles.create("user")
#admin_role = keystone.roles.create("admin")

#admin_user = keystone.users.create(name="BTH",
#                password="asdfghjkl",
#                email="karlskrona@bth.se", project_id=project.id)
#keystone.roles.add_user_role(admin_user, admin_role, project_name)



####initialize novaclient
from novaclient import client
nova = client.Client("2.1", session=sess)

###### Allocate Floating IP to project######
#We need to know available floating IP pools

nova.floating_ip_pools.list()
#[<FloatingIPPool: name=public>]

if len(nova.floating_ip_pools.list()) >1:	
	loop=1
	ip=nova.floating_ip_pools.list()
	for i in ip:
	    print str(loop) +". " + i[8:-1]
	    loop=loop+1
	image_number=int(raw_input("enter the Ip pool number"))
	#print image_number
	image= ip[image_number-1]
	s=image[8:-1]
	print" "
	print "you are selected :  " + s
	floating_ip = nova.floating_ips.create(ip[image_number-1].name)
else:
	floating_ip = nova.floating_ips.create(nova.floating_ip_pools.list()[0].name)

	
print "you have allacated IP address is  : " + floating_ip.ip 
print ""
print "####################:   Images list   :####################"
array=nova.images.list()
#[<Image: cirros-0.3.4-x86_64-uec>, <Image: cirros-0.3.4-x86_64-uec-ramdisk>, <Image: cirros-0.3.4-x86_64-uec-kernel>]

loop=1
for i in array:
    print str(loop) +". " + i[8:-1]
    loop=loop+1
image_number=int(raw_input("enter the image number"))
#print image_number
image= array[image_number-1]
s=image[8:-1]
print" "
print "you are selected :  " + s
image = nova.images.find(name=s)

print" "
print" "
print "####################:   Flavors list   :####################"
#nova.flavors.list()
Flavors=nova.flavors.list()
#[<Flavor: m1.tiny>, <Flavor: m1.small>, <Flavor: m1.medium>, <Flavor: m1.large>, <Flavor: m1.nano>, <Flavor: m1.xlarge>, <Flavor: m1.micro>]

loop=1
for i in Flavors:
    print str(loop) +". " + i[8:-1]
    loop=loop+1
image_number=int(raw_input("enter the image number"))
#print image_number
image= Flavors[image_number-1]
s=image[8:-1]
print" "
print "you are selected :  " + s
flavor = nova.flavors.find(name=s)

print" "
print" "
print "####################:   Networks list   :####################"
#nova.networks.list()
networks=nova.networks.list()
#[<Network: public>, <Network: private>]
loop=1
for i in networks:
    print str(loop) +". " + i[10:-1]
    loop=loop+1
image_number=int(raw_input("enter the image number"))
#print image_number
image= networks[image_number-1]
s=image[10:-1]
print" "
print "you are selected :  " + s

network = nova.networks.find(label=s)


server_name=raw_input("enter server name")
#With all parameters defined, now is possible to launch a new instance:
server = nova.servers.create(name = server_name, 
                                 image = image.id, 
                                 flavor = flavor.id, 
                                 nics = [{'net-id':network.id}])




#After a few seconds the instance is active

server = nova.servers.find(id=server.id)

print "Status   :" server.status
print "address  :"server.addresses

#Floting IP associated with server
instance = nova.servers.find(name=server_name)
instance.add_floating_ip(floating_ip)




#####Security Group rules######

#explicitly allowed as rules in a security group.
#show available security groups available and select named default

nova.security_groups.list()
#[<SecurityGroup description=Default security group, id=f8d5441f-f63e-4c1c-8b26-26902fa4ce33, name=default, rules=[{u'from_port': None, u'group': {u'tenant_id': u'16b27f5e755f4194b1b11a35f8116156', u'name': u'default'}, u'ip_protocol': None, u'to_port': None, u'parent_group_id': u'f8d5441f-f63e-4c1c-8b26-26902fa4ce33', u'ip_range': {}, u'id': u'0932d8a9-ac0d-47a7-a72d-cb311eca45b0'}, {u'from_port': None, u'group': {u'tenant_id': u'16b27f5e755f4194b1b11a35f8116156', u'name': u'default'}, u'ip_protocol': None, u'to_port': None, u'parent_group_id': u'f8d5441f-f63e-4c1c-8b26-26902fa4ce33', u'ip_range': {}, u'id': u'20c85363-d8ec-4af9-b102-fb863fcdc4e0'}, {u'from_port': -1, u'group': {}, u'ip_protocol': u'icmp', u'to_port': -1, u'parent_group_id': u'f8d5441f-f63e-4c1c-8b26-26902fa4ce33', u'ip_range': {u'cidr': u'0.0.0.0/0'}, u'id': u'442371b7-be79-4a7e-855e-82a11ded5ee6'}], tenant_id=16b27f5e755f4194b1b11a35f8116156>]


secgroup = nova.security_groups.find(name="default")


#Add a rule to allow incoming ssh connections (22/tcp) and another to allow all incoming icmp connections:

nova.security_group_rules.create(ip_protocol="tcp", 
                                     from_port="22", 
                                     to_port="22", 
                                     cidr="0.0.0.0/0", 
                                     group_id=None)



nova.security_group_rules.create(secgroup.id, 
                                     ip_protocol="icmp", 
                                     from_port=-1, 
                                     cidr="0.0.0.0/0", 
                                     to_port=-1)
print "Execution completed!!!"
