def yes_no_card(sender, receiver):
    c = '''
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
                    "sender": "''' + sender + '''",
                    "receiver": "''' + receiver + '''"
                  }
                }
              ]
            }
        }
        '''
    return c


def on_call_duty_change_response_card(sender, receiver, e_id, ns_date, ne_date):
    c = '''
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
                      "id": "onCallDutyChoiceResponse",
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
                    },
                    {
                        "type": "Input.Text",
                        "id": "comment",
                        "placeholder": "Add a comment",
                        "isMultiline": true
                    }
                  ],
                  "actions": [
                    {
                      "type": "Action.Submit",
                      "title": "SEND",
                      "data": {
                        "sender": "''' + sender + '''",
                        "receiver": "''' + receiver + '''",
                        "e_id": "''' + e_id + '''",
                        "ns_date": "''' + ns_date + '''",
                        "ne_date": "''' + ne_date + '''"
                      }
                    }
                  ]
                }
            }
            '''
    return c


def on_call_duty_change_request_card(events, incoming_msg):
    a = ""
    for i in events:
        a += '''{
                    "title": "''' + i["summary"] + '''",
                    "value": "''' + i["summary"] + '''"
                },'''
    a = a[:-1]

    c = '''
    {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
           "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.0",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "Choose the event you want to update"
                },
                {
                    "type": "Input.ChoiceSet",
                    "id": "e_id",
                    "style": "compact",
                    "isMultiSelect": false,
                    "choices": [
                        ''' + a + '''
                    ]
                },
                
                {
                    "type": "TextBlock",
                    "text": "Start Date: "
                },
                {
                    "type": "Input.Date",
                    "id": "onCallDutyStartDate"
                },
                 {
                    "type": "TextBlock",
                    "text": "End Date: "
                },
                {
                    "type": "Input.Date",
                    "id": "onCallDutyEndDate"
                },
                {
                    "type": "TextBlock",
                    "text": "Comment (optional): "
                },
                {
                    "type": "Input.Text",
                    "id": "comment",
                    "placeholder": "Add a comment",
                    "isMultiline": true
                }
            ],
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "REQUEST",
                    "data": {
                        "sender": "''' + incoming_msg.personId + '''"
                    }
                }
            ]
        }
    }
    '''
    return c


def show_card_card():
    c = '''
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
                                "isMultiline": true,
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
    return c


def show_list_card_card():
    c = '''
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
    return c


def create_event_card(e):
    a = ""
    for i in e["agents"]:
        a += '''{
                     "title": "''' + i["lastName"] + " " + i["firstName"] + " - " + i["domain"] + '''",
                     "value": "''' + i["surname"] + '''"
                   },'''
    a = a[:-1]
    c = '''
    {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.0",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "Choose the agent you want to put on this event"
                },
                {
                    "type": "Input.ChoiceSet",
                    "id": "agent_sur",
                    "style": "compact",
                    "isMultiSelect": false,
                    "choices": [
                        ''' + a + '''
                    ]
                },
                {
                    "type": "TextBlock",
                    "text": "Start date: "
                },
                {
                    "type": "Input.Date",
                    "id": "s_date"
                },
                {
                    "type": "TextBlock",
                    "text": "Start Time: "
                },
                {
                    "type": "Input.Time",
                    "id": "s_time",
                    "min": "00:00",
                    "max": "23:59",
                    "value": "08:00"
                },
                {
                    "type": "TextBlock",
                    "text": "Number of days: "
                },
                {
                    "type": "Input.Number",
                    "id": "n_days",
                    "min": 1,
                    "max": 14,
                    "value": 7
                }
           ],
            "actions": [
                {
                  "type": "Action.Submit",
                  "title": "CREATE"
                }
            ]
        }
    }
    '''
    return c


def update_event_card(e, agents):
    a = ""
    for i in e:
        a += '''{
                  "title": "''' + i["summary"] + '''",
                  "value": "''' + i["id"] + '''"
                },'''
    a = a[:-1]

    b = ""
    for i in agents["agents"]:
        b += '''{
                         "title": "''' + i["lastName"] + " " + i["firstName"] + " - " + i["domain"] + '''",
                         "value": "''' + i["surname"] + '''"
                       },'''
    b = b[:-1]

    c = '''
    {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "type": "AdaptiveCard",
            "version": "1.0",
            "body": [
                {
                    "type": "TextBlock",
                    "text": "Choose the event you want to update"
                },
                {
                    "type": "Input.ChoiceSet",
                    "id": "e_id",
                    "style": "compact",
                    "isMultiSelect": false,
                    "choices": [
                        ''' + a + '''
                    ]
                },
                {
                    "type": "TextBlock",
                    "text": "Choose the agent you want to put on this event"
                },
                {
                    "type": "Input.ChoiceSet",
                    "id": "agent_sur",
                    "style": "compact",
                    "isMultiSelect": false,
                    "choices": [
                        ''' + b + '''
                    ]
                },
                {
                    "type": "TextBlock",
                    "text": "Start date: "
                },
                {
                    "type": "Input.Date",
                    "id": "n_start_date"
                },
                {
                    "type": "TextBlock",
                    "text": "Start time: "
                },
                {
                    "type": "Input.Time",
                    "id": "n_start_time",
                    "min": "00:00",
                    "max": "23:59",
                    "value": "08:00"
                },
                {
                    "type": "TextBlock",
                    "text": "End date: "
                },
                {
                    "type": "Input.Date",
                    "id": "n_end_date"
                },
                {
                    "type": "TextBlock",
                    "text": "End time: "
                },
                {
                    "type": "Input.Time",
                    "id": "n_end_time",
                    "min": "00:00",
                    "max": "23:59",
                    "value": "08:00"
                }
            ],
            "actions": [
                {
                    "type": "Action.Submit",
                    "title": "UPDATE"
                }
            ]
        }
    }
    '''
    return c


def delete_event_card(e):
    a = ""
    for i in e:
        a += '''{
                  "title": "''' + i["summary"] + '''",
                  "value": "''' + i["id"] + '''"
                },'''
    a = a[:-1]
    c = '''
    {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
          "type": "AdaptiveCard",
          "version": "1.0",
          "body": [
            {
              "type": "TextBlock",
              "text": "Choose the event you want to delete"
            },
            {
              "type": "Input.ChoiceSet",
              "id": "e_id_del",
              "style": "compact",
              "isMultiSelect": false,
              "value": "1",
              "choices": [
                ''' + a + '''
              ]
            }
          ],
          "actions": [
            {
              "type": "Action.Submit",
              "title": "DELETE"
            }
          ]
        }
    }
    '''
    return c
