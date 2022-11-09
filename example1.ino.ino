byte AStatus = HIGH;
byte BStatus = HIGH;
byte CStatus = HIGH;
byte DStatus = HIGH;
byte EStatus = HIGH;
byte FStatus = HIGH;
byte GStatus = HIGH;
byte GLowStatus = HIGH;
byte ALowStatus = HIGH;
byte BLowStatus = HIGH;
byte CHighStatus = HIGH;
byte DHighStatus = HIGH;
byte EHighStatus = HIGH;
byte FHighStatus = HIGH;
byte GHighStatus = HIGH;
int GLowPin = 5;
int ALowPin = 6;
int BLowPin = 7;
//CHANGE LATER//
int CPin = 9;
int DPin = 10;
//            //
int EPin = 11;
int FPin = 12;
int GPin = 13;
int APin = 14;
int BPin = 15;
int CHighPin = 16;
int DHighPin = 17;
int EHighPin = 18;
int FHighPin = 19;
int GHighPin = 20;



void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 pinMode(CPin,OUTPUT);
 pinMode(DPin,OUTPUT);
 pinMode(EPin,OUTPUT);
 pinMode(FPin,OUTPUT);
 pinMode(GPin,OUTPUT);
}
void loop() {
 if(Serial.available())
    {
        char cmd = Serial.read();
        switch(cmd)
        {
            case 'A':
              AStatus = LOW;
//              Serial.println("Cmd received");
              break;

            case 'B':
              BStatus = LOW;
//             Serial.println("Cmd received");
              break;

            case 'C':
              CStatus = LOW;
//              Serial.println("Cmd received");
              break;

            case 'D':
              DStatus = LOW;
//             Serial.println("Cmd received");
              break;

            case 'E':
              EStatus = LOW;
//              Serial.println("Cmd received");
              break;

            case 'F':
              FStatus = LOW;
//              Serial.println("Cmd received");
              break;

            case 'G':
              GStatus = LOW;
//              Serial.println("Cmd received");
              break;

            case 'H':
              GLowStatus = LOW;
//              Serial.println("Cmd received");
              break;
            
            case 'I':
              ALowStatus = LOW;
//              Serial.println("Cmd received");
              break;

            case 'J':
              BLowStatus = LOW;
//              Serial.println("Cmd received");
              break;

            case 'K':
              CHighStatus = LOW;
//              Serial.println("Cmd received");
              break;
  
            case 'L':
              DHighStatus = LOW;
//            Serial.println("Cmd received");
             break;

            case 'M':
              EHighStatus = LOW;
//              Serial.println("Cmd received");
              break;

            case 'N':
              FHighStatus = LOW;
//            Serial.println("Cmd received");
              break;

            case 'O':
              GHighStatus = LOW;
              //Serial.println("Cmd received");
              break;
  
            case 'p':
              play();
              break;    
        }
    } 
}

void play() {
  digitalWrite(GLowPin,GLowStatus);
  digitalWrite(ALowPin,ALowStatus);
  digitalWrite(BLowPin,BLowStatus);
  digitalWrite(CPin,CStatus);
  digitalWrite(DPin,DStatus);
  digitalWrite(EPin,EStatus);
  digitalWrite(FPin,FStatus);
  digitalWrite(GPin,GStatus);
  digitalWrite(APin,AStatus);
  digitalWrite(BPin,BStatus);
  digitalWrite(CHighPin,CHighStatus);
  digitalWrite(DHighPin,DHighStatus);
  digitalWrite(EHighPin,EHighStatus);
  digitalWrite(FHighPin,FHighStatus);
  digitalWrite(GHighPin,GHighStatus);
  delay(50);
  AStatus = HIGH;
  BStatus = HIGH;
  CStatus = HIGH;
  DStatus = HIGH;
  EStatus = HIGH;
  FStatus = HIGH;
  GStatus = HIGH;
  GLowStatus = HIGH;
  ALowStatus = HIGH;
  BLowStatus = HIGH;
  CHighStatus = HIGH;
  DHighStatus = HIGH;
  EHighStatus = HIGH;
  FHighStatus = HIGH;
  GHighStatus = HIGH;
  digitalWrite(GLowPin,GLowStatus);
  digitalWrite(ALowPin,ALowStatus);
  digitalWrite(BLowPin,BLowStatus);
  digitalWrite(CPin,CStatus);
  digitalWrite(DPin,DStatus);
  digitalWrite(EPin,EStatus);
  digitalWrite(FPin,FStatus);
  digitalWrite(GPin,GStatus);
  digitalWrite(APin,AStatus);
  digitalWrite(BPin,BStatus);
  digitalWrite(CHighPin,CHighStatus);
  digitalWrite(DHighPin,DHighStatus);
  digitalWrite(EHighPin,EHighStatus);
  digitalWrite(FHighPin,FHighStatus);
  digitalWrite(GHighPin,GHighStatus);
}
