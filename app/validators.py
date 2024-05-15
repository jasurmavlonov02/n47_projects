from app.erros import BadRequestError
from app.models import User


def check_validators(user: User):
    if not user.username:
        return BadRequestError('Username is required')
    if not user.password:
        return BadRequestError('Password is required')
