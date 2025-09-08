print("Scenario 1")
import time
numbers = list(range(1000000))
start_time = time.time()
value = numbers[500001]  # Direct access
end_time = time.time()
print("Value:", value)
print("Time Taken:", end_time - start_time, "seconds")

print("Scenario 2")
import time
names = ["Name" + str(i) for i in range(1000000)]
target = "Name999999"
start_time = time.time()
for name in names:
    if name == target:
        break
end_time = time.time()
print("Time Taken:", end_time - start_time, "seconds")

print("Scenario 3")
import time
import bisect
numbers = list(range(1000000))
target = 999999
start_time = time.time()
index = bisect.bisect_left(numbers, target)
end_time = time.time()
print("Index:", index)
print("Time Taken:", end_time - start_time, "seconds")

print("Scenario 4")
import time
numbers = list(range(1000))
start_time = time.time()
for a in numbers:
    for b in numbers:
        pass
end_time = time.time()
print("Time Taken:", end_time - start_time, "seconds")