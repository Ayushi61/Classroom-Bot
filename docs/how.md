# How are we achieving this?

### How to interact with the bot?

We are using [slack commands](https://api.slack.com/interactivity/slash-commands)
to enable interaction with the classroom-bot. Please read the [link](https://api.slack.com/interactivity/slash-commands)
to understand slack commands.

Supported commands:

1. /assignment : This command helps with assignment management for TAs and 
assignment tracking and help for the students.

    eg: /assignment list (type this in any channel and the bot should come back with all your assignments)

2. /my : This command helps a student with his personal class management stuff. 
The user can do things like register itself to the classroom-bot so that the bot remembers the user, 
list his homework/project groups along with members info.

    eg: /my group (after the user has registered itself using **/my register**
    the bot should list the user's homework groups and their members.)

3. /group : This command helps managing groups of the class.

    eg: /group list (should list all the list the groups of the class with member details)


![The Big Picture](/docs/images/thebigpicture.jpg)


We have 3 micro-services setup to build the classroom environment.

### Components
1. Proxy Slack Service - the bot's ear and mouth
2. Core backend - the bot's brain
3. Admin UI - configure the classroom environments


#### Detailed components description

1. Proxy Slack Service<br/><br/>

   This service listens to all the events happening at the slack. A slack event can be 
   considered as things happening on a slack workspace (messages in channels, mention to the bot etc).
   <br/><br/>
   
   Our main motive of this service?<br>
   This service exists so that the system can receives all the requests users want
   to make to the **classroom-bot**. 
   <br/>Following requests are accepted by the classroom-bot at
   present.
   
   #### Assignments Requests
   1. Admin user can create assignment for the class.
   2. All the users can list the assignments with all the details like due date, resources link etc.
   
   #### Group Requests
   1. List group details the user is part of.
   
   #### User Management Requests
   Your class TA could have added you as a student to our system using the admin portal.
   But to correctly identify the identity of the student on slack (slack has it's own
   user id per user) we need a mapping to map slack user id to our system. For this reason the user 
   has to tell the class bot it's identity on slack.
   
   The way to do that is by typing this in any of the channel or a direct message to the slackbot:
   
   /my register {your_school_email_id_which_ta_would_have_used}
   For example: /my register xyz.ncsu.edu
   
   After this registration is done a whole bunch of features can be made available to the user
   by typing minimal things on slack.
   
   For example now typing the following on slack will list all your groups and your team mates: 
   
   /my group