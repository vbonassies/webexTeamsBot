# webexTeamsBot
simple webexTeams bot

To configure your variables to link your bot to your webhook,
 create a json file name data.json for example (if you chose
 another name, change it in teamsbot.py aswell) and in it
 write as follow:
 
 {<br>
  "teams_bot_email":  "your_bot_email",<br>
  "teams_bot_token":"your_bot_access_token",<br>
  "teams_bot_url": "your_http_tunnel_you_can_use_ngrok_
  for test",<br>
  "teams_bot_name": "you_bot_name"<br>
}


To use he calendar google API, you need a json file with
your credentials, to do so, follow he step 1 on this:
https://developers.google.com/calendar/quickstart/python