import RPi.GPIO as GPIO
import time
import smtplib

# Define GPIO pin for IR sensor
IR_sensor_pin = 18

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Setup IR sensor as input
GPIO.setup(IR_sensor_pin, GPIO.IN)

# Function to send email alert
def send_email_alert(message, subject="Vehicle Theft Alert"):
    # Replace with your SMTP server details (e.g., Gmail)
    sender_email = "your_email@example.com"
    sender_password = "your_email_password"  # Use app-specific password
    receiver_email = "recipient_email@example.com"

    # Create message body
    message = f"Subject: {subject}\n\n{message}"

    try:
        # Connect to SMTP server with TLS encryption
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, sender_password)

        # Send email
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", e)

# Main loop for vehicle theft detection
while True:
    # Read IR sensor status
    if GPIO.input(IR_sensor_pin) == True:
        # IR sensor detects movement, send email alert
        message = "Your vehicle has been triggered by the IR sensor. Please check your vehicle immediately."
        send_email_alert(message)

        # Additional delay (optional, adjust based on needs)
        time.sleep(60)  # Wait 1 minute before checking again

    # No movement detected
    else:
        time.sleep(1)  # Check every second

# Clean up GPIO on program exit (optional)
GPIO.cleanup() send me connections
