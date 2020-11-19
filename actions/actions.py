# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT

class RoomInfo(FormAction):
    def name(self) -> Text:
        return "form_book_room"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["number_room", "r_type"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message(template="utter_book_details_1", number_room=tracker.get_slot('number_room'),
                                 R_type=tracker.get_slot('r_type'))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "number_room": [self.from_entity(entity="number_room", intent=["room_no"])],
            "R_type": [self.from_entity(entity="r_type", intent=["room_type_1"])],
        }

class RoomNumberInfo(FormAction):
    def name(self) -> Text:
        return "form_book_room_with_number"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["r_type"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
 
        dispatcher.utter_message(template="utter_book_details_1", 
                                R_type=tracker.get_slot('r_type'))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "R_type": [self.from_entity(entity="r_type", intent=["room_type_1"])],
        }

#class SetNull(Action):
#
#    def name(self):
#        return "action_set_null"
#
#    def run(self, dispatcher, tracker, domain):
#        return [SlotSet("number", None), SlotSet("r_type", None)]

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
