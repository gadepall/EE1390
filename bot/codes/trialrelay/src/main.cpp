#include "Arduino.h"
#include <IRremote.h> //header file for IR receiver
int irpin = 11; //pin number to which IR sensor is connected
IRrecv irrecv(irpin); //object of class IRrecv included in the header file IRremote.h which specifies which pin of arduino is connected to the sensor
decode_results results; //decoded value of the result stored as object of the class decode_results included in the header file IRremote.h
void setup()
{
 Serial.begin(9600); //Setting the baud rate of serial communication
 irrecv.enableIRIn(); // Start IR receiver
}
void loop() {
 if (irrecv.decode(&results)) {//checking whether decoded value is not a null value
  {
   Serial.println(results.value); //printing the results on the serial monitor
   irrecv.resume(); // Receive the next value
  }
 }
} 
