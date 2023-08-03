from pywebio.input import input as pw_input
from pywebio.output import put_success, toast
from pywebio.output import popup

user_favorite_food = pw_input('Ask your favorite food')

smile = '\U0001F354'

toast(f'Oh, I like {user_favorite_food} {smile} too')
