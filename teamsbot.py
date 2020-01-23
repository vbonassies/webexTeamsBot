import requests
import sys
import json
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
from difflib import SequenceMatcher

with open("data.json", "r") as f:
    my_dict = json.load(f)

teams_bot_email = my_dict["teams_bot_email"]
teams_bot_token = my_dict["teams_bot_token"]
teams_bot_url = my_dict["teams_bot_url"]
teams_bot_name = my_dict["teams_bot_name"]
api_room_info_url = "https://api.ciscospark.com/v1/rooms"
api_message_room_url = "https://api.ciscospark.com/v1/messages"

httpHeaders = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + teams_bot_token
}

queryParams = {
    "sortBy": "lastactivity",
    "max": "2"
}

if not teams_bot_email or not teams_bot_token or not teams_bot_url or not teams_bot_name:
    print("teamsbot.py - Missing Bot Variable.")
    if not teams_bot_email:
        print("TEAMS_BOT_EMAIL")
    if not teams_bot_token:
        print("TEAMS_BOT_TOKEN")
    if not teams_bot_url:
        print("TEAMS_BOT_URL")
    if not teams_bot_name:
        print("TEAMS_BOT_APP_NAME")
    sys.exit()

bot = TeamsBot(
    teams_bot_name,
    teams_bot_token=teams_bot_token,
    teams_bot_url=teams_bot_url,
    teams_bot_email=teams_bot_email,
    debug=True,
    webhook_resource_event=[{"resource": "messages",
                             "event": "created"},
                            {"resource": "attachmentActions",
                             "event": "created"}]
)


def close_enough(str1, str2):
    r = SequenceMatcher(a=str1, b=str2)
    if r.ratio() > 0.85:
        return True


def greeting(incoming_msg):
    print(incoming_msg.roomId)
    sender = bot.teams.people.get(incoming_msg.personId)
    response = Response()

    if close_enough(incoming_msg.text.lower(), "what is the answer to the big question"):
        response.markdown = "42 obviously! "
        response.markdown += "<br/>So long and thank you for all the fish!"
        return response
    elif close_enough(incoming_msg.text.lower(), "how are you"):
        response.markdown = "I'm fine thank you, I hope you are having a wonderful day! "
        response.markdown += "<br/>See what I can do by asking for **/help**."
        return response
    elif close_enough(incoming_msg.text.lower(), "by which laws do you exist"):
        response.markdown = "The three laws of robotics guide my actions: "
        response.markdown += "<br/> - A robot may not injure a human being or," \
                             " through inaction, allow a human being to come to harm."
        response.markdown += "<br/> - A robot must obey the orders given it by human beings" \
                             " except where such orders would conflict with the First Law."
        response.markdown += "<br/> - A robot must protect its own existence as long as such" \
                             " protection does not conflict with the First or Second Laws."
        return response
    else:
        response.markdown = "Hello {}, I'm a chat bot. ".format(sender.displayName)
        response.markdown += "<br/>See what I can do by asking for **/help**."
        return response


def do_something(incoming_msg):
    return "I did what u said - {}".format(incoming_msg.text)


def questions(incoming_msg):
    response = "I can answer a few questions: "
    response += "<br/> - How are you?"
    response += "<br/> - What is the answer to the big question?"
    response += "<br/> - By which laws do you exist?"
    return response


def message_room(incoming_msg):
    if incoming_msg.text == "/messageroom":
        return "You need to add an email after the command, Ex: **/messageroom bob@bob.com****"
    to_person_email = incoming_msg.text.split("/messageroom", 1)[1]
    body = {
        "toPersonEmail": to_person_email,
        "text": "Hello, " + incoming_msg.personEmail + " send his regards"
    }
    response = requests.post(url=api_message_room_url, json=body, headers=httpHeaders)
    return "Message sent"


