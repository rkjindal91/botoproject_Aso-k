import boto.ec2
import csv
from datetime import *

class Volumes:
    def __init__(self):
        ''' Volumes Constructor '''

    def list_volumes(self, conn):
        ''' List Volumes '''
        # get all volumes
        vols = conn.get_all_volumes()

        # if volumes found
        if vols:
            # loop through volumes
            for v in vols:
                print 'Volume Id:', v.id
                print 'Volume Status:', v.status
                print 'Volume Size:', v.size
                print 'Zone:', v.zone
                print 'Volume Type:', v.type
                print 'Encrypted:', v.encrypted

                # print attachment set object
                attachmentData = v.attach_data
                print 'Instance Id:', attachmentData.instance_id
                print 'Attached Time:', attachmentData.attach_time
                print 'Device:', attachmentData.device
                print '**********************************'

    def unused_volumes(self, conn):
        ''' List Volumes '''
        # get all volumes
        vols = conn.get_all_volumes()

        filename = ('UnusedVolumes'+ str(datetime.now())+ '.csv').strip()
        with open(filename, 'w') as csvfile:
            fieldnames = ['VolumeId', 'Size', 'Region',
                      'Creation Time', 'Created From']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

        # if volumes found
            if vols:
            # loop through volumes
                for v in vols:
                    attachmentData = v.attach_data
                    if (attachmentData.instance_id == None):
                        writer.writerow({'VolumeId': v.id, 'Size': v.size, 'Region': v.type, 'Creation Time': v.create_time, 'Created From': v.zone})
                        print 'Volume ', v.id, ' with a size of ', v.size, 'GB is left unattached and not in-use. The creation time is ', v.create_time
                    else:
                        print v.id, '\n', attachmentData.instance_id
