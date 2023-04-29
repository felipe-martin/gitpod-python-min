import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Ruta al archivo de credenciales
creds_path = '/workspace/gitpod-python-min/credencial.json'
# Obtener la ID del video de YouTube que deseas transcribir
video_id = 'PHr8xPBhHJU'

# Cargar las credenciales de autenticación desde el archivo JSON
creds = service_account.Credentials.from_service_account_file(creds_path, scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])

# Crear un cliente de YouTube Data API
youtube = build('youtube', 'v3', credentials=creds)

# Obtener la URL de la transcripción del video
captions = youtube.captions().list(
    part='id', videoId=video_id
).execute()

caption_id = captions['items'][0]['id']

caption_url = youtube.captions().download(
    id=caption_id
).execute()['downloadUrl']

# Descargar la transcripción del video
import requests
from bs4 import BeautifulSoup

response = requests.get(caption_url)
soup = BeautifulSoup(response.text, 'xml')
transcript = soup.find_all('text')

# Imprimir la transcripción
for text in transcript:
    print(text.get_text())
