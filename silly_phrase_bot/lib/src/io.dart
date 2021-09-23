import 'dart:convert';
import 'dart:io';

import 'package:csv/csv.dart';
import 'package:path/path.dart' as p;
import 'package:silly_phrase_bot/src/model.dart';
import 'package:template_string/src/template.dart';
import 'package:template_string/template_string.dart';
import 'package:yaml/yaml.dart';

// Map<String, Map<String, String>>
dynamic loadDefaultYaml(File yamlFile) {
  final yaml = loadYaml(yamlFile.readAsStringSync());
  return yaml;
}

Map<String, String> loadDefaultWord(dynamic yaml, String group) {
  if (yaml[group] == null) {
    throw Exception('Not Found Key =$group in Default YAML');
  }
  return Map<String, String>.from(yaml[group]
      .map((k, v) => MapEntry<String, String>(k as String, v as String)));
}

Map<String, dynamic> csvToJson(File csvFile, dynamic yaml) {
  final rows = CsvToListConverter().convert(csvFile.readAsStringSync());

  // グループの一覧
  final groupSet = <String>{}; // Set の書き方
  // 各グループの単語のセット
  final groupWordSet = <String, Set<String>>{}; // Map<String,Set<String>>

  final phraseList = <Phrase>[];
  for (var row in rows.getRange(1, rows.length)) {
    if (row.length <= 1) continue;
    final group = (row[0] as String).trim();
    groupSet.add(group);
    final ref = (row[1] as String).trim();

    final template = (row[2] as String).trim();
    final groupWords = StringTemplate.regExp.allMatches(template);
    // whereType :特定の型の値だけ取り出す
    final words =
        groupWords.map((e) => e.group(1)).whereType<String>().toList();
    for (var w in words) {
      // KeyにValueが無ければ()=>{}で初期化,wordを追加
      groupWordSet.putIfAbsent(group, () => {}).add(w);
    }
    phraseList.add(Phrase(
        reference: ref,
        words: Set<String>.from(words).toList(),
        group: group,
        template: template));

    // print("$group,$ref,$template");
  }
  return PhraseList(
          header: Header(
              names: groupSet.toList(),
              group: groupWordSet.map((key, value) => MapEntry<String, Group>(
                  key, Group(words: loadDefaultWord(yaml, key))))),
          body: phraseList)
      .toJson();
}

void convert(File phraseFile, File defaultFile) {
  final yamlFile = defaultFile;
  final yaml = loadDefaultYaml(yamlFile);

  final file = phraseFile;
  final json = csvToJson(file, yaml);
  final name = p.basenameWithoutExtension(phraseFile.path);
  final output_path = p.setExtension(name, ".json");
  File(output_path).writeAsString(JsonEncoder.withIndent("  ").convert(json));
}
