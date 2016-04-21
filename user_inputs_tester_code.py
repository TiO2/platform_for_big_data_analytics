#Take inputs from ser to spin up his VM
from utils import *
from server_backend_functions import *


print 'Hello ! \n'

number_of_nodes = input('Enter number of nodes in the cluster: ')
print '\n' + str(number_of_nodes) + '\n'

if (number_of_nodes > 0):

    spec_name = ''

    print 'Select resource specifications for your Spark cluster(specify numbers) \n\r'
    print 'SPEC 1: m1.large\n\r'
    print 'SPEC 2: m1.medium\n\r'

    spec_choice = input('Enter the spec number: ')
    spec_name = get_specification_name(spec_choice)
    print spec_name + '\n'

    print 'creating the cluster\n'
    if (spec_name is not ''):
        create_status = create_cluster(number_of_nodes, spec_name)

    if (create_status == False):
        print 'Sorry ! We could not create your cluster at this time\n'
        cleanup_status = perform_cluster_cleanup(True, live_inst_list, live_floating_ip_id_list, live_floating_ip_list)

    else:
        get_private_ips(live_inst_list)        

else:
    print 'input invalid no nodes to create\n'






















