
## intent: greet
    - hey
    - hello
    - hi
    - hello there
    - hi there
    - good morning
    - good evening
    - moin
    - hey there
    - let's go
    - hey dude
    - goodmorning
    - goodevening
    - good afternoon
    - let's start
    - help me

## intent: goodbye
    - good afternoon
    - cu
    - good by
    - cee you later
    - good night
    - bye
    - goodbye
    - have a nice day
    - see you around
    - bye bye
    - see you later

## intent: book_room
    - I want to book a room.
    - Can you book a room?
    - How many rooms are available?
    - I would like to book a room.
    - I would like to have a room.
    - I want to stay here.
    - Can you give me the available rooms details?
    - Can I stay here?
    - Please book a room.
    - Please provide me a room.
    - Can you give a room for one day?
    - room
    - book room
    - book a room
    - How many rooms are available?

## intent: room_no
    - [1](number_room)
    - [2](number_room)
    - [1](number_room) room
    - [2](number_room) rooms
    - I want to book [1](number_room) room for 2 people
    - I want to book [2](number_room) rooms.
    - I want to book [2](number_room) rooms.
    - I want to book [1](number_room) room.
    - I would like to book [1](number_room) room for 2 people.
    - I would like to book [2](number_room) rooms.
    - Please book [2](number_room) room for 2 person.
    - Please provide me [1](number_room) room for two person.
    - Can you give [2](number_room) rooms for one day?

    
## intent: room_type_1
    - [Simple](r_type)
    - [Deluxe](r_type)
    - [simple](r_type:Simple)
    - [deluxe](r_type:Deluxe)
    - [simple](r_type:Simple) room
    - [deluxe](r_type:Deluxe) room

## intent: book_room_with_number
#    - I want to book [1](number_room) room for 2 people
#    - I want to book [2](number_room) rooms.
#    - I want to book [2](number_room) rooms.
#    - I want to book [1](number_room) room.
#    - I would like to book [1](number_room) room for 2 people.
#    - I would like to book [2](number_room) rooms.
#    - Please book [2](number_room) room for 2 person.
#    - Please provide me [1](number_room) room for two person.
#    - Can you give [2](number_room) rooms for one day?

## intent:confirm
    - Yes
    - Sure
    - Perfect
    - Confirm
    - yes
    - indeed 
    - of course
    - that sounds good
    - correct
    - affirmative
    - ok
    - okay
    - right

## intent:deny
    - No
    - Not looking right
    - no
    - never
    - I don't think so
    - don't like that
    - wrong
    - no way
    - not really
    - delete it
    - deny it
    - Not perfect
    - one more thing
    - ask again

## intent: clean_room
    -I want to have my room cleaned.
    -I have a request to clean my room.
    -I would like to have my room cleaned.
    -Please clean my room.
    -Please tell me about cleaning of the room.
    -When can I get my room cleaned?
    -Tell me about room's cleaning status.
    -Clean the room

## intent: time_now
    -Could you send someone right now?
    -I want to my room cleaned right now.
    -Send someone right now.
    -right now.
    -now
    -as soon as possible.
    -ASAP

## intent: time_after_sometime
    -Could you send someone after 2 hours?
    -Send someone after sometime.
    -Could you send someone after 3 hours?
    -Send someone after 2 hours.
    -Could you send someone after an hour?
    -Send someone after an hour.
    -not now.
    -After sometime.
    -Could you send someone before this night.
    -Send someone before this night.

## intent: ask_checkin
    -What is the check-in time of a hotel?
    -What are the standard check-in?
    -What are your check-in timings?
    -At what time can I check-in?
    -what is the checkin time?
    -what is the check-in time?
    -Check-in time?
    -Tell me about check-in time.
    -checkin

## intent: ask_checkout
    -What are your check-out timings?
    -what is the check-out time?
    -what is the checkout time?
    -What is the check-out time of a hotel?
    -checkout time?
    -checkout

## intent: ask_cencel_reservation
    -How do I cancel a reservation?
    -Can I cancel only certain parts of my reservation (for example one of the two booked rooms)?
    -Is it possible for partially cancelling the rooms
    -Can I cancel my hotel booking? 
    -How can I cancel my reservation?
    -Tell me the process to cancel the reservation.
    -cancel reservation.

## intent: ask_policy
    -What is your cancellation policy?
    -Tell me about the cancellation policy.
    -Is there any police to cancel the reservation?
    -How much refund can I get according to the cancellation policy?
    -policy?
  
## intent: ask_restaurant
    - Does the hotel have a restaurant?
    - Is there any restaurant in hotel?
    - Can I get restaurant in the hotel?
    - restaurant

## intent: ask_breakfast
    -Does the hotel offer breakfast?
    -Can I get breakfast from yourside?
    -Is breakfast included in this reservation?
    -Breakfast?

## intent: ask_breakfast_time
    -What are the breakfast timings?
    -can you specify the time for the breakfast?
    -at what time will you serve the breakfast?
    -what is the time for the breakfast?
    -Tell me about the breakfast timings?
    -Breakfast timings.
    -Breakfast time.

## intent: ask_restaurant_time
    -What are the restaurant timings?
    -can you specify the time for the restaurant?
    -at what time can I go to restaurant?
    -what is the time for the restaurant?
    -Tell me about the restaurant timings.
    -Restaurant timings.
    -Restaurant time?

## intent: ask_contact_details
    -What is the customer support number?
    -What is your phone number?
    -can you give me the hotel contact number
    -contact number
    -Is there a contact number for the hotel?
    -What is the contact number of the reception?


## intent: ask_security
    -tell me about the security services
    -tell me the security arrangements of the hotel
    -what are the security systems available
    -What security arrangements are available in your hotel?
    -Security?
