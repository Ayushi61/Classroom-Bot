# How to add the classroom bot to your workspace?

With our current way of things our slackbot is not distributed and hence not every workspace can 
automatically search for our bot and add it to their workspace.

#### How are we operating at present?

Since the project is still in very early stages of development,
our current model demands creating a slack app per workspace
where each workspace can represent a class. After this slack app is
created we would want the admins to enter few of the credentials of the
app into our system through the admin UI to get things working.

#### How to setup up my workspace with the classroom bot?

1. Goto this [link](https://api.slack.com/).
2. On top right corner you see "Your Apps". Click that button or directly visit [here](https://api.slack.com/apps).
3. Next you must be seeing "Create New App" green button. Click that button.
4. Here you will see a pop-up which will ask you to fill in a few details 
    
    a. App Name (we would suggest you keep it classroom-bot but anything else works fine as well)
    
    b. Development Workspace (this is where you select the workspace to which you want to attach the bot to)
    
5. After the app is created you will land at the app page, which will be used to configure rest of the things. The 
    things to be configured are standard and just needs a little time and no brain.
    
    a. Click on "Slash Commands" under "Features" sections in the navigation bar on the left side of the page.
        
    1. We need to create 3 commands here.
    2. First Command (group) parameters:
        
        a. Command: /group
        
        b. Request URL: http://a1ebeaa2e28c.ngrok.io/v0.1/service/commands/
           
           Note: We used ngrok to make our server accessible to slack. So the bot-server-proxy 
           service is started locally and then ngrok is used to create a public tunnel.
           This is a little pain since every to you run ngrok you will get a new url and
           you will have to update that ngrok url here again. But if you can purchase the ngrok
           premium then you can have one link attached to your account no matter how many times you
           restart ngrok. (Reference: https://ngrok.com/)
           
        c. Short Description: Enquire about groups (this fields is for your reference and you can fill in
            anything here)
            
        d. Usage hint: help list create delete (not all of them are implemented)
        
        e. Save the Command
        
    3. Second Command (assignment) parameters:
    
        a. Command: /assignment
        
        b. Request URL: Same as above
        
        c. Short Description: Whatever you feel like. Here what I put "Enquire and management options for class assignments."
        
        d. Usage hint: get | create assignment_name HW1 due_by 2020-09-25T23:59:59 homework_url https://www.google.com
        
        e. Save the command
        
    4. Third Command (my) parameters:
    
        a. Command: /my
        
        b. Request URL: Same as above
        
        c. Short Description: Whatever you feel like. (This command basically gives a track of your self in the class. Things like your
        homework groups, your grades etc)
        
        d. Usage hint: register your_email_id | group
        
            a. /my register xyz@ncsu.edu : This would register your email id to our system and create a link 
               between slack and our system for a user.
               
            b. Once registered you can type in things like "/my group" and the bot will intelligently list your
                assignment groups and their group member details.
                
6. We're close to setting up our slack workspace to integrate with classroom bot. Hang in tight. So for the next step we will have to give permission to our slack app to have access to things like listening on slack so that the request to classroom-bot can be forwarded to our proxy-server.

    On the App Page under "Features" section click on "OAuth and Permissions". Here add the following permissions under 
    **Bot Token Scopes**
    
    ![Bot Token Scope](/backend-service/bot_proxy_server/docs/images/bot_token_scopes.png)
    
7. Here are a few things to note down to attach this app of your workspace to the bot system:

    1. Bot Token: You can find this token under "OAuth & Permissions" sections. It's named as "Bot User OAuth
     Access Token"
     
    2. Workspace ID: Goto your slack workspace
        
        Note down the URL in the address bar of your browser:
        
           The URL should look something like this: https://app.slack.com/client/T01A2LS1RLJ/D019VUPB56J
           In the above URL T01A2LS1RLJ is your workspace id. Note down that as well.
           
    3. Admin Slack User ID: A slack workspace can have one admin who has the rights to create assignments,
        groups etc using the slack bot. Note down that ID as well.
        
        How to find this ID?
        
        Go to the slack profile of that user (admin user). The URL should look something like this:
            
            https://app.slack.com/client/T01A2LS1RLJ/C01A2LS2474/user_profile/U01AVLFSQE5
            Here : U01AVLFSQE5 is the admin user id (if you are looking at admin's profile on that
            workspace).
            
            Remember to look at the profile in the workspace to which you want the bot to be attached.
            Same user will have different slack user id in another workspace.
            
8. Awesome, you have everything now to connect your app to your workspace via classroom bot. Go to admin UI and put in the 
    three things noted in step 7.
    
9. Just last thing:   In your app home page under "Settings" click "Install App". Here if you haven't installed
this app on to your workspace before you should see an option for "Install App" otherwise you should see
"Reinstall App". Do "Reinstall App" everytime you add a new permission or change the request url in command configuration.


**It's not rare that things don't work after following all the steps. Feel free to reach out to the author @ (atrived@ncsu.edu)**
