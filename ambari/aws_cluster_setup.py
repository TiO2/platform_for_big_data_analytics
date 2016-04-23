
import subprocess
import sys

def ssh_command(key,user,host,cmd):
	ssh = subprocess.Popen(['ssh -o StrictHostKeyChecking=no -i {} {}@{} "{}"'.format(key,user,host,cmd)],
	                       shell=True,
	                       stdout=subprocess.PIPE,
	                       stderr=subprocess.PIPE)
	result = ssh.stdout.readlines()
	if result == []:
	    error = ssh.stderr.readlines()
	    print >>sys.stderr, "ERROR: %s" % error
	else:
	    print result
	return result

# Get Cluster Inputs
#from cluster_inputs import *
key = "my_ncsu_aws.pem" #"seckey_team7_6761.pem"
ambari_server_public = "ec2-54-82-253-93.compute-1.amazonaws.com"
ambari_server_private = "ip-172-31-53-106.ec2.internal"

cluster_nodes_public = ["ec2-52-23-184-136.compute-1.amazonaws.com","ec2-54-174-213-202.compute-1.amazonaws.com"]
cluster_nodes_private = ["ip-172-31-7-165.ec2.internal","ip-172-31-7-166.ec2.internal"]

all_public_ips = [ambari_server_public] + cluster_nodes_public

blueprint = "blueprint.json"
hostmapping = "map.json"
user = "ec2-user"


# Prerequisites - 
# Taken 2 instances of BestBase for the cluster nodes
# Taken 1 instance of Best Ambari for The Ambari Server
# Ambari server will have the ambari-server running
# The cluster nodes will have the ambari-agent running
# Assuming hostname resolution happens!
# The WebServer will have the ability to do password less ssh using the given sec_key 





# Check Ambari Server Running in ambari_server_public
cmd = "sudo ambari-server status"
ssh_command(key,user,ambari_server_public,cmd)






# Configure Agent and restart
for i,x in enumerate(cluster_nodes_public):
	regex = "s/hostname=localhost/hostname={}/g".format(ambari_server_private)
	cmd = 'sudo sed -i "'+regex+'" /etc/ambari-agent/conf/ambari-agent.ini'
	ssh_command(key,user,cluster_nodes_public[i],cmd)

	cmd = "sudo ambari-agent restart"
	ssh_command(key,user,cluster_nodes_public[i],cmd)



#validate that all hosts are registered with Ambari server
subprocess.call("curl -u admin:admin http://"+ambari_server_public+":8080/api/v1/hosts",shell=True)


#Modify the map.json according to cluster_node_private_ips
subprocess.call('curl -H "X-Requested-By: ambari" -X POST -u admin:admin http://'+ambari_server_public+':8080/api/v1/blueprints/my_blueprint2 -d @blueprint.json',shell=True)
subprocess.call('curl -H "X-Requested-By: ambari" -X POST -u admin:admin http://'+ambari_server_public+':8080/api/v1/clusters/my_blueprint2 -d @map.json',shell=True)

#monitor progress
subprocess.call('curl -u admin:admin -i -H "X-Requested-By: ambari" -X GET http://'+ambari_server_public+':8080/api/v1/clusters/cluster_name/requests/1 | grep progress_percent',shell=True)








