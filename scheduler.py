#Marisol Morales 
#CECS 326 Project 4
#Due Date: 4/20/2025

class Task:
    def __init__(self, name, priority, burst_time):
        self.name = name                    #task name (e.g., T1)
        self.priority = int(priority)       #task priority (1 to 10)
        self.burst_time = int(burst_time)   #total CPU time needed
        self.remaining_time = int(burst_time)  #time left for the task to finish

    def __repr__(self):
        return f"{self.name} (Priority: {self.priority}, Burst: {self.burst_time})"

#function to read tasks from a file (e.g., schedule.txt)
def read_tasks(file_path):
    tasks = []  #empty list to store Task objects

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():  #skip empty lines
                    #each line should look like: T1, 4, 20
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        name = parts[0].strip()
                        priority = parts[1].strip()
                        burst_time = parts[2].strip()
                        task = Task(name, priority, burst_time)
                        tasks.append(task)
                    else:
                        print(f"Skipping invalid line: {line}")
    #now lets handle the case for if the text file is not found or does not exist!
    except FileNotFoundError:
        print(f"Error: Could not find file {file_path}")

    return tasks

#function to simulate running a task on the CPU
#if time_slice is not given, the task runs until it finishes
def run(task, time_slice=None):
    if time_slice is None:
        #run the task completely 
        #this is used in FCFS and Priority
        print(f"Running task = [{task.name}] [{task.priority}] [{task.remaining_time}] for {task.remaining_time} units.")
        task.remaining_time = 0

    else:
        #run the task for one time slice 
        #this is used in Round-Robin
        
        if task.remaining_time <= time_slice:
            print(f"Running task = [{task.name}] [{task.priority}] [{task.remaining_time}] for {task.remaining_time} units.")
            task.remaining_time = 0
        else:
            print(f"Running task = [{task.name}] [{task.priority}] [{task.remaining_time}] for {time_slice} units.")
            task.remaining_time -= time_slice
