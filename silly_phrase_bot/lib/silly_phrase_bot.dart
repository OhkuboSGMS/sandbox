import 'dart:io';

import 'package:intl/date_symbol_data_local.dart';
import 'package:silly_phrase_bot/src/main.dart';

void main() async {
  initializeDateFormatting();
  // File(CSV)をパースしてjsonに変換
  // jsonをstorageにアップロード

  // File をどこからかダウンロード
  // File(json)をパースしてデータをdartに取り込む
  //
  final demoJson = File("demo.json");
  final dict = await parse(demoJson);

  print(dict!.keys.toList());
  print(dict.values.toList());
  for (var p in dict.values) {
    for (var pp in p) {
      print(pp.insert({"a": "帰省", "x": '延期', "y": "送別会"}));
    }
  }
}
