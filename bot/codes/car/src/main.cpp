#include "Arduino.h"
#include <IRremote.h> //header file for IR receiver
int irpin = 11; //pin number to which IR sensor is connected
IRrecv irrecv(irpin); //object of class IRrecv included in the header file IRremote.h which specifies which pin of arduino is connected to the sensor
decode_results results; //object of class decode_results included in the header file IRremote.h which specifies the obtained value from the sensor

const int m1n=3; //pin for (-ve) direction of motor1
const int m2p=4; //pin for (+ve) direction of motor2
const int m2n=5; //pin for (-ve) direction of motor2
const int m1p=2; //pin for (+ve) direction of motor1


void setup() {
 Serial.begin(9600); //Setting the baud rate of serial communication
 irrecv.enableIRIn(); // Start IR receiver

  pinMode(m1p, OUTPUT);
  pinMode(m1n, OUTPUT);
  pinMode(m2p, OUTPUT);
  pinMode(m2n, OUTPUT);

}
void loop() {
  if (irrecv.decode(&results)) //checking whether decoded value is not a null value
  {
	  Serial.println(results.value);
    if (results.value==16758855){ //code for button press 2
    digitalWrite(m1p, HIGH); 
    digitalWrite(m1n, LOW);
    digitalWrite(m2p, HIGH);
    digitalWrite(m2n, LOW);
  }
  else if (results.value==16756815){ //code for button press 8
    digitalWrite(m1p, LOW);
    digitalWrite(m1n, HIGH);
    digitalWrite(m2p, LOW);
    digitalWrite(m2n, HIGH);
  }
 else if (results.value==16767015){ //code for button press 4
    digitalWrite(m1p, HIGH);
    digitalWrite(m1n, LOW);
    digitalWrite(m2p, LOW);
    digitalWrite(m2n, LOW);
  }
     else if(results.value==16754775){ //code for button press 6
    digitalWrite(m1p, LOW);
    digitalWrite(m1n, LOW);
    digitalWrite(m2p, HIGH);
    digitalWrite(m2n, LOW);
  }
    else if(results.value==16750695){
    digitalWrite(m1p, LOW);
    digitalWrite(m1n, LOW);
    digitalWrite(m2p, LOW);
    digitalWrite(m2n, LOW);
  }
   irrecv.resume(); //for checking next value, resume() function is included from IRrecv class of IRremote.h header file
}

}

