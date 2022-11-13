import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

import 'package:flutter_homealarm/Settings_page.dart';
import 'CCTV_page.dart';
import 'Home_page.dart';
import 'common.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  MyApp({super.key});
  Future<FirebaseApp> _fbApp = Firebase.initializeApp();

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        theme: ThemeData(
          primarySwatch: Colors.red,
        ),
        home: FutureBuilder(
            future: _fbApp,
            builder: (context, snapshot) {
              if (snapshot.hasError) {
                print("You have an error ${snapshot.error.toString()}");
                return Text("Firebase failed");
              } else if (snapshot.hasData) {
                print("Firebase initialization succeded");
                return RootPage();
              } else {
                return const Center(
                  child: CircularProgressIndicator(),
                );
              }
            }));
  }
}

class RootPage extends StatefulWidget {
  const RootPage({super.key});

  @override
  State<RootPage> createState() => _RootPageState();
}

class _RootPageState extends State<RootPage> {
  int current_index = 0;

  void changeActivePage(int index) {
    setState(() {
      current_index = index;
    });
  }

  List<Widget> pages = [];

  @override
  void initState() {
    pages = const [HomePage(), CCTVPage()];
    super.initState();
  }

  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: const Text("JSecure"),
        actions: [
          Padding(
            padding: EdgeInsets.only(right: 10),
            child: IconButton(
              icon: Icon(Icons.settings),
              color: Colors.black,
              onPressed: () {
                Navigator.of(context)
                    .push(MaterialPageRoute(builder: (BuildContext context) {
                  return const SettingsPage();
                }));
              },
            ),
          )
        ],
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const [
          BottomNavigationBarItem(icon: Icon(Icons.home), label: "Home"),
          BottomNavigationBarItem(
              icon: Icon(Icons.video_camera_front_sharp), label: "CCTV"),
        ],
        onTap: (int index) {
          setState(() {
            changeActivePage(index);
            current_index = index;
          });
        },
        currentIndex: current_index,
      ),
      body: pages[current_index],
    );
  }
}
