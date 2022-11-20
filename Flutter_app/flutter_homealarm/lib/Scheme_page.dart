import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:flutter_time_picker_spinner/flutter_time_picker_spinner.dart';

class SchemePage extends StatefulWidget {
  const SchemePage({super.key});

  @override
  State<SchemePage> createState() => _SchemePageState();
}

class _SchemePageState extends State<SchemePage> {
  DateTime _dateTime = DateTime.now();

  String startTime = "00:00";
  String endTime = "00:00";


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: const Text("Scheme"),
        leading: IconButton(
          icon: const Icon(Icons.arrow_back_ios),
          onPressed: () {
            Navigator.of(context).pop();
          },
        ),
      ),
      body: Column(
        children: [
          Container(
              margin: const EdgeInsets.only(
                top: 30,
              ),
              child: Text("Your scheduled time: $startTime")),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                  margin: const EdgeInsets.symmetric(horizontal: 40, vertical: 20),
                  child: TimePickerSpinner(
                    is24HourMode: true,
                    normalTextStyle:
                        const TextStyle(fontSize: 24, color: Colors.lime),
                    highlightedTextStyle:
                        const TextStyle(fontSize: 24, color: Colors.black),
                    spacing: 20,
                    itemHeight: 80,
                    isForce2Digits: true,
                    onTimeChange: (time) {
                      setState(() {
                        setStartTime(time);
                      });
                    },
                  )),
              Container(
                  margin: const EdgeInsets.symmetric(horizontal: 40, vertical: 20),
                  child: TimePickerSpinner(
                    is24HourMode: true,
                    normalTextStyle:
                        const TextStyle(fontSize: 24, color: Colors.blue),
                    highlightedTextStyle:
                        const TextStyle(fontSize: 24, color: Colors.black),
                    spacing: 20,
                    itemHeight: 80,
                    isForce2Digits: true,
                    onTimeChange: (time) {
                      setState(() {
                        setEndTime(time);
                      });
                    },
                  )),
            ],
          ),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Container(
                margin: const EdgeInsets.symmetric(horizontal: 50),
                child: Text(
                  startTime,
                  textScaleFactor: 3,
                  style: const TextStyle(color: Colors.lime),
                ),
              ),
              Container(
                margin: const EdgeInsets.symmetric(horizontal: 25),
                child: Text(
                  endTime,
                  textScaleFactor: 3,
                  style: TextStyle(color: Colors.blue),
                ),
              ),
            ],
          ),
          Container(
              margin: const EdgeInsets.only(top: 70),
              height: 80,
              width: 150,
              child: MaterialButton(
                onPressed: () {
                  print("Set schedule");
                },
                shape: const StadiumBorder(),
                color: Colors.blueGrey,
                child: const Text("Set scheme"),
              )
          ),
          Container(
              margin: const EdgeInsets.only(top: 50),
              height: 50,
              width: 150,
              child: MaterialButton(
                onPressed: () {
                  print("Removing scheme");
                },
                shape: BeveledRectangleBorder(
                  borderRadius: BorderRadius.circular(12),
                ),
                color: Colors.red,
                child: const Text("Remove scheme"),
              )
          ),

        ],
      ),
    );
  }

  void updateFirebase() {
    final docUser =
        FirebaseFirestore.instance.collection("collectionPath").doc("");

    //docUser.update(data)
  }

  /* 
  Adds a 0 infront of hour or minute 
  if they are < 10                 
  */
  void setStartTime(DateTime time) {
    String setHour = "";
    String setMinute = "";

    if (time.hour.toInt() < 10) {
      setHour = "0" + time.hour.toString();
    } else {
      setHour = time.hour.toString();
    }

    if (time.minute.toInt() < 10) {
      setMinute = "0" + time.minute.toString();
    } else {
      setMinute = time.minute.toString();
    }

    startTime = "$setHour:$setMinute";
  }

  setEndTime(DateTime time) {
    String setHour = "";
    String setMinute = "";

    if (time.hour.toInt() < 10) {
      setHour = "0" + time.hour.toString();
    } else {
      setHour = time.hour.toString();
    }

    if (time.minute.toInt() < 10) {
      setMinute = "0" + time.minute.toString();
    } else {
      setMinute = time.minute.toString();
    }
  }
}
