from boto import ec2
import boto.ec2
import csv
from datetime import *


regions = boto.ec2.regions()
#OPEN CSV file to write to it.
filename = ('UntaggedInstances'+ str(datetime.now())+ '.csv').strip()
with open(filename, 'a') as csvfile:
    fieldnames = ['InstanceID', 'Type', 'Region',
                      'Creation Time', 'Created From']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for region in regions:
        rgname = region.name
        print rgname
        if rgname == 'cn-north-1':
            continue
        if rgname == 'us-gov-west-1':
            continue
        conn = ec2.connect_to_region(rgname)
        print conn
        reservations = conn.get_all_reservations()
        for reservation in reservations:
            print reservation
            instances = reservation.instances
            for instance in instances:
                ##START checking for tags and create them if not present.
                instancename = tags['Name']
                    if len(instancename) == 0:
                    instance.stop()   
if vols:
            for vol in vols:
                print vol.id
                attachmentData = vol.attach_data
                if (attachmentData.instance_id == None):
                    writer.writerow({'VolumeId': vol.id, 'Size': str(vol.size)+GB, 'Region': vol.zone, 'Creation Time': vol.create_time, 'Created From': vol.snapshot_id})

csvfile.close()
