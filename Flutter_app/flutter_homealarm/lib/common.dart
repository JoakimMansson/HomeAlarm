import 'package:flutter/material.dart';

/*------------------- Trigger and Alarm status ---------------------- */

class TriggerButton extends StatefulWidget {
  const TriggerButton({super.key});

  @override
  State<TriggerButton> createState() => _TriggerButtonState();
}

class _TriggerButtonState extends State<TriggerButton> {
  bool alarm_on = true;
  String path = "images/Secured.png";
  String last_armed = "";

  @override
  Widget build(BuildContext context) {
    return Center(
        child: Column(
      children: [
        Container(
            margin: const EdgeInsets.only(top: 30),
            child: Image(image: ResizeImage(AssetImage(path), width: 250, height: 250))
        ),
        Container(
          margin: const EdgeInsets.only(top: 20),
          child: const Text(
            "Disarmed 16:07",
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
        ),
        Container(
          margin: const EdgeInsets.only(top: 40),
          height: 60,
          width: 120,
          child: MaterialButton(
            onPressed: () {
              setState(() {
                UpdateAlarmState(alarm_on, path);
              });
            },
            child: const Text("Trigger"),
            shape: const StadiumBorder(),
            color: Colors.red,
          ),
        )
      ],
    ));
  }
}

void UpdateAlarmState(bool state, String path) {
  if (state == true) {
    state = false;
    path = "images/De-Secured.png";
  } else {
    path = "images/Secured.png";
  }
}


/*//////////////////////// Trigger and Alarm status /////////////////////// */