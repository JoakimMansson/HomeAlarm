import 'dart:math';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:flutter_homealarm/CCTV_page.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:flutter_homealarm/Scheme_page.dart';
import 'common.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  bool alarm_on = true;
  String path = "images/Secure.png";
  String last_armed = "";
  final DatabaseReference _testRef =
      FirebaseDatabase.instance.ref().child("test");

  @override
  Widget build(BuildContext context) {
    return Center(
        child: Column(
      children: [
        Container(
            margin: const EdgeInsets.only(top: 50),
            child: Image(
                image: ResizeImage(AssetImage(path), width: 250, height: 250))),
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
          width: 160,
          child: MaterialButton(
            onPressed: () {
              print("Update DB");
              updateDB(startSignal: true);
              setState(() {
                UpdateAlarmState();
              });
            },
            child: const Text("Trigger"),
            shape: const StadiumBorder(),
            color: Colors.red,
          ),
        ),
        Container(
          margin: const EdgeInsets.only(top: 50),
          height: 60,
          width: 100,
          child: MaterialButton(
            onPressed: (){
              Navigator.of(context)
                    .push(MaterialPageRoute(builder: (BuildContext context) {
                  return const SchemePage();
                }));
            },
            child: const Text("Scheme"),
            shape: const StadiumBorder(),
            color: Colors.grey,
          )
        )
      ],
    ));
  }

  Future updateDB({required bool startSignal}) async {
    final docuser = FirebaseFirestore.instance.collection("users").doc("test1");

    final json = {"start_alarm": startSignal};

    await docuser.set(json);
  }

  void UpdateAlarmState() {
    if (alarm_on == true) {
      alarm_on = false;
      path = "images/Insecure.png";
    } else {
      alarm_on = true;
      path = "images/Secure.png";
    }
  }
}
