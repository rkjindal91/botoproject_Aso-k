import boto.ec2
conn=boto.ec2.connect_to_region("us-east-1")
reservations = conn.get_all_instances()
print reservations
for res in reservations:
    print res, '\n'
    for inst in res.instances:
        if 'Name' in inst.tags:
            print "%s (%s) [%s]" % (inst.tags['Name'], inst.id, inst.state)
        else:
            print "%s [%s]" % (inst.id, inst.state)
