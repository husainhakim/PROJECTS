# WhatsApp Message Sender

This Python script allows users to send WhatsApp messages to any phone number at a scheduled time using the `pywhatkit` library. The script prompts the user for the recipient's phone number and the message content, and then sends the message at the specified hour and minute.

## Features

- Fetches the phone number input from the user.
- Allows users to enter a custom message.
- Sends messages at a specified time in 24-hour format.
- User-friendly command line interface.

## Prerequisites

- Python 3.x
- `pywhatkit` library

## Installation

1. Install the required library:
```
   pip install pywhatkit
```
2.	Clone the repository (if applicable):<br>
 ```
	git clone <repository-url>
 ```
3.	Navigate to the project directory (if applicable):<br>
```
    cd <project-directory>
```

<h3>Enter the following when prompted:</h3>
•	Phone Number: Enter the phone number (without the country code).<br>
•	Message: Enter the message you want to send.<br>
•	Hour: Enter the hour (in 24-hour format) for when you want to send the message.<br>
•	Minutes: Enter the minutes for the scheduled time.<br>

# Example Output
<h3>Output</h3>
<img src="Output.png" width="600"/>
<h3>Result</h3>
<img src="Result.png" width="600"/>

# Error Handling

•	If the phone number format is incorrect, the script will prompt you to enter it again.
•	Handles errors gracefully if there are issues sending the message.

# License

This project is open source and available under the MIT License.

# Contact

For any questions or feedback, please contact:

•	Name: Husain Hakim <br>
•	Email: husain.m.hakim.533@gmail.com<br>
•	GitHub: <a href="https://github.com/husainhakim">husainhakim</a>
 
