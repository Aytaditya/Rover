from flask import Flask, render_template
import serial 

# Initialize Flask app
app = Flask(__name__)

# Initialize serial port
ser = serial.Serial(port='COM3', baudrate=9600)

# Route to render webpage
@app.route('/')
def index():
    # Render the 'index.html' template
    return render_template('index.html')

# Route to get data from the serial port
@app.route('/data')
def get_data():
    # Read a line of data from the serial port, decode it, and strip any whitespace characters
    value = ser.readline().decode('utf-8').strip()
    # Return the data as a response to the client
    return value

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
