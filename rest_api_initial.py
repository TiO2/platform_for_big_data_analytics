from auto_spin_up_api_calls import *


#test inputs
##cpus = 4
##disk = 50
##name = 'custom'
##ram = 8192
instance_name = 'testinstance'
instance_specification_id = 4
volume_name = 'Boot_Volume_1'
volume_size = 60
volume_type = 'spindle'

##instance_specification_id = create_new_instance_specification(cpus, disk, name, ram)
instance_id = launch_new_instance(instance_name, instance_specification_id, volume_name, volume_size, volume_type)
floating_ip_id = create_new_floating_ip()
floating_ip_addr, instance = add_floating_ip_to_instance(instance_id, floating_ip_id)

