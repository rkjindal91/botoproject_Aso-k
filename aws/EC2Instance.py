from boto import ec2
import time


class EC2Instance:
    def __init__(self):
        ''' EC2Instance Constructor '''

    def list_instances(self, conn):
        ''' List EC2 Instances '''
        # get all instance reservations associated with this AWS account
        reservations = conn.get_all_reservations()
        # loop through reservations and extract instance information
        for r in reservations:
            # get all instances from the reservation
            instances = r.instances

            # loop through instances and print instance information
            for i in instances:
                # get instance name from the tags object
                tags = i.tags
                instancename = 'Default EC2 Instance Name'

                # check for Name property in tags object
                for Name in tags:
                    instancename = tags['Name']
#                    launchlist.append(tags['Name'])

                # print instance information
                   # print 'Instance Name:', instancename, '\t Instance Id:', i.id, '\t State:', i.state
            print i.id
            return i.id
            '''for i in instances:

                print i.private_ip_address
                print i.id'''

    def start_instance(self, conn, instance_id):
        ''' Starts a stopped instance '''
        # Filter reservations for a specific instance
        reserve = conn.get_all_reservations()
        reservations = conn.get_all_reservations(
            filters={'instance-id': instance_id})
        print reserve
        print reservations
        if(reservations):
            instance = reservations[0].instances[0]
            # start the instance if it's in a stopped state
            if(instance and instance.state == 'stopped'):
                print 'Attempting to start instance ', instance_id
                instance.start()
                # wait till instance is up and running...
                while not instance.update() == 'running':
                    # sleep for 10 seconds, before checking the status again
                    time.sleep(10)
                print 'Instance ', instance_id, ' is ', instance.state, ' now!'

    def stop_instance(self, conn, instance_id):
        ''' Stops a running instance'''
        # Filter reservations for a specific instance
        reserve = conn.get_all_reservations()
        reservations = conn.get_all_reservations(
            filters={'instance-id': instance_id})
        print reserve
        if(reservations):
            instance = reservations[0].instances[0]
            print instance
            # start the instance if it's in a running state
            if(instance and instance.state == 'running'):
                print 'Attempting to stop the instance ', instance_id
                instance.stop()
                # wait till instance is completely stopped...
                while not instance.update() == 'stopped':
                    # sleep for 10 seconds, before checking the status again
                    time.sleep(10)
                print 'Instance ', instance_id, ' is now!'

    def terminate_instance(self, conn, instance_id):
        ''' Terminates the Instance '''
        reservations = conn.get_all_reservations(
            filters={'instance-id': instance_id})
        if(reservations):
            instance = reservations[0].instances[0]
            print instance
            # terminate the instance if it's present
            if(instance):
 #               print instance 'will be terminated now.'
                #conn.terminate_instances(instance_ids=[instance_id])
                instance.terminate()

                #instance.terminate(instance_id=[instance_id])
                print 'Instance ', instance_id, ' is termirnated ', instance
