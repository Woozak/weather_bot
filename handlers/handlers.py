from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.keyboards import geo_kb

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        text=f'Привет, <b>{message.from_user.first_name}</b>!\n'
             f'Отправь мне свою геолокацию, и я пришлю тебе погоду.', reply_markup=geo_kb
    )


@router.message(F.location)
async def location_message(message: Message):
    latitude = message.location.latitude
    longitude = message.location.longitude



@router.message()
async def other_messages(message: Message):
    await message.answer(
        text=f'Извини, но на данный момент я могу только присылать погоду в ответ на отправленную геолокацию.',
        reply_markup=geo_kb
    )
