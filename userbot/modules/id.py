from PIL import Image, ImageDraw, ImageFont
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.id")
async def image_maker(event):
    id = "".join(event.raw_text.split(maxsplit=2)[1:])
    user = await event.get_reply_message()
    chat = event.input_chat
    if user:
        await event.client.get_profile_photos(user.sender)
    else:
        await event.client.get_profile_photos(chat)
        await event.client.download_profile_photo(user,
                                                  file="user.png", download_big=True
                                                  )
        user_photo = Image.open("user.png")
        id_template = Image.open("userbot/resources/FrameID.png")
        user_photo = user_photo.resize((989, 1073))
        id_template.paste(user_photo, (1229, 573))
        position = (2473, 481)
        draw = ImageDraw.Draw(id_template)
        color = "rgb(23, 43, 226)"  # red color
        font = ImageFont.truetype("userbot/resources/fontx.ttf", size=200)
        draw.text(
            position,
            user.sender.first_name.replace("\u2060", ""),
            fill=color,
            font=font,
        )
        id_template.save("user_id.png")
        await event.edit("`Membuat ID Card..`")
        await event.client.send_file(
            event.chat_id,
            "Generated User ID",
            reply_to=event.message.reply_to_msg_id,
            file="user_id.png",
            force_document=False,
            silent=True,
        )
        await event.delete()


CMD_HELP.update(
    {
        "id": ">`.id`\
        \nUsage: Reply to a user to generate ID Card."
    }
)
