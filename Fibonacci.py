import math
import time

print("Press Enter to Start Fibonacci sequence")
input()

a, b = 1, 1
while True:
    a, b = b, a + b

    print(a)
    time.sleep(0.1)