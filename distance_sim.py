import random
import time
#   generate random distance around the mean given by the user


def generate(mean):
    # generating imprecision
    rand = random.randint(0, 2)

    # 0 for addition and 1 for subtraction
    op = random.randint(0, 1)
    op = int(op)

    if op == 0:
        return mean + rand
    return mean - rand


#   calculate average distance for ten counts
def distance(i):
    count = 0
    result = 0
    for j in range(10):
        count += 1
        dist = generate(i)
        result += dist
        if count == 10:
            x = result/count
            # print(x)
            return x
            result = 0
            dist = 0
            count = 0
        time.sleep(0.1)
