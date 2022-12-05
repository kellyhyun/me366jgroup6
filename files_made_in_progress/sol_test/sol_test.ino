byte sol_status = HIGH;
int solPin = 9;

void setup() {
    Serial.begin(115200);
    pinMode(solPin, OUTPUT);

}

void loop() {
    digitalWrite(solPin, LOW);
    delay(200);
    digitalWrite(solPin, HIGH);
    delay(500);
}