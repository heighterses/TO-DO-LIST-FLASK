class to_do:
    task_bucket = {}

    def __init__(self, day, time, task):
        self.day = day
        self.time = time
        self.task = task

    def adding_task(self):
        self.day = input("Day :")
        self.time = float(input("Time from(1-24): "))
        self.task = input("Task: ")

    def adding_task_into_bucket(self):
        key = self.day
        value = {
            "time": self.time,
            "task": self.task
        }
        time = self.time
        to_do.task_bucket[key] = value


numb = int(input("How Much do you Have tasks in Coming Week: "))

for _ in range(numb):
    app = to_do("", 0, "")
    app.adding_task()
    app.adding_task_into_bucket()

print("")
print(f"Your Tasks : {to_do.task_bucket}")



