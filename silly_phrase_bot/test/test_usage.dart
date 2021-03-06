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
    final phrase = pm.groupDict['japan_politics']![0];
    final word = pm.groupWordDict['japan_politics'];
    final map = Map.fromEntries(word!.map((e) => MapEntry(e, "Test")));
    final template =phrase.insert(map);
    print(template);

    final phrases = pm.groupDict['japan_politics'];
    final allPhrase =phrases.insertWordAll(map);
    assert(allPhrase.length == 1);
    print(allPhrase);
  });
}
