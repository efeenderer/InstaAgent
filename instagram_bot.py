from instagrapi import Client
import os
from dotenv import load_dotenv
load_dotenv()




cl = Client()

account_username = os.environ.get("INSTAGRAM_USERNAME") 
account_password = os.environ.get("INSTAGRAM_PASSWORD")

cl.login(account_username,account_password)


target_id = cl.user_id_from_username(account_username)
medias = cl.user_medias_v1(target_id)

print(len(medias))



threads = cl.direct_threads()
print(f"Threads len: {len(threads)} many threads")

for thread in threads:
    print(f"Thread ID: {thread.id}  Thread Users: {[user.username for user in thread.users]}")

    for message in thread.messages:
        try:
            text = message.text if message.item_type == "text" else "Not a text"
            print(f"""Message id: {message.id}
Message user: {cl.username_from_user_id(message.user_id)}
Message Time: {message.timestamp}
Message Item type: {message.item_type}
Message Text: {text}
""")
        except Exception as e:
            print(f"Exception at message. Error : {e}")


for media in medias:

    print(f"Comment Count: {media.comment_count}")
    print(f"Caption Text: {media.caption_text}")
    print(f"Media Type: {media.media_type}")

    comments = cl.media_comments(media.id)

    for idx, comment in enumerate(comments):
        
        print(f"Comment {idx+1}: Comment text: {comment.text}, User: {comment.user.username}, UserID: {comment.user.pk}")





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


THREAD STRUCTURE

thread.pk                      : primary key of the thread  
thread.id                      : unique ID of the thread (can be same as pk)  
thread.messages                : list of DirectMessage objects in the thread  
thread.users                   : list of UserShort objects participating in the thread  
thread.inviter                 : UserShort object of the user who started the thread  
thread.last_activity_at        : timestamp of the last activity in the thread  
thread.thread_type             : type of the thread ('private', 'group', etc.)  
thread.thread_title            : title or display name of the thread  
thread.is_group                : whether the thread is a group chat  
thread.read_state              : integer value representing read state  
thread.shh_mode_enabled        : whether SHH (silent mode) is enabled  
thread.last_seen_at            : dictionary with user IDs as keys and last seen info as values  


MESSAGE STRUCTURE, thread.messages[]

message.id                     : message ID  
message.user_id                : sender’s user ID  
message.thread_id              : ID of the thread this message belongs to  
message.timestamp              : when the message was sent (datetime object)  
message.item_type              : type of message content ('text', 'xma_media_share', etc.)  
message.is_sent_by_viewer      : whether this message was sent by the logged-in user  
message.text                   : the actual message text (for text messages)  
message.reactions              : reactions (if any)  
message.reply                  : replied message object (if it's a reply)  
message.link                   : shared link (if any)  
message.animated_media         : animated media (GIF, etc.)  
message.media                  : media (photo or video, deprecated)  
message.visual_media           : ephemeral or visual media (e.g., disappearing photos)  
message.xma_share              : MediaXma object for shared Instagram post/story  
message.client_context         : internal context ID (used for debugging or tracking)

MEDIA XMA STRUCTURE, message.item_type == "xma_media_share"

message.xma_share.video_url            : shared Instagram post/video URL  
message.xma_share.title                : post caption/title text  
message.xma_share.preview_url          : thumbnail image of the post  
message.xma_share.preview_url_mime_type: MIME type of the preview image  
message.xma_share.header_icon_url      : profile picture of the post owner  
message.xma_share.header_icon_width    : width of header icon (usually 50)  
message.xma_share.header_icon_height   : height of header icon  
message.xma_share.header_title_text    : username or name of the content owner  
message.xma_share.preview_media_fbid   : Facebook media ID  


USER STRUCTURE (Inside thread.users[] or thread.inviter)

user.pk                        : user ID  
user.username                  : Instagram username  
user.full_name                 : full name of the user  
user.profile_pic_url           : profile picture URL (low-res or default)  
user.profile_pic_url_hd        : HD version of profile picture (may be None)  
user.is_private                : whether the account is private  


LAST SEEN STRUCTURE (Inside thread.last_seen_at[<user_id>])

last_seen.item_id              : ID of the last seen message by this user  
last_seen.timestamp            : timestamp when they last saw the thread  
last_seen.created_at           : timestamp of creation (usually same as timestamp)  
last_seen.shh_seen_state       : internal dict (typically empty)



"""


