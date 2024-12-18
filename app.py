import RPi.GPIO as GPIO
from flask import Flask, render_template, redirect, url_for
import time

# Set up Flask app
app = Flask(__name__)

# Set GPIO mode and pin for LED
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
LED_PIN = 14  # GPIO pin for the LED
GPIO.setup(LED_PIN, GPIO.OUT)  # Set the pin as an output

@app.route('/')
def index():
    """ Home route to display the current LED status """
    led_status = GPIO.input(LED_PIN)  # Read the current state of the LED
    return render_template('index.html', led_status=led_status)

@app.route('/on')
def turn_on():
    """ Route to turn on the LED """
    try:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
        print("LED turned ON")
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error turning LED on: {e}")
        return f"Error turning LED on: {e}", 500

@app.route('/off')
def turn_off():
    """ Route to turn off the LED """
    try:
        GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
        print("LED turned OFF")
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error turning LED off: {e}")
        return f"Error turning LED off: {e}", 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
