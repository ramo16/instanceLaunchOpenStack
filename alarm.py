########################################################################################
# Name    : Vamsi                                                                      #
# Version : 1                                                                          #
# Date    : 2018/07/15                                                                 #
########################################################################################

######Authentication########

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
CEILOMETER_ENDPOINT="http://192.168.136.138:8777"
import keystoneclient.v3.client as k_client
keystone = k_client.Client(auth_url="http://192.168.136.138:5000/v3", username="admin",password="password", project_name="admin",user_domain_id="default", project_domain_id="default")
import ceilometerclient.v2 as c_client
auth_token = keystone.auth_token
ceilometer = c_client.Client(endpoint=CEILOMETER_ENDPOINT, token= lambda : auth_token )



#intially know list of meters available

ceilometer.meters.list()

#then create alarms each meter individually


#######set a custom alarm#########

# UPDATABLE_ATTRIBUTES = [
#	    'name',
#	    'description',
#	    'type',
#	    'state',
#	    'severity',
#	    'enabled',
#	    'alarm_actions',
#	    'ok_actions',
#	    'insufficient_data_actions',
#	    'repeat_actions',
#	    'project_id',
#	    'user_id'    ]


#if we want note meter information just add   ' alarm_action'=log::// \'




#alarm1

ceilometer.alarms.create(name='meter1',discription='fan rounds per minute',threshold=100,comparison_operator='gt',period=600,meter_name='hardware.ipmi.fan')

#alarm2

ceilometer.alarms.create(name='meter2',discription='temperature reading from sensor',threshold=70,comparison_operator='gt',period=600,meter_name='hardware.ipmi.temperature')


#alarm3

ceilometer.alarms.create(name='meter3',discription='Voltage reading from sensor',threshold=100,comparison_operator='lt',period=600,meter_name='hardware.ipmi.voltage')


#list of alarms available

ceilometer.alarms.list()


