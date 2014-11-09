
// set some ping constants
const int usPin = 7;
const int irPin = A5;

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  pinMode(irPin, INPUT);
}

long get_US_distance()
{
  long duration;

  pinMode(usPin, OUTPUT);
  digitalWrite(usPin, LOW);
  delayMicroseconds(2);
  digitalWrite(usPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(usPin, LOW);

  pinMode(usPin, INPUT);
  duration = pulseIn(usPin, HIGH, 1000000);

  // convert the time into a distance
  return microsecondsToCentimeters(duration);
}

long get_IR_status()
{
  return analogRead(irPin);
}


void loop()
{
  // establish variables for duration of the ping, 
  // and the distance result in inches and centimeters:
  long US_distance, IR_status;

  US_distance = get_US_distance();

  IR_status = get_IR_status();

  Serial.print("<");
  Serial.print(IR_status>500?"False":"True");
  Serial.print(":");
  Serial.print(US_distance);
  Serial.println(">");

  delay(100);
}

long microsecondsToCentimeters(long microseconds)
{
  // The speed of sound is 340 m/s or 29 microseconds per centimeter.
  // The ping travels out and back, so to find the distance of the
  // object we take half of the distance travelled.
  return microseconds / 29 / 2;
}



