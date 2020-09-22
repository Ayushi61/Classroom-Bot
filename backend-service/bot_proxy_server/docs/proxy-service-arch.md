# Proxy service code architecture and flow


At present the bot can fulfill student request coming through slash commands only.

![Request Flow](/backend-service/bot_proxy_server/docs/images/proxy-server-request-handling.jpg)

Below is the flow of a request from slack coming to us and the system coming up with a response for the
request. The flow represents both logical request-response flow along with code flow. The code is 
structured exactly as is represented in the above diagram.

1. Someone in the slack types in a slash commands.
2. Slack redirects that command request to our proxy server which lands in one of the django views.
3. The django view uses dispatcher to dispatch the commands to one of the handlers.
4. Then handler validates whether the incoming request is valid. If invalid sends back suitable response.
5. If valid the handler decides then which of the endpoints of the bot-server should be called. The bot server
endpoint is called and the response is collected, transformed and send back to the slack.
