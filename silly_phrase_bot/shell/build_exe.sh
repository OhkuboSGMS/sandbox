pyinstaller upload/google_drive_csv.py --onefile
pyinstaller upload/upload_phrase_json.py --onefile
dart compile exe bin/silly_phrase_bot.dart

rm -rf build/