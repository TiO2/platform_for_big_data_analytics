
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
key = "seckey_team7_6761.pem"
instances = [("vm1","10.23.2.38"),("vm2","10.23.2.222"),("vm3","10.23.2.183")]
blueprint = "blueprint.json"
hostmapping = "map.json"
user = "cloud-user"


# Prerequisites - 
# Taken 2 instances of BestBase for the cluster nodes
# Taken 1 instance of Best Ambari for The Ambari Server
# Ambari server will have the ambari-server running
# The cluster nodes will have the ambari-agent running
# Assuming hostname resolution happens!
# The WebServer will have the ability to do password less ssh using the given sec_key 



# Hostname Resolution
# For all instance started
# In /etc/hosts append the following
# instance_name instance_floating_ip
# instance_name.transcirrus-1.oscar.priv instance_floating_ip

for vm in instances:
	for hn,ip in instances:
		cmd = 'echo {} | sudo tee -a /etc/hosts'.format("")
		ssh_command(key,user,vm[1],cmd)

	 	cmd = 'echo {} {} | sudo tee -a /etc/hosts'.format(ip,hn)
	 	ssh_command(key,user,vm[1],cmd)

	 	cmd = 'echo {} {} | sudo tee -a /etc/hosts'.format(ip,hn+".transcirrus-1.oscar.priv")
		ssh_command(key,user,vm[1],cmd)



# Restart Ambari Ambari Server
cmd = "sudo service ambari-server restart"
ssh_command(key,user,instances[0][1],cmd)



# Configure Agent and restart
for hn,ip in instances[1:]:
	regex = "s/hostname=localhost/hostname={}/g".format(instances[0][1])

	print ip
	cmd = 'sudo sed -i "'+regex+'" /etc/ambari-agent/conf/ambari-agent.ini'
	print cmd
	ssh_command(key,user,ip,cmd)

	cmd = "sudo ambari-agent restart"
	print cmd
	ssh_command(key,user,ip,cmd)



#validate that all hosts are registered with Ambari server
subprocess.call("curl -u admin:admin http://"+instances[0][1]+":8080/api/v1/hosts",shell=True)


#Modify the map.json according to cluster_node_private_ips
subprocess.call('curl -H "X-Requested-By: ambari" -X POST -u admin:admin http://'+instances[0][1]+':8080/api/v1/blueprints/my_blueprint2 -d @blueprint.json',shell=True)
subprocess.call('curl -H "X-Requested-By: ambari" -X POST -u admin:admin http://'+instances[0][1]+':8080/api/v1/clusters/my_blueprint2 -d @map.json',shell=True)

#monitor progress
subprocess.call('curl -u admin:admin -i -H "X-Requested-By: ambari" -X GET http://'+instances[0][1]+':8080/api/v1/clusters/cluster_name/requests/1 | grep progress_percent',shell=True)








