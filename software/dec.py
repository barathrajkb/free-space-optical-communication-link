import serial
import time

def str2arr(data):
    x = data[data.find('1') - 1:]
    main_data = []
    k = 0

    for i in range(int(len(x) / 8)):
        temp = ''
        for j in range(8):
            temp += x[k]
            k += 1
        main_data.append(temp)

    return main_data


def bin2txt(binary_list):
    ascii_string = ''.join(
        chr(int(b, 2)) for b in binary_list if b != '00000000'
    )
    return ascii_string


arduino = serial.Serial('COM7', 9600, timeout=1)

time.sleep(2)

data = ""

print("Receiving data... Press Ctrl+C to stop.\n")

try:
    while True:
        line = arduino.readline().decode(errors='ignore').strip()

        if line:
            print("Received:", line)
            data += line

            # Decode once enough bits are received
            if len(data) >= 8:
                try:
                    txt = bin2txt(str2arr(data))
                    print("Decoded Text:", txt)
                except:
                    pass

except KeyboardInterrupt:
    print("\nStopped.")

finally:
    arduino.close()