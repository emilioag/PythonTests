from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from script.gdrive_credentials import get_credentials
import click


@click.group()
def main():
    """gdrive."""
    pass


@main.command()
@click.option('--file', '-f', help="file name", required=True)
@click.option('--credentials-file', '-c', help="Credentials file name", required=True)
def upload(file, credentials_file):
    service = build('drive', 'v3', credentials=get_credentials(credentials_file))

    media = MediaFileUpload(file)

    file_name = file.split('/')[-1]

    service.files().create(body={'name': file_name}, media_body=media, fields='id').execute()


if __name__ == '__main__':
    main()
