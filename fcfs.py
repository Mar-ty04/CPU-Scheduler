#Marisol Morales 
#CECS 326 Project 4
#Due Date: 4/20/2025

from scheduler import read_tasks, run

#this function runs the tasks based on FCFS 
def schedule_fcfs(tasks):
    print("Scheduling using FCFS")
    for task in tasks:
        run(task)

#now lets make our main function
#reads the tasks from a file and schedules them using the FCFS algorithm.
def main():
    #lets read our task from the file 'schedule.txt'
    tasks = read_tasks("schedule.txt")
    #now that we have read our tasks we can schedule them using the FCFS algorithm
    schedule_fcfs(tasks) 

#this allows us to actually run our main function
main()