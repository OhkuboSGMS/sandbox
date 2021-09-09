import 'package:intl/date_symbol_data_local.dart';
import 'package:template_string/template_string.dart';
import 'dart:io';
void main() async{
  initializeDateFormatting();
  final phraseFile = File("phrase.txt");
  final phrases =phraseFile.readAsLinesSync();
  for(var line in phrases){
    print(line.insertTemplateValues({'x':'中止','y':'うんち','z':'コロナ','a':'テスト'}));
  }
}