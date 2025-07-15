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
        
        print(f"Comment {idx+1}: Comment text: {comment.text}, User: {comment.user.username}, UserID: {comment.user.pk}")
        
        try:
            comment_comments = cl.media_comments(comment.pk)
            print(f"Comments of the comment: {comment_comments}")
        except:
            continue



"""
COMMENT STRUCTURE

comment.pk                      : comment ID  
comment.text                    : comment text  
comment.user                    : user data object  
comment.user.pk                 : user ID  
comment.user.username           : username of the commenter  
comment.user.full_name          : full name of the commenter  
comment.user.is_private         : whether the user account is private  
comment.user.profile_pic_url    : profile picture URL of the user  
comment.user.profile_pic_url_hd : high-definition profile picture URL (if available)  
comment.created_at_utc          : timestamp of when the comment was created (UTC)  
comment.content_type            : type of content (e.g., 'comment')  
comment.status                  : status of the comment (e.g., 'Active')  
comment.replied_to_comment_id   : ID of the parent comment, if it's a reply  
comment.has_liked               : whether the current user has liked this comment  
comment.like_count              : number of likes on the comment  

"""


