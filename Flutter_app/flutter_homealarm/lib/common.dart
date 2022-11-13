import 'package:flutter/material.dart';

/*------------------- Trigger and Alarm status ---------------------- */



void UpdateAlarmState(bool state, String path) {
  if (state == true) {
    state = false;
    path = "images/De-Secured.png";
  } else {
    path = "images/Secured.png";
  }
}


/*//////////////////////// Trigger and Alarm status /////////////////////// */