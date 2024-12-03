import os

dir = os.fsencode("/var/ansible-dir/enamysl/docker_test/images_scan/")
content = ""

for file in os.listdir(dir):
    concatenated = dir.decode('utf-8') + file.decode('utf-8')
    with open(concatenated, 'r') as opened:
        content = opened.readlines()
        if len(content) > 4:
            with open("inactive_containers.txt", "a") as output_file:
                for line in content:
                    output_file.write(line)
                output_file.write("\n\n") 
