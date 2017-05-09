from boto import ec2
import boto.ec2
import csv
from datetime import *


regions = boto.ec2.regions()
filename = ('UnusedVolumes'+ str(datetime.now())+ '.csv').strip()
with open(filename, 'a') as csvfile:
    fieldnames = ['VolumeId', 'Size', 'Region',
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
        vols = conn.get_all_volumes()
        if vols:
            for vol in vols:
                print vol.id
                attachmentData = vol.attach_data
                if (attachmentData.instance_id == None):
                    writer.writerow({'VolumeId': vol.id, 'Size': str(vol.size)+GB, 'Region': vol.zone, 'Creation Time': vol.create_time, 'Created From': vol.snapshot_id})

csvfile.close()
