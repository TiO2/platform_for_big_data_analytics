#Methods to make REST API-calls to Transcirrus Box
from constants import *
import requests
import json

##
###Create a New Instance Specification
##def create_new_instance_specification(cpus, disk, name, ram):
##
##    try: 
##
##        request_url = base_url + project_id + '/instance_specifications'
##        data = "{\"cpus\":" + str(cpus) + "," + \
##               "\"disk\":" + str(disk) + "," + \
##               "\"name\":\"" + name + "\"," + \
##               "\"ram\":" + str(ram) + "," + \
##               "\"visibility\": \"private\"}"
##
##        print data + '\n'
##        response = requests.post(request_url, headers = headers, data = data)
##        print response.text + '\n'
##        r = response.json()
##        instance_specification_id = r['instance_specification']['id']
##        return instance_specification_id
##
##    #log the errors
##    except:
##        print 'Error ! Unexpected value returned'
##        
        

#Launch a New Sandbox Instance
def launch_new_instance(instance_name, instance_specification_id, volume_name, volume_size, volume_type):

    try:
        
        request_url = base_url + project_id + '/instances'
        data = "{\"image_id\":\"" + hortonworks_image_id + "\"," + \
               "\"is_boot_from_volume\": false," + \
               "\"name\":\"" + instance_name + "\"," + \
               "\"network_name\":\"" + network_name + "\"," + \
               "\"security_group_name\":\"" + security_group_name + "\"," + \
               "\"security_key_name\":\"" + security_key_name + "\"," + \
               "\"specification_id\":\"" + str(instance_specification_id) + "\"," + \
               "\"volume_name\":\"" + volume_name + "\"," + \
               "\"volume_size\":\"" + str(volume_size) + "\"," + \
               "\"volume_type\":\"" + volume_type + "\"," + \
               "\"zone\": \"nova\" }"
        print data + '\n'
        response = requests.post(request_url, headers = headers, data = data)
        print response.text + '\n'
        r = response.json()

        #complete this later
        instance_id = r['instance']['id']
        return instance_id

    except:
        print 'Error ! Unexpected value returned'



#Create a New Floating IP
def create_new_floating_ip():

    try:
        
        request_url = base_url + 'floating_ips'
        print request_url

        #add network_id here
        data = "{\"network_id\":\"" + network_id + "\"," + \
               "\"project_id\":\"" + project_id + "\" }"
        print data + '\n'
        response = requests.post(request_url, headers = headers, data = data)
        print response.text + '\n'
        r = response.json()

        #complete this later
        floating_ip_id = r['floating_ip']['id']
        return floating_ip_id

    except:
        print 'Error ! Unexpected value returned'



#Add the floating IP to the newly created instance
def add_floating_ip_to_instance(instance_id, floating_ip_id):

    try:

        request_url = base_url + 'floating_ips/' + floating_ip_id + '/action'
        print request_url

        #add network_id here
        data = "{\"action\": \"add\"," + \
               "\"instance_id\":\"" + instance_id + "\"," + \
               "\"project_id\":\"" + project_id + "\" }"
        
        print data + '\n'
        response = requests.post(request_url, headers = headers, data = data)
        print response.text + '\n'
        r = response.json()

        #return floating ip address to calling program
        floating_ip_addr = r['add']['address']
        instance_name = r['add']['instance_name']
        return floating_ip_addr, instance_name
        

    except:
        print 'Error ! Unexpected value returned'



###Create a new spindle volume for the VM (limit to spindle for now)
##def create_new_spindle_volume(volume_name, volume_size, volume_type):
##
##    try:
##
##        if (volume_type = 'ssd'):
##            volume_id = total_ssd_volume_id
##        else:
##            if (volume_type = 'spindle'):
##            volume_id = total_spindle_volume_id
##            else:
##                print 'Error in type of volume field
##
##        request_url = base_url + project_id + '/volumes'
##
##        data = "{\"name\":\"" + volume_name + "\"," + \
##               "\"size\":" + volume_size + "," + \
##               "\"type\":\"" + volume_type + "\"," + \
##               "\"volume_id\":\"" + volume_id + "\"," + \
##               "\"zone\": \"nova\"}"
##        
##        print data + '\n'
##        response = requests.post(request_url, headers = headers, data = data)
##        print response.text + '\n'
##        r = response.json()
##        
##
##    except:
##        print 'Error ! Unexpected value returned'

