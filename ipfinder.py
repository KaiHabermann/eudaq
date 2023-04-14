import json
import subprocess

"""
Prints out the ssh IP for the assosciated Docker network.
This enables the local ssh connection into the container.
Thus X- forwarding is as usual and not in the wierd docker was.
Further one can now ssh from afar and forward the X-server.
"""

process = subprocess.run(["docker","inspect","EUDAQNetwork"], capture_output=True, text=True)
result = json.loads(process.stdout)

wanted_containers = ["main_container"]
container_list = list(result[0]["Containers"].values())
for container in container_list:
    if not container['Name'] in wanted_containers:
        continue
    print(f"Container: {container['Name']} Local IPv4: {container['IPv4Address']}")

print("Remote ssh connection can be established via the port 2222 and host IPv4!")