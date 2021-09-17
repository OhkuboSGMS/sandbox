// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'model.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

PhraseList _$PhraseListFromJson(Map<String, dynamic> json) => PhraseList(
      header: Header.fromJson(json['header'] as Map<String, dynamic>),
      body: (json['body'] as List<dynamic>)
          .map((e) => Phrase.fromJson(e as Map<String, dynamic>))
          .toList(),
    );

Map<String, dynamic> _$PhraseListToJson(PhraseList instance) =>
    <String, dynamic>{
      'header': instance.header,
      'body': instance.body,
    };

Header _$HeaderFromJson(Map<String, dynamic> json) => Header(
      names: (json['names'] as List<dynamic>).map((e) => e as String).toList(),
      group: (json['group'] as Map<String, dynamic>).map(
        (k, e) => MapEntry(k, Group.fromJson(e as Map<String, dynamic>)),
      ),
    );

Map<String, dynamic> _$HeaderToJson(Header instance) => <String, dynamic>{
      'names': instance.names,
      'group': instance.group,
    };

Group _$GroupFromJson(Map<String, dynamic> json) => Group(
      words: (json['words'] as List<dynamic>).map((e) => e as String).toList(),
    );

Map<String, dynamic> _$GroupToJson(Group instance) => <String, dynamic>{
      'words': instance.words,
    };

Phrase _$PhraseFromJson(Map<String, dynamic> json) => Phrase(
      reference: json['reference'] as String,
      words: (json['words'] as List<dynamic>).map((e) => e as String).toList(),
      group: json['group'] as String,
      template: json['template'] as String,
    );

Map<String, dynamic> _$PhraseToJson(Phrase instance) => <String, dynamic>{
      'reference': instance.reference,
      'words': instance.words,
      'group': instance.group,
      'template': instance.template,
    };
