# ESP32 Battery Tester

This is a simple python app and esp32 sketch to test the battery life of the target microcontroller.

# Prerequisites

This project assumes you have the Arduino IDE setup for your ESP32 and can compile and upload sketches to the module. Additionally this project assumes you have a Python 3 environment to work in (tested on Python 3.7 specifically).

## Quickstart

### Run Server

- Change directory to the project root directory.
- Install dependencies with `pip install -r requirements.txt` (or `pip3 install -r requirements.txt` in posix systems). Consider creating a virtual environment using the venv module and using that for your python environment.
- Run the server by running `python app.py` (or `python3 app.py` for posix systems).
- Note the IP address of your server; the server binds to 0.0.0.0 so you'll need to check that via `ipconfig` in Windows or `ip a` in posix systems.

### Compile and Upload Sketch

- Ensure the ESP32 has the battery installed and charged that you're wanting to test.
- BEFORE OPENING `sketch\sketch.ino`, copy `WifiConfig_example.h` to `WifiConfig.h`. Then uncomment the code and change the ssid and password to your wifi password. Additionally change the server_ip to the ip running the python server.
- Open the `sketch\sketch.ino`.
- Open the serial port monitor and change baud rate to 115200.
- Plug in your ESP32 and compile/upload the sketch.
- Check the serial console for wifi connection verification and the initial HTTP request. You should see a 200 request code and a hello world json return.
- Check the server for successful get requests being received.
- Once observed, unplug the ESP32 and allow it to run on battery until it is dead.

### Interpreting Results

The server will write 2 files. The first `t0.txt` is the timestamp of the initial get request received. The `t1.txt` is the timestamp of the most recent get request. Taking the difference between the two will give you the total battery time of the device.
