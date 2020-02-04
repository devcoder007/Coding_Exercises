import os
import re

path = 'path/to/the/directory/'

files = []

for r, d, f in os.walk(path):
    for file in f:
        if '.log' in file:
            files.append(os.path.join(r, file))

ip_addr=[]
for fn in files:
    with open(fn) as f:
        for line in f:
            var = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
            if var:
                ip_addr.append(var)

print(ip_addr)


