from asyncio import Task

#tasks = [5, 2, 7, 1, 4, 3]
#workers = [0, 0, 0]

#Task 5:
#workers = [5, 0, 0]
#Task 2:
#workers = [5, 2, 0]
#Task 7:
#workers = [5, 2, 7]
#Task 1:
#workers = [5, 3, 7]
#Task 4:
#workers = [5, 7, 7]
#Task 3:
#workers = [8, 7, 7]

tasks = [5, 2, 7, 1, 4, 3]
workers = [0, 0, 0]

for task in tasks:
    smallest_worker = workers.index(min(workers))

    workers[smallest_worker] += task

    print(f"Worker  {smallest_worker + 1} got task {task}")
    print(f"Current workload: {workers}")

print(f"Final workloads: {workers}")