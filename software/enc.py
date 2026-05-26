import serial
import time

def str2arr(data):
    x = data[data.find('1')-1:]
    main_data = []
    k = 0
    for i in range(int(len(x)/8)):
        temp = ''
        for j in range(8):
            temp+= x[k]
            k += 1
        main_data.append(temp)
    return main_data


def bin2txt(binary_list):
    ascii_string = ''.join(chr(int(b, 2)) for b in binary_list if b != '00000000')
    return ascii_string

arduino = serial.Serial(port="COM7", baudrate=9600, timeout=1)
time.sleep(2)
with open("arduino_data.txt", "w") as file:
    print("Logging data... Press Ctrl+C to stop.")

    try:
        while True:
            data = arduino.readline().decode().strip()  # Read and decode the data
            if data:
                print(data)
                file.write(data)
                file.flush()
    except KeyboardInterrupt:
        print("\nStopped by user.")
arduino.close()

with open("arduino_data.txt", "r") as file:
    data = file.read()
    txt = bin2txt(str2arr(data))
    print(txt)

