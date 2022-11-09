byte AStatus = LOW;
byte BStatus = LOW;
byte CStatus = LOW;
byte DStatus = LOW;
byte EStatus = LOW;
byte FStatus = LOW;
byte GStatus = LOW;
byte GLowStatus = LOW;
byte ALowStatus = LOW;
byte BLowStatus = LOW;
byte CHighStatus = LOW;
byte DHighStatus = LOW;
byte EHighStatus = LOW;
byte FHighStatus = LOW;
byte GHighStatus = LOW;
int GLowPin = 5;
int ALowPin = 6;
int BLowPin = 7;
//CHANGE LATER//
int CPin = 9;
int DPin = 8;
//            //
int EPin = 10;
int FPin = 11;
int GPin = 12;
int APin = 13;
int BPin = 14;
int CHighPin = 15;
int DHighPin = 16;
int EHighPin = 17;
int FHighPin = 18;
int GHighPin = 19;



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
            case 'A':
              AStatus = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'B':
              BStatus = HIGH;
//             Serial.println("Cmd received");
              break;

            case 'C':
              CStatus = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'D':
              DStatus = HIGH;
//             Serial.println("Cmd received");
              break;

            case 'E':
              EStatus = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'F':
              FStatus = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'G':
              GStatus = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'H':
              GLowStatus = HIGH;
//              Serial.println("Cmd received");
              break;
            
            case 'I':
              ALowStatus = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'J':
              BLowStatus = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'K':
              CHighStatus = HIGH;
//              Serial.println("Cmd received");
              break;
  
            case 'L':
              DHighStatus = HIGH;
//            Serial.println("Cmd received");
             break;

            case 'M':
              EHighStatus = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'N':
              FHighStatus = HIGH;
//            Serial.println("Cmd received");
              break;

            case 'O':
              GHighStatus = HIGH;
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
  delay(400);
  AStatus = LOW;
  BStatus = LOW;
  CStatus = LOW;
  DStatus = LOW;
  EStatus = LOW;
  FStatus = LOW;
  GStatus = LOW;
  GLowStatus = LOW;
  ALowStatus = LOW;
  BLowStatus = LOW;
  CHighStatus = LOW;
  DHighStatus = LOW;
  EHighStatus = LOW;
  FHighStatus = LOW;
  GHighStatus = LOW;
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
