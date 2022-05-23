import time

file = open('pspL.txt', 'r')
lines = file.readlines()
for line in lines:
    print(line)
    time.sleep(1)