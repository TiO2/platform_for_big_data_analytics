import json

def updateJsonFile(hostmapping,cluster_nodes):
	jsonFile = open(hostmapping, "r")
	data = json.load(jsonFile)
	jsonFile.close()

	print data["host_groups"][0]["hosts"][0]["fqdn"]
	data["host_groups"][0]["hosts"][0]["fqdn"] = cluster_nodes[0][0]
	
	for i,instance in enumerate(cluster_nodes[1:]):
		data["host_groups"][1]["hosts"][i]["fqdn"] = instance[0]

	jsonFile = open("map.json", "w+")
	jsonFile.write(json.dumps(data))
	jsonFile.close()




hostmapping = "map.json"
instances = [("vm1","10.23.2.38"),("vm2","10.23.2.222"),("vm3","10.23.2.183"),("vm4","10.23.2.185")]

cluster_nodes = instances[1:]
updateJsonFile(hostmapping,cluster_nodes)

