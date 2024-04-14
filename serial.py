from flask import Flask, render_template
import serial 

# Initialize Flask app
app = Flask(__name__)

# Initialize serial port
ser = serial.Serial(port='COM3', baudrate=9600)

# Route to render webpage
@app.route('/')
def index():
    # Reading data from serial port
    value = ser.readline().decode('utf-8').strip()
    # Rendering the 'index.html' template with the value
    return render_template('index.html', value=value)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
