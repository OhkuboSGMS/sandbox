import 'dart:convert';
import 'dart:io';

import 'package:json_annotation/json_annotation.dart';
import 'package:template_string/template_string.dart';

part 'model.g.dart';

class PhraseManager {
  late PhraseList phraseList;
  Map<String, List<Phrase>> groupDict = {};
  Map<String, List<String>> groupWordDict = {};


  Future<PhraseManager> _process(dynamic json) async{
    try {
      phraseList = PhraseList.fromJson(json);
      final groupName = phraseList.header.names;
      groupDict.clear();
      groupWordDict.clear();
      for (var phrase in phraseList.body) {
        if (!groupName.contains(phrase.group)) {
          throw FormatException('Group[${phrase.group}]はグループリストに含まれていません');
        }
        if (groupDict[phrase.group] == null) {
          groupDict[phrase.group] = [];
          groupWordDict[phrase.group] = [];
        }
        groupDict[phrase.group]!.add(phrase);
        for (var word in phrase.words) {
          if (!groupWordDict[phrase.group]!.contains(word)) {
            groupWordDict[phrase.group]?.add(word);
          }
        }
      }
    } on Exception catch (e) {
      print(e);
    }
    return this;
  }
  //jsonFileからデータを生成
  Future<PhraseManager> process(File jsonFile) async {
    return _process(jsonDecode(jsonFile.readAsStringSync()));
  }
  ///jsonのStringから生成
  Future<PhraseManager> processFromJsonStr(String jsonStr)async{
    return _process(jsonDecode(jsonStr));
  }
}

@JsonSerializable()
class PhraseList {
  final Header header;
  final List<Phrase> body;

  PhraseList({
    required this.header,
    required this.body,
  });

  factory PhraseList.fromJson(Map<String, dynamic> json) =>
      _$PhraseListFromJson(json);

  Map<String, dynamic> toJson() => _$PhraseListToJson(this);
}

@JsonSerializable()
class Header {
  final List<String> names;
  final Map<String, Group> group;

  Header({required this.names, required this.group});

  factory Header.fromJson(Map<String, dynamic> json) => _$HeaderFromJson(json);

  Map<String, dynamic> toJson() => _$HeaderToJson(this);
}

@JsonSerializable()
class Group {
  Map<String, String> words;

  Group({required this.words});

  factory Group.fromJson(Map<String, dynamic> json) => _$GroupFromJson(json);

  Map<String, dynamic> toJson() => _$GroupToJson(this);
}

@JsonSerializable()
class Phrase {
  final String reference;
  final List<String> words;
  final String group;
  final String template;

  Phrase(
      {required this.reference,
      required this.words,
      required this.group,
      required this.template});

  Phrase.none()
      : reference = 'None',
        words = [],
        group = 'None',
        template = 'None'; // 設定されているワードに注意してテンプレート分を生成
  String insert(Map<String, String> word) {
    if (!this.words.every((e) => word.keys.contains(e))) {
      return 'Not Enough Words ${this.words}';
    }
    try {
      return template.insertTemplateValues(word);
    } on Exception catch (e) {
      return e.toString();
    }
  }

  factory Phrase.fromJson(Map<String, dynamic> json) => _$PhraseFromJson(json);

  Map<String, dynamic> toJson() => _$PhraseToJson(this);

  @override
  String toString() {
    return 'Phrase{reference: $reference, words: $words, group: $group, template: $template}';
  }
}
