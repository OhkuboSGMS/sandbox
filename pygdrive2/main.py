from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive


def login_with_service_account(credential_json_path: str):
    settings = {
        "client_config_backend": "service",
        "service_config": {
            "client_json_file_path": credential_json_path,
        }
    }
    gauth = GoogleAuth(settings=settings)
    gauth.ServiceAuth()
    return gauth


def upload_file_google_drive():
    auth = login_with_service_account('credentials.json')
    drive = GoogleDrive(auth)
    root_folder = '<folder_id>'
    # root_folderを親とするフォルダを取得
    file_list = drive.ListFile({'q': f"'{root_folder}' in parents"}).GetList()
    # このアカウントがアクセスできるすべてのフォルダを列挙
    query_folder = drive.ListFile({'q': f"mimeType = 'application/vnd.google-apps.folder'"}).GetList()
    for file1 in query_folder:
        print('title: {}, id: {}'.format(file1['title'], file1['id']))


if __name__ == '__main__':
    upload_file_google_drive()
