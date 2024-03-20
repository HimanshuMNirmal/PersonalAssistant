import threading
import pywhatkit
import datetime

def send_whatsapp_message(number, message, time):
    try:
        # Parse the time string to a datetime object
        scheduled_time = datetime.datetime.strptime(time, "%H:%M")
        
        # Schedule the message asynchronously
        threading.Thread(target=send_message_async, args=(number, message, scheduled_time)).start()

        print("Message scheduled successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def send_message_async(number, message, scheduled_time):
    # Wait until the scheduled time
    while datetime.datetime.now() < scheduled_time:
        pass

    # Send the message
    pywhatkit.sendwhatmsg(number, message, scheduled_time.hour, scheduled_time.minute)
