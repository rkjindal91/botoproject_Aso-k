import sys
import boto.ec2
sgname=sys.argv[1]
#sgid=sys.argv[2]

conn = boto.ec2.connect_to_region("ap-south-1")
groups = conn.get_all_security_groups()
#print groups[0]
for group in groups:
    #print group.name, group.id
    if (sgname[0:3] != 'sg-') and (group.name == sgname):
        print group.name
        print group.id
        rules = group.rules
        for rule in range(len(rules)):
            if '0.0.0.0/0' in str(rules[rule].grants):
                print rules[rule].ip_protocol, rules[rule].from_port, rules[rule].to_port, rules[rule].grants
    elif group.id == sgname:
        print group.name
        print group.id
        rules = group.rules
        for rule in range(len(rules)):
            if '0.0.0.0/0' in str(rules[rule].grants):
                print rules[rule].ip_protocol, rules[rule].from_port, rules[rule].to_port, rules[rule].grants