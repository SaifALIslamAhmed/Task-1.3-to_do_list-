# Welcome to T0-DO LIST!

Hi! I'm Saif Al-Islam and i'm gonna give u a quick brief about this TO-DO list


# Description

TO-DO LIST is a CLI python program doing functions like managing tasks.


## Features

- **Adding Tasks:** Add new items to the tracker.
- **Viewing Tasks:** Displays the list of tasks.
- **Completing Tasks:** Mark specific tasks as completed.
- **Removing Tasks:** Delete tasks from the active list.
- **Data Persistence (Bonus):** Saves data to an external file so tasks persist between sessions.


## Requirements

- **Python Version:** Python 3.x 
- **Standard Libraries:** `datetime` (Built-in, used to display the current timestamp when the application launches).


## EXPLAINING

(2-4) AFTER GREETING THE TRAINER, the first 3 lines are for importing date time library and declaring the time function and printing it

(6-16) After that, data saving error handling(exception). Using try and except functions to normally stop and generate an error message instead of program crashing. and reading saved data from out file

(19) using while loop using Boolean (true) to keep looping

(20-24) displaying the menu and request action from the user

(26-29) firs condition if user entered "1", then the system displays new message requesting the user to enter the task. then the system prints that the Task was added successfully

(31-32) the second condition, if the user entered "2", The system will display all tasks entered by the user #side note from saif (gotta to optimize it and displays every task in line). if the task pending, the system doesn't show any statue near the task. If the task done, the system does display "completed" as statue beside it

(36-40) the third condition, The system requests the index of the task has done. then the system edits the chosen list's element by adding " - Completed"

(41-44) the fourth condition, creating a variable named removedtask that store the index of the task the user wants to remove. Using pop function. After that system prints that “task indexed {removedtask} had been removed successfully...."

(45-51) the fifth and the final condition, it's about breaking the loop and terminating the program

(54) creating a ne file at the first time ever the program runned.Saving the tasks in a file name "TODOlist" with the extension "txt'

(55-57) it's about saving every task in one line and using write function


##  Bugs

 - If u entered index not exist in the list, The program will crash… It’s really easy to solve using condition statement
- Must request the name of the task or the option instead of the number


## Challenges 

- Coding: it was a long time since i coded by python since protons 2019. so i had some difficulties and some forgotten topics the Hager’s vid helped me to memorize python. i was mainly depending on **w3schools**

- Timing: I managed time to handle the code and and at the same time doing ground work like assembly some parts in R1 and R2 (7alimo & Abdelfatah) and solve their problems.


# Conclusion
At the end, thank you homies for the greet resources and task. It’s really easy despite of my delay and the bugs in the code


## References



1. https://www.w3schools.com/python/python_file_write.asp

2. https://youtu.be/kTaqR1WyT8A?si=dPeh0qiLZAIaPB-S
