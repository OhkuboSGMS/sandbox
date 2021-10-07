# About 
 迷言に単語を当てはめて新しい迷言を作る

## Develop

### json_serializable
`flutter pub run build_runner build  --delete-conflicting-outputs`

### create CLI App
`dart compile exe bin\silly_phrase_bot.dart`

#### execute CLI
'bin/silly_phrase_bot '

### Create Python bin

#### Download CSV From Google Drive
`pyinstaller upload/google_drive_csv.py --onefile`

#### Upload Json to Firebase Cloud Storage
`pyinstaller upload/upload_phrase_json.py --onefile`

### フレーズの作成

1. CSVにフレーズを追加する ✅
2. CSVをダウンロードする ✅
2. CSVをアプリ用jsonに変換する ✅
3. CLIとして作成 ✅
4. jsonをファイルAPIアップロードする ✅

## Reference
google_driveにサービスアカウントキーから認証無しでアクセス

https://playwithgoogleapi.hatenablog.com/entry/2019/06/30/133415
アカウントについて
https://qiita.com/t-yotsu/items/5d3d36847fbc71b72b76

## TODO
dart python の依存関係の自動化