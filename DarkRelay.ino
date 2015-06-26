/*****************************************************
This is the demo sketch for the command line interface
by FreakLabs. It's a simple command line interface
where you can define your own commands and pass arguments
to them. 
*****************************************************/
#include <Cmd.h>

int relay1_pin = 31;
int relay2_pin = 32;
int relay3_pin = 33;
int relay4_pin = 34;
int relay5_pin = 35;
int relay6_pin = 36;
int relay7_pin = 37;
int relay8_pin = 38;

bool relay1_enb = false;
bool relay2_enb = false;
bool relay3_enb = false;
bool relay4_enb = false;
bool relay5_enb = false;
bool relay6_enb = false;
bool relay7_enb = false;
bool relay8_enb = false;

int led_blink_delay_time = 1000;

void setup()
{
  // set the led pin as an output. its part of the demo.
  pinMode(relay1_pin, OUTPUT); 
  pinMode(relay2_pin, OUTPUT); 
  pinMode(relay3_pin, OUTPUT); 
  pinMode(relay4_pin, OUTPUT); 
  pinMode(relay5_pin, OUTPUT); 
  pinMode(relay6_pin, OUTPUT); 
  pinMode(relay7_pin, OUTPUT); 
  pinMode(relay8_pin, OUTPUT); 
  
  
  
  // init the command line and set it for a speed of 57600
  cmdInit(57600);
  
  // add the commands to the command table. These functions must
  // already exist in the sketch. See the functions below. 
  // The functions need to have the format:
  //
  // void func_name(int arg_cnt, char **args)
  //
  // arg_cnt is the number of arguments typed into the command line
  // args is a list of argument strings that were typed into the command line
  cmdAdd("relay1yes", relay1yes);
  cmdAdd("relay1no", relay1no);
  cmdAdd("relay2yes", relay2yes);
  cmdAdd("relay2no", relay2no);
  cmdAdd("relay3yes", relay3yes);
  cmdAdd("relay3no", relay3no);
  cmdAdd("relay4yes", relay4yes);
  cmdAdd("relay4no", relay4no);
  cmdAdd("relay5yes", relay5yes);
  cmdAdd("relay5no", relay5no);
  cmdAdd("relay6yes", relay6yes);
  cmdAdd("relay6no", relay6no);
  cmdAdd("relay7yes", relay7yes);
  cmdAdd("relay7no", relay7no);
  cmdAdd("relay8yes", relay8yes);
  cmdAdd("relay8no", relay8no);

  digitalWrite(relay1_pin, HIGH);
  digitalWrite(relay2_pin, HIGH);
  digitalWrite(relay3_pin, HIGH);
  digitalWrite(relay4_pin, HIGH);
  digitalWrite(relay5_pin, HIGH);
  digitalWrite(relay6_pin, HIGH);
  digitalWrite(relay7_pin, HIGH);
  digitalWrite(relay8_pin, HIGH);
}

void loop()
{
  cmdPoll();


}

// Blink the LED. This is an example of using command line arguments
// to call a function in a sketch.
// If a numeric arg is specified, then use that to set the 
// delay time. If called with no arguments, then turn the LED off.
//
// Usage: At the command line, to blink the LED, type:
// blink 100
// 
// This blinks the LED with a 100 msec on/off time. 
//
// Usage: At the command line, to turn off the LED, type:
// blink
//
// Calling the function with no arguments will turn off the LED
//
// Also, you'll notice that the function "cmdStr2Num" is needed. Since
// the numeric arg is stored as an ASCII string, it needs to be converted
// to an integer. When you call cmdStr2Num, you need to specify two arguments:
// 1) the numeric string to be converted
// 2) the numeric base that will be used to convert it,ie: 10 = decimal, 16 = hex
// RELAY 1 COMMAND
void relay1yes(int arg_cnt, char **args)
{
  Serial.println("she said yes!");
  digitalWrite(relay1_pin, LOW);
}

void relay1no(int arg_cnt, char **args)
{
  digitalWrite(relay1_pin, HIGH);
  Serial.println("she said no!");
}
//RELAY 2 COMMAND
void relay2yes(int arg_cnt, char **args)
{
  Serial.println("she said yes!");
  digitalWrite(relay2_pin, LOW);
}

void relay2no(int arg_cnt, char **args)
{
  digitalWrite(relay2_pin, HIGH);
  Serial.println("she said no!");
}

//RELAY 3 COMMAND
void relay3yes(int arg_cnt, char **args)
{
  Serial.println("she said yes!");
  digitalWrite(relay3_pin, LOW);
}

void relay3no(int arg_cnt, char **args)
{
  digitalWrite(relay3_pin, HIGH);
  Serial.println("she said no!");
}

//RELAY 4 COMMAND
void relay4yes(int arg_cnt, char **args)
{
  Serial.println("she said yes!");
  digitalWrite(relay4_pin, LOW);
}

void relay4no(int arg_cnt, char **args)
{
  digitalWrite(relay4_pin, HIGH);
  Serial.println("she said no!");
}

//RELAY 5 COMMAND
void relay5yes(int arg_cnt, char **args)
{
  Serial.println("she said yes!");
  digitalWrite(relay5_pin, LOW);
}

void relay5no(int arg_cnt, char **args)
{
  digitalWrite(relay5_pin, HIGH);
  Serial.println("she said no!");
}

//RELAY 6 COMMAND
void relay6yes(int arg_cnt, char **args)
{
  Serial.println("she said yes!");
  digitalWrite(relay6_pin, LOW);
}

void relay6no(int arg_cnt, char **args)
{
  digitalWrite(relay6_pin, HIGH);
  Serial.println("she said no!");
}

//RELAY 7 COMMAND
void relay7yes(int arg_cnt, char **args)
{
  Serial.println("she said yes!");
  digitalWrite(relay7_pin, LOW);
}

void relay7no(int arg_cnt, char **args)
{
  digitalWrite(relay7_pin, HIGH);
  Serial.println("she said no!");
}

//RELAY 8 COMMAND
void relay8yes(int arg_cnt, char **args)
{
  Serial.println("she said yes!");
  digitalWrite(relay8_pin, LOW);
}

void relay8no(int arg_cnt, char **args)
{
  digitalWrite(relay8_pin, HIGH);
  Serial.println("she said no!");
}
