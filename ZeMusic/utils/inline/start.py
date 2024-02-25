from pyrogram.types import InlineKeyboardButton

import config
from ZeMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=". aDD Me To Your Groups .", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=". Support .", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=". aDD Me To Your Groups .",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="**. AssistanT .**", callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text="- BoT OWNER .", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="- SUPPORT .", url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=". cHanneL Bot .", url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=". cL Source .", url=f"https://t.me/W_4_M"),
        ],
    ]
    return buttons
