import boto
ec2 = boto.connect_ec2()
sgs = ec2.get_all_security_groups()
#print sgs
for sg in sgs:
    print sg.name, '\n', len(sg.instances())
    insName = sg.instances()
    for i in range(len(insName)):
    	print insName[i]
    	conn=boto.ec2.connect_to_region
    #for sg.instances