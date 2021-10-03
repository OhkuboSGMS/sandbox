import 'dart:io';

import 'package:args/args.dart';
import 'package:silly_phrase_bot/src/io.dart' as io;

void main(List<String> args) {
  final parser = ArgParser();
  parser.addOption('phrase');
  parser.addOption('default');

  final result = parser.parse(args);
  final phrase = result['phrase'] as String;
  final _default = result['default'] as String;
  final phraseFile = File(phrase);
  final defaultFile = File(_default);
  if (phraseFile.existsSync() && defaultFile.existsSync()) {
    print('Convert $phrase with $_default to json File');
    io.convert(phraseFile, defaultFile);
  } else {
    exitCode = 1;
  }
}
