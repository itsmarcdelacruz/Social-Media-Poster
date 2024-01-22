from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def youtube_authenticate():
    # Load client secrets and request access to YouTube API
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json', scopes=["https://www.googleapis.com/auth/youtube.upload"])
    credentials = flow.run_console()
    return build('youtube', 'v3', credentials=credentials)

def upload_short(youtube, file_path, title, description, category_id, tags):
    body = {
        'snippet': {
            'title': title,
            'description': description,
            'tags': tags,
            'categoryId': category_id
        },
        'status': {
            'privacyStatus': 'public'
        }
    }

    # The file format and the content type must match
    media = MediaFileUpload(file_path, mimetype='video/*')

    # Insert the video to YouTube and execute
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    response = request.execute()

    return response

if __name__ == "__main__":
    youtube = youtube_authenticate()
    file_path = 'path/to/your/short/video.mp4'
    title = 'Your Video Title'
    description = 'Your Video Description'
    category_id = '22'  # Choose the category ID that best suits your video
    tags = ['shorts', 'youtube', 'example']

    response = upload_short(youtube, file_path, title, description, category_id, tags)
    print(response)
