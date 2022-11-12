import 'package:flutter/material.dart';
import 'common.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  bool alarm_on = true;
  String path = "images/Active.png";

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        TriggerButton(),
      ],
    );
  }
}

void changeState(bool currentState, String path) {
  if (currentState == true) {
    currentState = false;
    path = "images/De-activated.png";
  } else {
    currentState = true;
    path = "images/Active.png";
  }
}
