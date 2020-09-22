# What all can the classroom bot do?

### What all did we plan?

When the team discussed this ideas we had lot of cool stuff in our mind that we wanted to do (we still want to do them).
But more importantly we wanted to created a complete class room environment on the slack itself.

As a student I should never feel the need to go anywhere to access any of my course resources. Just me being present in
the slack workspace of the course should give me access to all the class resources.

When talking of resources we mean things like course schedule, course assignments, course grades, course resources (video links,
paper references, zoom meeting urls etc).

## In the below sections we would like to put in very concrete points on what all we have achieved and what all we can suggest as future features



### What have we achieved in phase-1?

1. /my commands give access to all the things that matters to a student individually like his/her grades, homework groups, meeting schedule for the course etc.
    
    Supported operations with my commands as of now:
    
        a. register - register a user with slack on the workspace to the system
        b. group - list all the groups the student is part of in the course
        
2. /assignment commands enables assignment management of the class.

    Supported operations with group commands as of now:
    
        a. list - list all the assignments along with there details
        b. create - create a new assignment (only admin user can do this)
        

Refer [this](/backend-service/bot_proxy_server/docs/cmdexmple.md) for detailed commands examples.

### What next?

Broadly speaking our team would have definitely added support for grades, group management, schedule management class room resources (link to zoom meetings, google sheet for github links of all projects and things like that).

In terms of what we have already implemented we would have fine tuned all the operations in /my and /assignment command.

    1. /assignment command should support assignment updates, sending reminders for approaching deadlines
    2. /my commands should get support for my grades, schedules, deadlines, resources


### Fancy stuff possible with the classroom-bot?

    1. Classroom bot can automatically send reminders to class for approaching deadlines for
       homeworks.
       
    2. Classroom bot can automatically send reminders to groups for their tutorial sessions along
       with meeting links.
       
    3. Reminds students to attend lectures with lecture zoom link.
    
    4. Set personal reminders for individual students based on what they want to get reminded.
    

##Final comments

A lot of things the team has implemented or has proposed to implement is by keeping CSC 510 Fall 2020 course structure
in mind. But in the end this bot should be designed in a way that it can integrate with any general 
classroom environment.