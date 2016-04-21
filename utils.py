#This file holds the structures and methods to query user inputs and
#and respond with appropriate id's to spin up VMs

status_message_list = {'200': 'Success', '400': '400 Bad Request', '404': '404 Not Found', '500': '500 Error'}

specification_choice_list = {'1': 'm1.large', '2': 'm1.medium'}

specification_id_list = {'m1.large': '4', 'm1.medium': '3'}

image_id_list = {'CentOS_Base': 'd2d7ed2c-1372-48dc-9f5d-34a7a52dd760', 'CentOS': '3d11dc35-d683-4709-849f-7af99a74b2f0'}

live_inst_list = {}
live_floating_ip_list = {}
live_floating_ip_id_list = {}
live_private_ip_list = {}


def get_specification_id(spec_name):
    return specification_id_list[spec_name]

def get_specification_name(spec_choice):
    return specification_choice_list[str(spec_choice)]

def get_image_id(image_name):
    return image_id_list[image_name]

def get_status_message(status_code):
    return status_message_list[status_code]
    


    

    


