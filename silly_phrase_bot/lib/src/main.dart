import 'dart:async';
import 'dart:convert';
import 'dart:io';

import 'package:silly_phrase_bot/src/model.dart';

Future<Map<String, List<Phrase>>?> parse(File jsonFile) async {
  try {
    final phraseList =
        PhraseList.fromJson(jsonDecode(jsonFile.readAsStringSync()));
    final groupName = phraseList.header.names;
    final groupDict = <String, List<Phrase>>{};

    for (var phrase in phraseList.body) {
      if (!groupName.contains(phrase.group)) {
        throw FormatException('Group[${phrase.group}]はグループリストに含まれていません');
      }
      if(groupDict[phrase.group]==null){
        groupDict[phrase.group] =[];
      }
      groupDict[phrase.group]!.add(phrase);
    }
    return groupDict;
  } on Exception catch (e) {
    print(e);
    return null;
  }
}
