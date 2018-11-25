#include "Arduino.h"
#include <IRremote.h> //header file for IR receiver
int irpin = 11; //pin number to which IR sensor is connected
IRrecv irrecv(irpin); //object of class IRrecv included in the header file IRremote.h which specifies which pin of arduino is connected to the sensor
decode_results results; //object of class decode_results included in the header file IRremote.h which specifies the obtained value from the sensor
void setup() {
 Serial.begin(9600); //Setting the baud rate of serial communication
 irrecv.enableIRIn(); // Start IR receiver
 pinMode(2, OUTPUT);
 pinMode(3, OUTPUT);
 pinMode(4, OUTPUT);
 pinMode(5, OUTPUT);
}

void loop() {
  if (irrecv.decode(&results)) //checking whether decoded value is not a null value
  {
    if (results.value==16758855){ //code for button press 2
    digitalWrite(2, HIGH);
    }
    else if (results.value==16756815){ //code for button press 8
    digitalWrite(3, HIGH);
    }
    else if (results.value==16767015){ //code for button press 4
    digitalWrite(4, HIGH);
    }
    else if(results.value==16754775){ //code for button press 6
    digitalWrite(5, HIGH);
    }
    else{ //code for stopping
      digitalWrite(2, LOW);
      digitalWrite(3, LOW);
      digitalWrite(4, LOW);
      digitalWrite(5, LOW);
    }
    
    irrecv.resume(); //for checking next value, resume() function is included from IRrecv class of IRremote.h header file
  }
}


