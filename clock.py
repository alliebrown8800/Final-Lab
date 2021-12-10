# Define pins
serialPin = 17;
latchPin = 27;
clockPin = 22;



void loop() {
  for (int i = 0; i <= 3; i++) { //cycles through all PWM pins
    for (int k = 0; k <= arrHeight; k++) { //cycles through countTo number of digArray rows
      analogWrite((pinArray[i]), 255); //turns PWM pin(i) on
      for (int h = 0; h <= digLoop; h++) { //how many times to cycle through columns
        for (int j = 0; j <= arrWidth; j++) { //cycles through all displayed column data
          digitalWrite(latchPin, HIGH);
          shiftOut(dataPin, clockPin, MSBFIRST, digArray[k][j]);
          digitalWrite(latchPin, LOW);
          delay(segSpeed); //delay until next segment displayed sequence
        }
      }
      analogWrite((pinArray[i]), 0); //turns PWM pin(i) off
      delay(nextPin); //delay until next displayed digit sequence
    }
  }
  delay(repeatSeq); //delay until everything is started over again
}