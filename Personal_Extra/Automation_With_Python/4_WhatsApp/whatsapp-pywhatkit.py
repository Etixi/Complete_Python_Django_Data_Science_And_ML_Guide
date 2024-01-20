import pywhatkit
import time


# Get phone number from user input
phone_number = input('Enter phone number (with country code): ')
pywhatkit.sendwhatmsg(phone_number, "Test", 0, 0)

# Check if the country code is included
# if not phone_number.startswith('+'):
#     print("Please include the country code starting with '+' in the phone number.")
# else:
#     try:
#         # Send a WhatsApp message with a 0-second delay
#         pywhatkit.sendwhatmsg(phone_number, "This is a test message with a 0s delay", 0, 0, wait_time=0)
#         print("Message sent with a 0-second delay!")
#     except KeyboardInterrupt:
#         print("Process was manually interrupted.")
#     except Exception as e:
#         print(f"An error occurred: {e}")



