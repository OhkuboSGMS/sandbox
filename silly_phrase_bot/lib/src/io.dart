import 'dart:io';

import 'package:csv/csv.dart';

void csvToJson(File csvFile) {
  final rows = CsvToListConverter().convert(csvFile.readAsStringSync());

  for (var row in rows) {
    final group = (row[0] as String).trim();
    final ref = (row[1] as String).trim();
    final phrase = (row[2] as String).trim();
    print("$group,$ref,$phrase");
  }
}

void main() {
  final file = File("phrase.csv");
  print(file);
  csvToJson(file);
}
