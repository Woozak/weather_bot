from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.keyboards import geo_kb
from weather import get_weather

router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        text=f'Привет, <b>{message.from_user.first_name}</b>!\n'
             f'Отправь мне свою геолокацию или название населенного пункта, '
             f'и я пришлю тебе погоду.', reply_markup=geo_kb
    )


@router.message(F.location)
async def location_message(message: Message):
    latitude = message.location.latitude
    longitude = message.location.longitude

    await message.answer(get_weather(latitude=latitude, longitude=longitude), reply_markup=geo_kb)


@router.message()
async def other_messages(message: Message):
    city = message.text

    await message.answer(get_weather(city=city), reply_markup=geo_kb)
