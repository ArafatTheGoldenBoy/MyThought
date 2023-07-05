from random import randrange

ip = ["198.172.0.1", "198.172.0.2", "198.172.0.3", "198.172.0.4"]
newRandomIp = ["0"]


def RandomNumberWithRemember(ip):
    lenght = len(ip)
    for i in range(lenght):
        r = randrange(len(ip))
        newRandomIp.append(ip[r])
        ip.pop(r)

    count = int(newRandomIp[0])
    count += 1
    # print("List: ", newRandomIp)
    if count == len(newRandomIp):
        random_num_with_remember = "list need to feed again"
    else:
        random_num_with_remember = newRandomIp[count]
        newRandomIp[0] = str(count)

    return random_num_with_remember


print(RandomNumberWithRemember(ip=ip))
print(RandomNumberWithRemember(ip=ip))
print(RandomNumberWithRemember(ip=ip))
print(RandomNumberWithRemember(ip=ip))
print(RandomNumberWithRemember(ip=ip))
print(RandomNumberWithRemember(ip=ip))
print(RandomNumberWithRemember(ip=ip))
print(RandomNumberWithRemember(ip=ip))
