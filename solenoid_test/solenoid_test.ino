int solPin = 9;
int solPin2 = 10;
int solPin3 = 11;
int solPin4 = 12;
int solPin5 = 13;

void setup() {
  // put your setup code here, to run once:
pinMode(solPin,OUTPUT);
digitalWrite(solPin,LOW);
pinMode(solPin2,OUTPUT);
digitalWrite(solPin2,LOW);
pinMode(solPin3,OUTPUT);
digitalWrite(solPin3,LOW);
pinMode(solPin4,OUTPUT);
digitalWrite(solPin4,LOW);
pinMode(solPin5,OUTPUT);
digitalWrite(solPin5,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
digitalWrite(solPin,HIGH);
digitalWrite(solPin2,HIGH);
digitalWrite(solPin3,HIGH);
digitalWrite(solPin4,HIGH);
digitalWrite(solPin5,HIGH);
delay(500);
digitalWrite(solPin,LOW);
digitalWrite(solPin2,LOW);
digitalWrite(solPin3,LOW);
digitalWrite(solPin4,LOW);
digitalWrite(solPin5,LOW);
delay(500);

}
