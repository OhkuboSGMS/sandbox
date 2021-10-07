from __future__ import print_function

import argparse
import io
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# If modifying these scopes, delete the file token.json.
from googleapiclient.http import MediaIoBaseDownload


def main(csv_file_id: str, default_file_id: str):
    creds = Credentials.from_service_account_file('credentials.json')
    service = build('drive', 'v3', credentials=creds)
    # Call the Drive v3 API
    request = service.files().export_media(fileId=csv_file_id, mimeType='text/csv')
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    with open('phrase.csv', 'wb') as fp:
        fp.write(fh.getbuffer())

    request = service.files().get_media(fileId=default_file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    with open('default.yaml', 'wb') as fp:
        fp.write(fh.getbuffer())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv_file_id', default='1ZapCTVCSiqmWmO8BFf0goVz2s5llVji-VhU-HwavWrY',
                        help='Google Drive CSV File ID')
    parser.add_argument('--default_file_id', default='1kCfADDpoz6XdsHihB8zMriBZAPcntKNs')
    args = parser.parse_args()
    print(f'Download Phrase CSV From {args.csv_file_id} Default Yaml From {args.default_file_id}')
    main(args.csv_file_id, args.default_file_id)
    print('End')
