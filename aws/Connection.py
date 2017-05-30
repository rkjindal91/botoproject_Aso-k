# import boto ec2
from boto import ec2
import boto.ec2

class Connection():

    def __init__(self):
        ''' Connection Instance '''
        self.region = 'us-east-1'

    def list_regions(self):
        ''' List Regions of AWS '''
        regionsaws = boto.ec2.regions()
        for regionaws in regionsaws:
            rgname = regionsaws.name
         #   return rgname
            return rgname

    def ec2Connection(self, rgname):
        ''' Create and return an EC2 Connection '''
        conn = ec2.connect_to_region(rgname)
        return conn
