from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const


async def go_clicked(callback: CallbackQuery, button: Button,
                     manager: DialogManager):
    await callback.message.answer("Going on!")


async def run_clicked(callback: CallbackQuery, button: Button,
                      manager: DialogManager):
    await callback.message.answer("Running!")


row = Row(
    Button(Const("Go"), id="go", on_click=go_clicked),
    Button(Const("Run"), id="run", on_click=run_clicked),
    Button(Const("Fly"), id="fly"),
)
