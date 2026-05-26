int laser = A0;
int threshold = 12;  // Adjust based on ambient light

void setup() {
  pinMode(laser, INPUT);
  Serial.begin(9600);
}

void rev() {
  char d[9];  // Increased size to store 8 bits + null terminator
  for (int i = 0; i < 8; i++) {
    int bit = analogRead(laser);
    d[i] = (bit > threshold) ? '1' : '0';  // Store as character '1' or '0'
    delay(100);
  }
  d[8] = '\0';  // Null terminator for string
  Serial.println(d);  // Correctly print the binary string
}

void loop() {
  rev();  
}
