#Marisol Morales 
#CECS 326 Project 4
#Due Date: 4/20/2025

from scheduler import read_tasks, run

#define a helper function to get the priority from a task
def get_priority(task):
    return task.priority

#this function runs the tasks based on priority
def schedule_priority(tasks):
    print("Scheduling using Priority Scheduling")

    #sort tasks so the highest priority (largest number) comes first
    tasks.sort(key=get_priority, reverse=True)

    #run each task in order of sorted priority
    for task in tasks:
        run(task)


#now lets make our main function
#reads the tasks from a file and schedules them using the Priority Scheduling algorithm.
def main():
    #lets read our task from the file
    tasks = read_tasks("pri-schedule.txt") 
    #now that we have read our tasks we can schedule them using the priority scheduling algorithm
    schedule_priority(tasks) 

#this allows us to actually run our main function
main() 