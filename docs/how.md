# How are we achieving this?

### How to interact with the bot?

We are using [slack commands](https://api.slack.com/interactivity/slash-commands)
to enable interaction with the classroom-bot. Please read the [link](https://api.slack.com/interactivity/slash-commands)
to understand slack commands.

Supported commands:

Refer to this for supported commands: [Supported Commands](/backend-service/bot_proxy_server/docs/cmdexmple.md)


![The Big Picture](/docs/images/thebigpicture.jpg)


We have 3 micro-services setup to build the classroom environment.

### Components
1. Proxy Slack Service - the bot's ear and mouth
2. Core backend - the bot's brain
3. Admin UI - configure the classroom environments


#### Detailed components description

1. Proxy Slack Service<br/><br/>

   This service listens to all the events happening at the slack. A slack event can be 
   considered as things happening on a slack workspace (slash command request, messages in channels, mention to the bot etc).
   <br/><br/>
   
   Our main motive of this service?<br>
   This service exists so that the system can receives all the requests users want
   to make to the **classroom-bot**. 
   
   To request for a service from the slack bot type in one of the supported commands with correct parameters.
   The way to do that is by typing this in any of the channel or a direct message to the slackbot:
   
   Example slash command request:
   
   /my register {your_school_email_id_which_ta_would_have_used}
   For example: /my register xyz.ncsu.edu
   
2. Bot Server:

    This is the brain of the bot. The server has apis to access courses configured, assignments, students in
    particular course, assignment groups.
    
    This service essentially remembers everything you want your bot to remember and help with in your classroom.
    
    The proxy service after receiving requests from the slash and parsing it calls API end points from this service 
    to fetch appropriate data.
    
3. Admin UI

    This is where the admin of a course gets all his super power from. The admin can control things
    like creating a new course, setting up assignments, creating assignment groups, assigning grades.
    
    The admin UI also calls bot server apis.