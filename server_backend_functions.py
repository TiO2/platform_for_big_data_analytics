from api_calls import *

#CREATE CLUSTER
def create_cluster(number_of_nodes, spec_name):

    try:
        
        nodes = number_of_nodes

        image_id = get_image_id('CentOS')
        spec_id = get_specification_id(spec_name)
        print spec_id + '\n'

        if (nodes > 0):
            while(nodes > 0):
                vm_name = 'VM' + str(str(number_of_nodes - nodes + 1))                
                inst_status, inst_id = launch_new_instance(vm_name, image_id, spec_id)
                print 'status of ' + vm_name + ' ' + str(inst_status) + '\n'

                if (inst_status == 200):
                    live_inst_list[vm_name] = inst_id
                    fltg_ip_status, floating_ip_id = create_new_floating_ip()
                    if (fltg_ip_status == 200):
                        live_floating_ip_id_list[vm_name] = floating_ip_id
                        add_fltg_status, floating_ip_addr = add_floating_ip_to_instance(inst_id, floating_ip_id)
                        if (add_fltg_status == 200):
                            live_floating_ip_list[vm_name] = floating_ip_addr
                            nodes = nodes - 1
                        else:
                            logging.info('creating instance failed - issue - ' + vm_name + ' floating IP could not be attached')                            
                    else:
                        logging.info('creating instance failed - issue - ' + vm_name + ' floating IP could not be created')                    
                else:
                    logging.info('creating instance failed - issue - ' + vm_name + ' could not be created')

                print 'number of nodes left ' + str(nodes) + '\n'


        
        print live_inst_list 
        print live_floating_ip_list 
        print live_floating_ip_id_list

        if(nodes == 0):
            print 'All nodes created successfully'
            return True
                
    except:
        logging.debug('exception in create_cluster')
        return False



#DELETE CLUSTER
def perform_cluster_cleanup(delete_command):
    try:
        if (delete_command == True):
            if (len(live_inst_list) == 0):
                print 'Error ! incorrectly called delete on a empty cluster: instances do not exist'
            elif (len(live_inst_list) > 0):
                for key in live_inst_list.keys():
                    response_status = delete_instance(live_inst_list[key])
                    if (response_status == 200):
                        print 'deleting ' + key + '\n'
                    else:
                        print 'could not delete ' + key + '\n'
                live_inst_list.clear()

            if (len(live_floating_ip_list) == 0 or len(live_floating_ip_id_list) == 0):
                print 'Error ! incorrectly called delete on a empty cluster: floating ips do not exist'
            elif ((len(live_floating_ip_list) == len(live_floating_ip_id_list)) and len(live_floating_ip_id_list) > 0):
                for key in live_floating_ip_id_list.keys():
                    response_status = delete_unused_floating_ip(live_floating_ip_id_list[key])
                    if (response_status == 200):
                        print 'deleting ip address of ' + key + '\n'
                    else:
                        print 'could not delete ip address of ' + key + '\n'
                live_floating_ip_list.clear()
                live_floating_ip_id_list.clear()
        else:
            print 'You entered no! Could not delete the cluster'
            return

    except:
        logging.debug('Could not delete cluster')
        return False


#GET PRIVATE IPS OF VMS
def get_private_ips(running_inst_list):

    try:

        number_of_instances = len(running_inst_list)
        
        for inst_name in running_inst_list.keys():
            response_status, vm_private_ip_addr = get_instance_details(running_inst_list[inst_name])
            if (response_status == 200):
                live_private_ip_list[inst_name] = vm_private_ip_addr
                number_of_instances = number_of_instances - 1
                print 'the private ip address of ' + inst_name + ' is ' + str(vm_private_ip_addr)
            else:
                print 'could not get private ip address of ' + inst_name + '\n'

        if (number_of_instances == 0):
            print 'All private ips obtained successfully'
            print live_private_ip_list
        
        else:
            print 'Could not get private IP addresses of ' + str(number_of_instances) + ' instances'

    except:
        logging.debug('could not get private ip addresses of the VMs')
        return

                
            
        











            
            
        
    


        


        
        
        
