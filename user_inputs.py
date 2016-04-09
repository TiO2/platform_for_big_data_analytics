#Take inputs from ser to spin up his VM
from utils import *
from rest_api_initial import *


print 'Hello ! \n'

number_of_nodes = input('Enter number of nodes in the cluster: ')
print '\n' + str(number_of_nodes) + '\n'

if (number_of_nodes > 0):

    master_spec_name = ''
    slave_spec_name = ''

    print 'Select resource specifications for your Spark Master and Slave instances (specify numbers) \n\r'
    print 'SPEC 1: m1.large\n\r'
    print 'SPEC 2: m1.medium\n\r'

    master_spec_choice = input('Enter the spec number for the master: ')
    master_spec_name = get_specification_name(master_spec_choice)
    print master_spec_name + '\n'
    

    if (number_of_nodes > 1):
        slave_spec_choice = input('Enter the spec number for the slaves: ')
        slave_spec_name = get_specification_name(slave_spec_choice)
        print slave_spec_name + '\n'        
    else: print 'no slaves to create. creating only master\n'

    print 'creating the cluster\n'
    create_cluster(number_of_nodes, master_spec_name, slave_spec_name)
    

else:
    print 'input invalid no nodes to create\n'


command = raw_input('Do you want to delete your cluster? [Y/N]: ')
delete_cluster(command)




















