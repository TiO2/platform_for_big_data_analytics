import auto_spin_up_api_calls


#test inputs
cpus = 4
disk = 50
name = 'custom'
ram = 8192
instance_name = 'testinstance'

instance_specification_id = create_new_instance_specification(cpus, disk, name, ram)
instance_id = launch_new_instance(instance_name, instance_id)
floating_ip_id = create_new_floating_ip()
floating_ip_addr = add_floating_ip_to_instance(instance_id, floating_ip_id)
vm_volume_id = create_new_spindle_volume(volume_name, volume_size, volume_type)
add_volume_to_vm(instance_id, vm_volume_id)



