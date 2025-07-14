from instagrapi import Client
import os
from dotenv import load_dotenv
load_dotenv()


account_username = os.environ.get("INSTAGRAM_USERNAME") 
account_password = os.environ.get("INSTAGRAM_PASSWORD") 

cl = Client()

cl.login(account_username,account_password)


target_id = cl.user_id_from_username(account_username)
medias = cl.user_medias_v1(target_id)

print(len(medias))


for media in medias:
    print(f"Comment Count: {media.comment_count}")
    print(f"Caption Text: {media.caption_text}")
    print(f"Media Type: {media.media_type}")
    comments = cl.media_comments(media.id)
    for idx, comment in enumerate(comments):
        print(f"Comment {idx+1}: {comment}")