def send_request(incoming_msg):
    if incoming_msg.text == "/sendrequest":
        return "You need to add an email after the command, Ex: **/sendrequest bob@bob.com****"
    to_person_email = incoming_msg.text.split("/sendrequest", 1)[1]
    body = {
        "toPersonEmail": to_person_email,
        "text": incoming_msg.personEmail + " want to ask you something"
    }
    response = requests.post(url=api_message_room_url, json=body, headers=httpHeaders)
    json_data = json.loads(response.text)
    yes_no(json_data, incoming_msg.personEmail, to_person_email)
    return "request sent"


def yes_no(json_data, sender_email, receiver_email):
    attachment = '''
        {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
              "type": "AdaptiveCard",
              "version": "1.0",
              "body": [
                {
                  "type": "TextBlock",
                  "text": "Yes or No"
                },
                {
                  "type": "Input.ChoiceSet",
                  "id": "choice",
                  "style": "compact",
                  "isMultiSelect": false,
                  "value": "1",
                  "choices": [
                    {
                      "title": "Yes",
                      "value": "Yes"
                    },
                    {
                      "title": "No",
                      "value": "No"
                    }
                  ]
                }
              ],
              "actions": [
                {
                  "type": "Action.Submit",
                  "title": "OK",
                  "data": {
                    "sender": "'''+sender_email+'''",
                    "receiver": "'''+receiver_email+'''"
                  }
                }
              ]
            }
        }
        '''
    backupmessage = "This and example of a yes no."

    c = create_message_with_attachment(json_data["roomId"],
                                       msgtxt=backupmessage,
                                       attachment=json.loads(attachment))
    print(c)
    return ""


def search_room(incoming_msg):
    response = requests.get(url=api_room_info_url, headers=httpHeaders, params=queryParams)
    return "Here are the rooms info you requested: " + response.text


def quickmaths(incoming_msg):
    if incoming_msg.text == "/quickmaths":
        return "You need to add an operation after the command, Ex: **/quickmaths 1+1**"
    return str(eval(incoming_msg.text.split("/quickmaths", 1)[1]))


def show_card(incoming_msg):
    attachment = '''
    {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [{
                "type": "Container",
                "items": [{
                    "type": "TextBlock",
                    "text": "This is a sample of the adaptive card system."
                }]
            }],
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "Create",
                    "data": "add",
                    "style": "positive",
                    "id": "button1"
                },
                {
                    "type": "Action.Submit",
                    "title": "Delete",
                    "data": "remove",
                    "style": "destructive",
                    "id": "button2"
                },
                {
                    "type": "Action.ShowCard",
                    "title": "Set On-Call duty date",
                    "card": {
                        "type": "AdaptiveCard",
                        "body": [
                            {
                                "type": "Input.Date",
                                "id": "onCallDutyDate"
                            },
                            {
                                "type": "Input.Text",
                                "id": "commentOnCallDuty",
                                "placeholder": "Add a comment",
                                "isMultiline": true
                            }
                        ],
                        "actions": [
                            {
                                "type": "Action.Submit",
                                "title": "OK"
                            }
                        ],
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
                    }                
                },
                {
                    "type": "Action.ShowCard",
                    "title": "Comment",
                    "card": {
                        "type": "AdaptiveCard",
                        "body": [
                            {
                                "type": "Input.Text",
                                "id": "comment",
                                "isMultipleline": true,
                                "placeholder": "Enter your comment"
                            }
                        ],
                        "actions": [
                            {
                                "type": "Action.Submit",
                                "title": "OK"
                            }
                        ]
                    }
                }
            ],
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.0"
        }
    }
    '''
    backupmessage = "This is an example using Adaptive Cards."

    c = create_message_with_attachment(incoming_msg.roomId,
                                       msgtxt=backupmessage,
                                       attachment=json.loads(attachment))
    print(c)
    return ""


def show_list_card(incoming_msg):
    attachment = '''
    {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
          "type": "AdaptiveCard",
          "version": "1.0",
          "body": [
            {
              "type": "TextBlock",
              "text": "Pick the priority"
            },
            {
              "type": "Input.ChoiceSet",
              "id": "priority",
              "style": "compact",
              "isMultiSelect": false,
              "value": "1",
              "choices": [
                {
                  "title": "Low",
                  "value": "1"
                },
                {
                  "title": "Medium",
                  "value": "2"
                },
                {
                  "title": "High",
                  "value": "3"
                }
              ]
            }
          ],
          "actions": [
            {
              "type": "Action.Submit",
              "title": "OK"
            }
          ]
        }
    }
    '''
    backupmessage = "This is an example using Adaptive Cards and InputChoice."

    c = create_message_with_attachment(incoming_msg.roomId,
                                       msgtxt=backupmessage,
                                       attachment=json.loads(attachment))
    print(c)
    return ""


