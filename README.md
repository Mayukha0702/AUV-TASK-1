# AUV-TASK-1

##Introduction

I'm **Mayukha**,first-year student in **Smart Manufacturing**. I'm not very familiar with Python, but I used this task to start learning the basics and get familiar with **ROS (Robot Operating System)**.

At first, I took some time to understand the basic code and how everything works. But after getting used to it, things became kind of  easier. I tried my best to understand and solve the questions. Due to time constraints and upcoming end-semester exams, I was able to complete **two questions** from Task 1.

## What I Learned from This Task

- How to create ROS packages and nodes  
- How publishing and subscribing work in ROS  
- How to use custom messages  
- How to simulate basic robot movement  

---

## Task 1 – Chat Between Two Users

### Task Description:
Create a ROS package that allows two people (Jolyne and Joestar) to chat with each other using the same `rosnode` and `rostopic`.

### My Approach:
- Created a ROS package for the chat system.
- Both users publish and subscribe to the same topic.
- Used `rospy` for handling both publisher and subscriber in the same node.
- Each user types a message, which is published to the topic, and receives messages published by the other user.

### What I Learned:
- Basics of publisher-subscriber communication in ROS.
- how to create nodes.
- got to know few Python commands.
- both the files were to be executed in different terminals.
- the message written in one terminal would be shown in the other terminal.

### Challenges:
- Understanding how to run both users in the same node and topic.
- Getting used to Python syntax and structure.
- faced problems in installing git as i used VMware workstation and there was no internet connection.

  
 ## Task 2 – Number Processing

### Task Description:
This task is about creating a chain of three programs (nodes) in ROS:

1. The first one sends numbers that are multiples of 2.
2. The second one takes that number, multiplies it by 10, and sends it to another topic.
3. The third one receives that new number, adds 5 to it, and prints the final result.

###My Approach:
- I made three nodes:
  - The first one keeps publishing numbers like 2, 4, 6, 8...
  - The second one notes those numbers, multiplies them by 10, and sends them to a new topic.
  - The third one notes those numbers from  new topic, adds 5 to the number, and prints it.
- I used `rospy` to create all three nodes and topics.

##What I Learned:
- How to connect multiple ROS nodes together.
- How to use data from one node in another.
- How messages are passed and changed step-by-step in ROS.

###Challenges:
- aking sure each node talks to the correct topic.
- Figuring out how to pass the numbers properly.
- the only thing i dint know was how to stop the infinitely running loop. Then i got to know using AI that ctrl C will stop the infinite loop.

  ## Task 3 – Bot Movement Simulation

### Task Description:
The task was to let the user give commands like `"forward"` or `"turn left"`, and the bot should move on a 2D plane while keeping track of its position and direction. The position data would be sent using a custom message called `bot_pose`.
###  My Status:
I couldn't complete this question, but I tried to understand the logic behind it.

###  What I Understood:
Even though I didn’t get the time to run the code, I understood what should be done in the task:
- Taking user input as movement commands
- Updating the bot's position `(x, y)` and its facing direction

  
