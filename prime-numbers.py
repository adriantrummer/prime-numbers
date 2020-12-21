import time

i = 1
counter = 0
is_prime = True

while True:
    i += 1
    counter = i - 1
    is_prime = True
    while counter > 1:
        if not i % counter:
            is_prime = False
        counter -= 1
    if is_prime == True:
        print(i)
 #   time.sleep(0.1)
