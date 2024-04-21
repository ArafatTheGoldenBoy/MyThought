import time

start_time = time.monotonic()
wait_time = 1  # wait_time in seconds
intervel = 1


def timer(start_time, wait_time, intervel):
    flag = False
    current_time = time.monotonic()
    elapsed_time = current_time - start_time
    # print(start_time, current_time, elapsed_time)
    if elapsed_time >= wait_time:
        wait_time += intervel
        # print(wait_time)
        flag = True
    return flag, wait_time


while True:
    flag, wait_time = timer(start_time, wait_time, intervel)
    print(flag)
    time.sleep(0.4)
