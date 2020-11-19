# Rasa-hotel-chatbot-20
I am trying to build a simple chat-bot for a hotel. Here I am using the Rasa framework for this project.

# Objective
This chatbot is able to do the following basic functionalities
Book room
Request Room Cleaning
Handle FAQs
Handle Greetings

# Requirements
python 3.6.8 and Rasa 2.0 

# Require cmd
Train the chatbot -> rasa train
Run action server -> rasa run actions
Build a rasa server -> rasa shell

# Flow of conversation
# Book Room
User: I want to book a room.

Bot: How many rooms would you like to book?

User: 2 rooms

Bot: What type of room would you want to book?

Button01 - Simple
Button 2 - Deluxe
User: (selecting the type as Simple)

Bot: You have chosen to book 2 simple rooms

# Clean room
Schedule cleaning right away -
User: I want to have my room cleaned

Bot: When should I arrange for a cleaning?

User: Could you send someone right now?

Bot: Sure, I will send someone to your room right away.

Schedule cleaning using relative time -
User: I want to have my room cleaned

Bot: When should I arrange for a cleaning?

User: Could you send someone after 2 hours?

Bot: Sure, I have scheduled a cleaning for 5 pm today.

# FAQs
Check-in timings -
User: What are your check-in timings?

Bot: Check-in time starts at 4 PM. Minimum check-in age is 21. Please contact the reception for early check-in requests.

Check-out timings -
User: What are your check-out timings?

Bot: Check-out time is 11 AM. Please contact the reception for late checkout requests.

Cancel Reservation -
User: How do I cancel a reservation?

Bot: To cancel a reservation, select the “Reservations” link from the homepage.

Bot: On the Reservations page, under the heading ‘View, Change or Cancel a Reservation,’ enter your confirmation number, and either the last name on the reservation or the last four digits of the credit card used to make the reservation.

Cancellation Policy -
User: What is your cancellation policy?

Bot: The booking deposit is refundable if the cancellation occurs at least 15 days before arrival. For cancellations made after this limit, a penalty will be imposed based on the cancellation policy.

Restaurant -
User: Does the hotel have a restaurant?

Bot: Yes, the hotel has a restaurant called the Zephyr Bar. With our menu we strive to reflect the historic art and the spirit of our neighborhood by offering a glimpse into what makes our area unique.

Breakfast Availability -
User: Does the hotel offer breakfast?

Bot: The hotel provides its guests with a free made-to-order breakfast each morning.

Breakfast timings -
User: What are the breakfast timings?

Bot: Monday through Friday breakfast is 6 am to 9 am. On Saturday and Sunday, we are open from 7 am to 10:30 am.

Restaurant timings -
User: What are the timings of your restaurant?

Bot: Our restaurant serves a dazzling 24-hour menu.
 
Security
User: what are the security systems available
Bot: The Hotel has the following Security Arrangements:
          Fire Safety
          Wet Riser System
          Alarm Syste
          CCTV Cameras
          24-hours Control Room to monitor the security cameras
          EVD Machine to scan the luggage 
          24-hours fire fighting & first aid trained security guards

Contact Number
User: What is the customer support number?
Bot:      Contact Number-928467
          Mail ID:- hotel@abc.com
          Address:- xyz Nagar PQR city, 305781
          
          
Submission:- 
Thank you @Limechat for this assignment.
