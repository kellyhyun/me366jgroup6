#include <Adafruit_NeoPixel.h>

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

#define LEDPIN 21
#define NUMPIXELS 22
byte LED[NUMPIXELS];

int colors[NUMPIXELS][3] = 
  {
    {255, 0, 0},
    {150, 0, 150},
    {150, 0, 150},
    {150, 150, 150},
    {0, 0, 255},
    {0, 0, 255},
    {0, 255, 0},
    {150, 150, 0},
    {150, 150, 0},
    {150, 97, 0},
    {255, 0, 0},
    {255, 0, 0},
    {150, 0, 150},
    {150, 150, 150},
    {150, 150, 150},
    {0, 0, 255},
    {0, 255, 0},
    {0, 255, 0},
    {150, 150, 0},
    {150, 97, 0},
    {150, 97, 0},
    {255, 0, 0},
  };

Adafruit_NeoPixel pixels(NUMPIXELS, LEDPIN, NEO_GRB + NEO_KHZ800);

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
 for (int i = GLowPin; i<=GHighPin; i++) {
    pinMode(i,OUTPUT);
 }
 pinMode(LEDPIN,OUTPUT);
}
void loop() {
 if(Serial.available())
    {
        char cmd = Serial.read();
        switch(cmd)
        {
            case 'A':
              AStatus = LOW;
              LED[12] = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'B':
              BStatus = LOW;
              LED[13] = HIGH;
              LED[14] = HIGH;
//             Serial.println("Cmd received");
              break;

            case 'C':
              CStatus = LOW;
              LED[4] = HIGH;
              LED[5] = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'D':
              DStatus = LOW;
              LED[6] = HIGH;
//             Serial.println("Cmd received");
              break;

            case 'E':
              EStatus = LOW;
              LED[7] = HIGH;
              LED[8] = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'F':
              FStatus = LOW;
              LED[9] = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'G':
              GStatus = LOW;
              LED[10] = HIGH;
              LED[11] = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'H':
              GLowStatus = LOW;
              LED[0] = HIGH;
//              Serial.println("Cmd received");
              break;
            
            case 'I':
              ALowStatus = LOW;
              LED[1] = HIGH;
              LED[2] = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'J':
              BLowStatus = LOW;
              LED[3] = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'K':
              CHighStatus = LOW;
              LED[15] = HIGH;
//              Serial.println("Cmd received");
              break;
  
            case 'L':
              DHighStatus = LOW;
              LED[16] = HIGH;
              LED[17] = HIGH;
//            Serial.println("Cmd received");
             break;

            case 'M':
              EHighStatus = LOW;
              LED[18] = HIGH;
//              Serial.println("Cmd received");
              break;

            case 'N':
              FHighStatus = LOW;
              LED[19] = HIGH;
              LED[20] = HIGH;
//            Serial.println("Cmd received");
              break;

            case 'O':
              GHighStatus = LOW;
              LED[21] = HIGH;
              //Serial.println("Cmd received");
              break;
  
            case 'p':
              play();
              break;    
        }
    } 
}

void play() {
  for (int i = 0; i < NUMPIXELS; i++) {
    if (LED[i] == HIGH) {
        pixels.setPixelColor(i, pixels.Color(colors[i][0],colors[i][1],colors[i][2]));
        LED[i] = LOW;
    }
  }
  pixels.show();
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
  pixels.clear();
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
