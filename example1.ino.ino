byte AStatus = LOW;
byte BStatus = LOW;

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
}
void loop() {
 if(Serial.available())
    {
        char cmd = Serial.read();
        switch(cmd)
        {
            case'A':
            AStatus = HIGH;
            Serial.println("Cmd received");
            break;

            case'B':
            BStatus = HIGH;
            Serial.println("Cmd received");
            break;

            case'p':
            play();
            break;    
        }
    } 
}

void play() {
  digitalWrite(9,AStatus);
  digitalWrite(10,BStatus);
  delay(400);
  AStatus = LOW;
  BStatus = LOW;
  digitalWrite(9,AStatus);
  digitalWrite(10,BStatus);
}
