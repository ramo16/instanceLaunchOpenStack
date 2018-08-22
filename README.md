# openstack_instance_launch
This is command line tool for instance lanch in openstack environment. This In this tool we configure openstack instance with manually similar like Open stack dash board. For user simplification in this script we need to choose only numbers for selecting parameters.

## Devstack installation

Download DevStack

		$ git clone https://git.openstack.org/openstack-dev/devstack
		$ cd devstack

The devstack repository contains a script that installs OpenStack and templates for configuration files
Create a local.conf

### Create a local.conf file with 4 passwords present at the root of the devstack

		[[local|localrc]]
		ADMIN_PASSWORD=secret
		DATABASE_PASSWORD=$ADMIN_PASSWORD
		RABBIT_PASSWORD=$ADMIN_PASSWORD
		SERVICE_PASSWORD=$ADMIN_PASSWORD

This is the minimum required config to get started with DevStack.
Start the install

		./stack.sh


## command for lanch instance:

		python launch_instance.py
