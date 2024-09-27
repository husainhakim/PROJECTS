import pywhatkit as kit

phone_number = input("Enter the phone number :-")
phone = f"+91{phone_number}"  # Use the format: +CountryCodePhoneNumber
message = input("Enter a message:-")

# Set the time for sending the message
hour = int(input("Enter the hour (24-hour format):-"))  # 24-hour format
minute = int(input("Enter minutes:-"))

# Send the message
kit.sendwhatmsg(phone, message, hour, minute)
