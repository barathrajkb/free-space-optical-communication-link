void stringToBinary(const char *input, char output[][9], int length) {
    for (int i = 0; i < length; i++) {
        for (int j = 7; j >= 0; j--) {
            output[i][7 - j] = (input[i] & (1 << j)) ? '1' : '0';
        }
        output[i][8] = '\0'; // Null-terminate each binary string
    }
}

void setup() {
    Serial.begin(9600);
    pinMode(3, OUTPUT);  // Laser connected to Pin 3
        char text[] = "akash";
    int length = sizeof(text) - 1; // Exclude null terminator
    char binaryArray[length][9];

    stringToBinary(text, binaryArray, length);
    
    for (int i = 0; i < length; i++) {
        for (int j = 0; j < 8; j++) {
            int bitValue = binaryArray[i][j] - '0';
            digitalWrite(3, bitValue);
            delay(50);
        }
    }
    
}

void loop() {
  digitalWrite(3,LOW);
}
