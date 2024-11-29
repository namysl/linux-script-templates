import os

dir = os.fsencode("/var/ansible-dir/enamysl/docker_test/images_scan/")
no_images = []
images = []

for file in os.listdir(dir):
        concatenated = dir.decode('utf-8') + file.decode('utf-8')
        print(concatenated)
        with open (concatenated, 'r') as opened:
                lines = len(opened.readlines())
                print("number of lines:", lines, "in", file)
                if lines > 4:
                        images.append(file)
                else:
                        no_images.append(file)

images.sort()

for item in images:
        print(item.decode('utf-8').split('.')[0]) 