def send_response(sender_email, receiver_email, response):
    body = {
        "toPersonEmail": sender_email,
        "text": "Hello, " + receiver_email + " as responded to you request and said: " + response
    }
    response = requests.post(url=api_message_room_url, json=body, headers=httpHeaders)
    return "Response sent"


def handle_cards(api, incoming_msg):
    """
    :param api:
    :param incoming_msg:
    :return:
    """
    m = get_attachment_actions(incoming_msg["data"]["id"])
    send_response(m["inputs"]["sender"], m["inputs"]["receiver"], m["inputs"]["choice"])
    return "card action was : {}".format(m["inputs"]["choice"])


def create_message_with_attachment(rid, msgtxt, attachment):
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'authorization': 'Bearer ' + teams_bot_token
    }

    url = 'https://api.ciscospark.com/v1/messages'
    data = {"roomId": rid, "attachments": [attachment], "markdown": msgtxt}
    response = requests.post(url, json=data, headers=headers)
    return response.json()


def get_attachment_actions(attachmentid):
    headers = {
        'content-type': 'application/json; charset=utf-8',
        'authorization': 'Bearer ' + teams_bot_token
    }

    url = 'https://api.ciscospark.com/v1/attachment/actions/' + attachmentid
    response = requests.get(url, headers=headers)
    #print(response.json())
    return response.json()


def ret_message(incoming_msg):
    """
    :param incoming_msg:
    :return:
    """
    response = Response()
    response.text = "Here's a fun little meme."

    u = "https://sayingimages.com/wp-content/uploads/"
    u = u + "aaaaaalll-righty-then-alrighty-meme.jpg"
    response.files = u
    return response


def current_time(incoming_msg):
    """
    :param incoming_msg:
    :return:
    """
    timezone = bot.extract_message("/time", incoming_msg.text).strip()

    u = "http://worldclockapi.com/api/json/{timezone}/now".format(
        timezone=timezone
    )
    r = requests.get(u).json()

    if r["serviceResponse"]:
        return "**Error**: " + r["serviceResponse"]

    returned_data = r["currentDateTime"].split("T")
    cur_date = returned_data[0]
    cur_time = returned_data[1][:5]
    timezone_name = r["timeZoneName"]

    reply = "In {TZ} it is currently {TIME} on {DATE}.".format(
        TZ=timezone_name, TIME=cur_time, DATE=cur_date
    )
    return reply


current_time_help = "Look up the current time for a given timezone. "
current_time_help += "_Example: **/time GMT**_"

bot.set_greeting(greeting)

bot.add_command('attachmentActions', '*', handle_cards)
bot.add_command("/showcard", "Show an adaptative card", show_card)
bot.add_command("/showlistcard", "Show an adaptative card with input_choice", show_list_card)
bot.add_command("/dosomething", "Help for do something", do_something)
bot.add_command("/demo", "Sample that creates a Team message to be returned.", ret_message)
bot.add_command("/quickmaths", "Do some quick maths. Example: **/quickmaths 1+1**", quickmaths)
bot.add_command("/time", current_time_help, current_time)
bot.add_command("/questions", "List of the questions I can answer", questions)
bot.add_command("/messageroom",
                "Send your regards to a given email, Example: **/messageroom bob@bob.com**",
                message_room)
bot.add_command("/searchroom", "Search for the two most recent active room", search_room)
bot.add_command("/sendrequest", "Send a Yes or No card to a user, Example: **/sendrequest bob@bob.com**", send_request)

bot.remove_command("/echo")

if __name__ == "__main__":
    bot.run(host="0.0.0.0", port=80)
