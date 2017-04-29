#!/usr/bin/Python

#Import classes from aws package
from aws import Connection
from aws import EC2Instance

#Instantiate Connection
connInst = Connection()
print(type(connInst))
print(connInst.region)

#Create an EC2 Connection
conn = connInst.ec2Connection()

#print connection
print conn
ec2 = EC2Instance()
InsID = ec2.list_instances(conn)
print InsID
for Ins in InsID:
	
	ec2 = EC2Instance()
#call start_instance with the Id of an instance
#ec2.start_instance(conn, 'i-058a5bd098a8f3158')
#ec2.stop_instance(conn, 'i-058a5bd098a8f3158')
	ec2.terminate_instance(conn, Ins)

print conn.get_all_reservations # new line added for trial purpose