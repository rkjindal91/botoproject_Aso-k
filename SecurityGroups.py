import sys
import boto.ec2
sgname=sys.argv[1]
sgid=sys.argv[2]

conn = boto.ec2.connect_to_region("ap-south-1")
groups = conn.get_all_security_groups()
print groups
for group in groups:
	if group.name == sgname:
        print group.name
        print group.id
        rules = group.rules
        for rule in range(len(rules)):
        	if '0.0.0.0/0' in str(rules[rule].grants):
            	print rules[rule].ip_protocol, rule.from_port, rule.to_port, rule.grants
    elif group.id == sgid:
        print group.name
        print group.id
        for rule in group.rules:
            print rule.ip_protocol, rule.from_port, rule.to_port, rule.grants