import 'dart:io';

import 'package:intl/date_symbol_data_local.dart';
import 'package:silly_phrase_bot/src/model.dart';
import 'package:test/test.dart';

void main() async {
  initializeDateFormatting();
  // File(CSV)をパースしてjsonに変換
  // jsonをstorageにアップロード
  // File をどこからかダウンロード
  // File(json)をパースしてデータをdartに取り込む
  test("Json -> PhraseManager", () async {
    final demoJson = File("demo.json");
    final pm = PhraseManager();
    await pm.process(demoJson);

    print(pm.groupDict);
    print(pm.groupWordDict);
  });
}
