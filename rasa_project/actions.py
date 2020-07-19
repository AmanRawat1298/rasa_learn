# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


# class ActionHelloWorld(Action):
class custom_act(Action):

    def name(self) -> Text:
        return "action_selected_restaurant"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any])-> List[Dict[Text, Any]]:

        print("response sent from actions.py!\n")
        
        ################
        entities = tracker.latest_message['entities']
        #entities = Tracker.latest_message['entities']
        print("Entities :",entities)
        message = ""
        for e in entities:
            if e['entity'] == 'theme':
                name = e['value']
        
            if name == "indian":
                message = "INDIAN: This is an indian restaurant"
            if name == "chinese":
                message = "CHINESE: This is an chinese restaurant"
                
        
        dispatcher.utter_message(text="Hello World from custom_actions.py! and entity: "+message)
        return []





class show_leader(Action):

    def name(self) -> Text:
        return "action_show_leader"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        name = tracker.get_slot("name")
        country = tracker.get_slot("country") 
       
        leader_name = ""
        if country.lower() == "us":
            leader_name = "DONALD TRUMP"
        elif country.lower() == "india":
            leader_name = "Modi"
        else:
            leader_name = "Leader Name not available"
          
        message = "{} belongs to {} and leader name is {}".format(name,country,leader_name) 
        print("Message : ", message)


        dispatcher.utter_message(text=message)

        return [SlotSet("leader",leader_name)]
