from __future__ import print_function

import argparse
import io
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

# If modifying these scopes, delete the file token.json.
from googleapiclient.http import MediaIoBaseDownload


def main(file_id: str, output: str):
    creds = Credentials.from_service_account_file('credentials.json')
    service = build('drive', 'v3', credentials=creds)
    # Call the Drive v3 API
    request = service.files().export_media(fileId=file_id, mimeType='text/csv')
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    with open(output, 'wb') as fp:
        fp.write(fh.getbuffer())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_id', help='Google Drive CSV File ID')
    parser.add_argument('output', help='Output Path')
    args = parser.parse_args()
    print(f'Download Phrase CSV From {args.file_id}')
    main(args.file_id, args.output)
    print('End')
