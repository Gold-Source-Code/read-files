import time

with open('pspL.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line)
        time.sleep(1)