import serial
import time

# Configure your serial port (Change 'COM3' to your actual port)
ser = serial.Serial(port='COM4', baudrate=115200, timeout=1)

def send_single_byte(value):
    if value not in (0, 1):
        print("Error: Only 0 or 1 allowed.")
        return

    # Convert the integer 0 or 1 into a single raw byte
    byte_to_send = bytes([value]) 
    
    ser.write(byte_to_send)
    print(f"Sent raw byte: {value} ({byte_to_send})")

try:
    # Example usage: alternate sending 1 and 0
    while True:
        send_single_byte(1)
        time.sleep(1)
        
        send_single_byte(0)
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping...")
finally:
    ser.close()
