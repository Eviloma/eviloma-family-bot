import os
from minio import Minio
import requests

async def sendProfilePhoto(message, bot):
    token = os.getenv("TOKEN")
    photos = await bot.get_user_profile_photos(message.from_user.id)
    if photos.total_count > 0:
        photo = photos.photos[0][-1]
        file_id = photo.file_id
        file_path = (await bot.get_file(file_id)).file_path
        file_url = f'https://api.telegram.org/file/bot{token}/{file_path}'
        
        if file_url == None:
            return None
        
        if not os.path.exists('TelegramBot/UsersAvatars/tmp'):
            os.makedirs('TelegramBot/UsersAvatars/tmp')
            
        try:    
            response = requests.get(file_url)
            if response.status_code == 200:
                _, file_extension = os.path.splitext(file_path)
                file_name = f"{message.from_user.id}{file_extension}"
                file_path = os.path.join('TelegramBot/UsersAvatars/tmp', file_name)
                with open(file_path, 'wb') as f:
                    f.write(response.content)
        except:
            print('[TelegramBot]: Error download and save Telegram profile photo')
            return None
        
        try:
            access_key = os.getenv("UPLOAD_PHOTO_ACCESS_KEY")
            secret_key = os.getenv("UPLOAD_PHOTO_SECRET_KEY")
            
            client = Minio("s3.eviloma.org", access_key, secret_key)
            
            source_file = f'TelegramBot/UsersAvatars/tmp/{file_name}'
            
            bucket_name = 'telegram'
            destination_file = file_name
            
            found = client.bucket_exists(bucket_name)
            if not found:
                client.make_bucket(bucket_name)
            
            client.fput_object(
                bucket_name, destination_file, source_file,
            )
            
            if os.path.exists(source_file):
                os.remove(source_file)
        except:    
            print('[TelegramBot]: Error upload and delete Telegram profile photo')
            return None

    return None