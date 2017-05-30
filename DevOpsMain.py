#!/usr/bin/Python

# IMPORT classes from aws package
from aws import Connection
from aws import EC2Instance
from aws import Volumes

# INSATANTIATE Connection
connInst = Connection()

# CREATE an EC2 Connection
reg = connInst.list_regions()
print reg
for regionaws in reg:
	#rgname = reg
 	#print rgname
        # return rgname
	conn = connInst.ec2Connection(regionaws)

# PRINT connection
	print conn

# Instantiate EC2Instance for operations
# ec2 = EC2Instance()

# InsID = ec2.list_instances(conn)
# print InsID
# for Ins in InsID:
#   Ins.start()
#  print (Ins, "is starting now")
#	ec2 = EC2Instance()
# call start_instance with the Id of an instance
# ec2.start_instance(conn, Ins)
# ec2.stop_instance(conn, 'i-058a5bd098a8f3158')
# ec2.terminate_instance(conn, 'i-0322d35086f51111c')

# print conn.get_all_reservations # new line added for trial purpose
# instantiate Volumes and list volumes
volumeInst = Volumes()
volumeInst.unused_volumes(conn)
