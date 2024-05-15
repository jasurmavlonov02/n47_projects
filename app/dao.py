import json
from app.models import User
from app.utils import generate_id
from app.http import Response

filename = 'db/users.json'


def read_all_users(filename: str):
    try:
        with open(filename) as f:
            user_list = json.load(f)
        return user_list
    except FileNotFoundError as e:
        return e


def create_user(user: User):
    users: dict = read_all_users(filename)
    with open(filename, 'w') as f:
        users[user.user_id] = user.__dict__
        json.dump(users, f, indent=4)
        return Response('User Successfully created')


user = User(username='Jake', password='123!@#', user_id=generate_id())

create_user(user)


def read_user(user_id: str):
    users = read_all_users(filename)
    for _id, user_data in users.items():
        if _id == user_id:
            return user_data
    raise Exception(f'User {user_id} => not found')

# print(read_user('101'))
# update, delete
