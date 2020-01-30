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


def on_call_duty_change_response_card(sender, receiver):
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


def on_call_duty_change_request_card(incoming_msg):
    c = '''
    {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [{
                "type": "Container",
                "items": [{
                    "type": "TextBlock",
                    "text": "On Call duty change request."
                }]
            }],
            "actions": [
                {
                    "type": "Action.ShowCard",
                    "title": "Please fill this form to request your on call duty change",
                    "card": {
                        "type": "AdaptiveCard",
                        "body": [
                             {
                                "type": "TextBlock",
                                "text": "Receiver email: "
                            },
                            {
                                "type": "Input.Text",
                                "id": "receiver",
                                "placeholder": "Email of the receiver",
                                "isMultiline": true
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
                                "title": "OK",
                                "data": {
                                    "sender": "''' + incoming_msg.personId + '''"
                                }
                            }
                        ],
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
                    }                
                }
            ],
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.0"
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


def create_event_card():
    c = '''
    {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": {
            "type": "AdaptiveCard",
            "body": [{
                "type": "Container",
                "items": [{
                    "type": "TextBlock",
                    "text": "Create an event on your calendar."
                }]
            }],
            "actions": [
                {
                    "type": "Action.ShowCard",
                    "title": "Please fill out this form to create an event",
                    "card": {
                        "type": "AdaptiveCard",
                        "body": [
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
                            },
                             {
                                "type": "TextBlock",
                                "text": "Summary: "
                            },
                            {
                                "type": "Input.Text",
                                "id": "summary",
                                "isMultiline": true,
                                "placeholder": "Summary.."
                                
                            },
                             {
                                "type": "TextBlock",
                                "text": "Description: "
                            },
                            {
                                "type": "Input.Text",
                                "id": "description",
                                "placeholder": "Add a description",
                                "isMultiline": true
                            }
                        ],
                        "actions": [
                            {
                                "type": "Action.Submit",
                                "title": "OK",
                                "data": {
                                    
                                }
                            }
                        ],
                        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json"
                    }                
                }
            ],
            "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
            "version": "1.0"
        }
    }
    '''
    return c


def update_event_card(e):
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
              "text": "Choose the event you want to update"
            },
            {
              "type": "Input.ChoiceSet",
              "id": "e_id",
              "style": "compact",
              "isMultiSelect": false,
              "value": "1",
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
            },
             {
                "type": "TextBlock",
                "text": "Summary: "
            },
            {
                "type": "Input.Text",
                "id": "summary",
                "isMultiline": true,
                "placeholder": "Summary.."
                
            },
             {
                "type": "TextBlock",
                "text": "Description: "
            },
            {
                "type": "Input.Text",
                "id": "description",
                "placeholder": "Add a description",
                "isMultiline": true
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
