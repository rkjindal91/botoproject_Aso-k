import boto
ec2 = boto.connect_ec2()
sgs = ec2.get_all_security_groups()
#print sgs
for sg in sgs:
    print 'Security Group name is ', sg.name, '.\n', 'It is attached to ', len(sg.instances()), ' which are as follows:-\n'
    insName = sg.instances()
    for i in range(len(insName)):
    	print insName[i]
    print '\n'    
	#conn=boto.ec2.connect_to_region
    #for sg.instances
