## story: book room
* greet
  - utter_greet
* book_room
  - form_book_room
  - form{"name": "form_book_room"}
  - form{"name": null}
  - utter_confirm_it
* confirm
  - utter_next_confirm

## story: book room deny
* greet
  - utter_greet
* book_room
  - form_book_room
  - form{"name": "form_book_room"}
  - form{"name": null}
  - utter_confirm_it
* deny
  - utter_next_deny

## story: book room 1
* greet
  - utter_greet
* book_room_with_number{"number_room":"1"}
  - slot{"number_room":"1"}
  - form_book_room_with_number
  - form{"name": "form_book_room_with_number"}
  - form{"name": null}
  - utter_confirm_it
* confirm
  - utter_next_confirm

## story: book room 1 deny
* greet
  - utter_greet
* book_room_with_number{"number_room":"1"}
  - slot{"number_room":"1"}
  - form_book_room_with_number
  - form{"name": "form_book_room_with_number"}
  - form{"name": null}
  - utter_confirm_it
* deny
  - utter_next_deny

## story: book room 2
* greet
  - utter_greet
* book_room_with_number{"number_room":"2"}
  - slot{"number_room":"2"}
  - form_book_room_with_number
  - form{"name": "form_book_room_with_number"}
  - form{"name": null}
  - utter_confirm_it
* confirm
  - utter_next_confirm

## story: book room 2 deny
* greet
  - utter_greet
* book_room_with_number{"number_room":"2"}
  - slot{"number_room":"2"}
  - form_book_room_with_number
  - form{"name": "form_book_room_with_number"}
  - form{"name": null}
  - utter_confirm_it
* deny
  - utter_next_deny



## story: Clean Room
* greet
  - utter_greet
* clean_room
  - utter_ask_time
* time_now
  - utter_quick_response
* goodbye
  - utter_goodbye

## story: Clean Room 1
* greet
  - utter_greet
* clean_room
  - utter_ask_time
* time_after_sometime
  - utter_response_later
* goodbye
  - utter_goodbye

## story: Checkin timings
* ask_checkin
  - utter_checkin
  
## stroy: Checkout timings
* ask_checkout
  - utter_checkout

## story: Cancel Reservation
* ask_cencel_reservation
  - utter_cancel_reservation
  - utter_cancel_reservation_more

## story: Cancellation Policy
* ask_policy
  - utter_policy

## story: Restaurant
* ask_restaurant
  - utter_restaurant

## story: Breakfast Avail
* ask_breakfast
  - utter_breakfast

## story: Breakfast Time
* ask_breakfast_time
  - utter_breakfast_time

## story: Restaurant Time
* ask_restaurant_time
  - utter_restaurant_time

## story: Security
* ask_security
  - utter_security

## story: Contact details
* ask_contact_details
  - utter_contact_details
