#import boto ec2
from boto import ec2

class Connection():
    
    def __init__(self):
        ''' Connection Instance '''
        self.region = 'us-east-1'

    def ec2Connection(self):
        ''' Create and return an EC2 Connection '''
        conn = ec2.connect_to_region(self.region)
        return conn
