import sys
import boto.ec2
import csv
from datetime import *
#sgname=sys.argv[1]
#sgid=sys.argv[2]

##For all regions
regions = boto.ec2.regions()
for region in regions:
    rgname = region.name
    if rgname == 'cn-north-1':
        continue
    if rgname == 'us-gov-west-1':
        continue
    conn = boto.ec2.connect_to_region(rgname)
    groups = conn.get_all_security_groups()
    #print groups[0]
    filename = ('UnristrictedAccess-'+ rgname + '-' + str(datetime.now()) + '.csv')
    with open(filename, 'a') as csvfile:
        fieldnames = ['SecurityGroup-Id', 'SecurityGroup-Name', 'Region',
                      'OpenPorts', 'VulnerableInstances', 'Created From']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for group in groups:
            vinstance = []
    #print group.name, group.id
    #if (sgname[0:3] != 'sg-') and (group.name == sgname):
            print rgname
            print group.name
            print group.id
            rules = group.rules
            instname = group.instances()
            for iname in instname:
                for i in range(len(instname)):
                    vinstance.append(instname)


            for rule in range(len(rules)):
                if '0.0.0.0/0' in str(rules[rule].grants):
                    #instname = group.instances()
                    #for iname in instname:
                    #    for i in range(len(instname)):
                    #        vinstance.append(instname)
                    print rules[rule].ip_protocol, rules[rule].from_port, rules[rule].to_port, rules[rule].grants
                    writer.writerow({'SecurityGroup-Id': group.id, 'SecurityGroup-Name': group.name,
                                    'Region': rgname,
                                    'OpenPorts': rules[rule].to_port,
                                    'VulnerableInstances': vinstance
                                    })
    csvfile.close()