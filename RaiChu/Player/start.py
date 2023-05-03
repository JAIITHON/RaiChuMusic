from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaiChu.config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from Process.filters import other_filters2
from time import time
from Process.filters import command
from datetime import datetime
from Process.decorators import authorized_users_only

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 ** 2 * 24),
    ("hour", 60 ** 2),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""اهلا {message.from_user.mention()}, My name is {BOT_NAME}.
بيك يصحبي انا بوت شغل اغاني ف رومات الطيزجرام لو مزاجك وحش وعاوز تشغل اغاني ضفني ف رومك وروق ع مزاجك ومتاح سماع سكس. عشان مزاجك يظبط اكترر 
.
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [                   
                    InlineKeyboardButton(
                        "الاوامر❔", callback_data="cbbasic"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        " الشرح❓", callback_data="cbhowtouse"
                    ),
                  ],[
                    InlineKeyboardButton(
                       "قناة البوت", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                    InlineKeyboardButton(
                       "جروب البوت", url=f"https://t.me/{GROUP_SUPPORT}"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕ ضفني في جروباك ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["repo", "source"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f01f58c3d9b187ae1d8a1.jpg",
        caption=f"""Here Is The Source Code Fork And Give Stars ✨""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ʀᴇᴘᴏ ⚒️", url=f"مفيش يكسمك")
                ]
            ]
        ),
    )
