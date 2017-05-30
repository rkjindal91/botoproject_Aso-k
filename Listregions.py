import boto.ec2
regions = boto.ec2.regions()
print regions
for region in regions:
	print region
