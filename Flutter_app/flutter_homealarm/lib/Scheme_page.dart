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
              child: Text("Your scheduled time: ${setHour}:${setMinute}")),
          Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                  margin: const EdgeInsets.only(top: 20, right: 40),
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
                  margin: const EdgeInsets.only(top: 20, left: 40),
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
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Container(
                margin: const EdgeInsets.only(top: 10, right: 20),
                child: Text(
                  startTime,
                  textScaleFactor: 4,
                  style: const TextStyle(color: Colors.lime),
                ),
              ),
              Container(
                margin: const EdgeInsets.only(top: 10, left: 20),
                child: Text(
                  endTime,
                  textScaleFactor: 4,
                  style: TextStyle(color: Colors.blue),
                ),
              ),
            ],
          ),
          Container(
              margin: const EdgeInsets.only(top: 50),
              height: 80,
              width: 150,
              child: MaterialButton(
                onPressed: () {
                  print("Set schedule");
                },
                shape: const StadiumBorder(),
                color: Colors.grey,
                child: const Text("Set scheme"),
              ))
        ],
      ),
    );
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
