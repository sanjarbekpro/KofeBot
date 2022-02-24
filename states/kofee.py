from aiogram.dispatcher.filters.state import State, StatesGroup
from numpy import product

class Kofee(StatesGroup):
    category=State()
    product=State()
    amaunt=State()

