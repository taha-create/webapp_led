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

@app.route('/toggle')
def toggle_led():
    """ Route to toggle the LED """
    try:
        # Get current LED state and toggle it
        current_status = GPIO.input(LED_PIN)
        new_status = GPIO.LOW if current_status == GPIO.HIGH else GPIO.HIGH
        GPIO.output(LED_PIN, new_status)  # Set the new state for the LED
        print("LED toggled, current state:", "ON" if new_status == GPIO.HIGH else "OFF")
        
        # Redirect to the home route to reflect the new state
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error toggling LED: {e}")
        return f"Error toggling LED: {e}", 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
