import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","مكس","سورس مكس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/1068724d97569bb1a4a35.jpg",
        caption=f""". 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝗧𝗼 𝗦𝗼𝘂𝗿𝗰𝗲 𝗺𝗶𝘅 .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- 𝗱𝗲𝘃 𝘀𝗼𝘂𝗿𝗰𝗲 .", url=f"https://t.me/P_T_I"), 
                    
                
                    InlineKeyboardButton(
                        ". 𝘀𝘂𝗽𝗽𝗼𝗿𝘁 .", url=f"https://t.me/LddfY"),
                ],[
                    
                
                    InlineKeyboardButton(
                        ". 𝘀𝗼𝘂𝗿𝗰𝗲 .", url=f"https://t.me/W_4_M"),
                
        ],

            ]

        ),

    )

