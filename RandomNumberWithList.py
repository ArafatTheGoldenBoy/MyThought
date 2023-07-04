from random import randrange

ip = ["198.172.0.1", "198.172.0.2", "198.172.0.3", "198.172.0.4"]
lenght = len(ip)
newRandomIp = []
for i in range(lenght):
    r = randrange(len(ip))
    newRandomIp.append(ip[r])
    ip.pop(r)
print(newRandomIp)
