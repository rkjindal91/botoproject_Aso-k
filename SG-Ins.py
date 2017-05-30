import boto3
fpointer = open("list_instance.csv", "w")
fpointer.write("Region,Instance_id,Security_id,Securitygroup_name,Tag\n")
reg = boto3.client('ec2');
region = reg.describe_regions()
for regions in region['Regions']:
regname = regions['RegionName']
connection = boto3.client('ec2',region_name=regname)
regDesc = connection.describe_instances()
for i in regDesc['Reservations']:
for tg in i['Instances']:
iid = tg['InstanceId']
helo = ""	
totalUsers = []
for tgng in tg['Tags']:
tst = tgng['Key'] + tgng['Value']
totalUsers.append(tst)
helo = helo + " Key: " + tgng['Key'] + " Value: " + tgng['Value']
for sg in tg['SecurityGroups']:
sgg = sg['GroupId']
fpointer.write(regname + "," + iid + "," + sgg + "," + sg['GroupName'] + "," + helo + "\n")
#print tagna