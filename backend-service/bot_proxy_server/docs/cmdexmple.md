# Slack Command Examples

## `/my` Commands

1. `/my register xyz@gmail.com` - register yourself to the class. Ask your TA create a student record
                                for you on the bot server before registering. Otherwise you can
                                register as many times as possible. Just keep registering till TA creates
                                your student records with us.
                                
2. `/my group` - list your homework/assignment groups. It also lists your team mates for each of the group
               the user is part of.
               
               
Future `/my` commands:

1. `/my grades` - show all the grades of the user for the course.
2. `/my schedule` - show all the schedules of the user for the course.
3. `/my resource` - show all the resources that the student has created for himself on the class workspace.

These are just suggestions, possibilities are endless.


## /assignment Commands

1. `/assignment get` - get all the assignments for the course.
2. `/assignment create assignment_name HW1 due_by 2020-09-25T23:59:59 homework_url https://www.google.com` - this command can
   only be run by the admin user of the workspace. This admin user is registered when the course
   is created from the admin UI. Other users in that workspace won't be able to run this command.
   
Future `/assignment` commands:

1. `/assignment remind` - if run by the admin the slack bot can remind all the students on slack for an
                        approaching assignment deadline
                        

These are just suggestions, possibilities are endless.

## `/group` Commands

Basically we could not integrate any group commands with the slack in phase-1 with time constraints. But here are 
some interesting suggestions.

Future /assignment commands:

1. `/group list` - list all the groups along with member details
2. `/group list group_number` - list group details for specified group number
3. `/group create group_number member1, ...., member_n` for_which_homework hw1

These are just suggesstion, you know what will I say next. **Possibilities are endless.**