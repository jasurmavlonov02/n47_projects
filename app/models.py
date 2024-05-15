from datetime import datetime
from typing import Optional
from app.enums import Language


class User:
    def __init__(self,

                 username: str,
                 password: str,
                 user_id: str,
                 email: Optional[str] = None,
                 language: Optional[Language] = None,
                 is_active: bool = False,
                 created_at: Optional[datetime] = None):

        self.username = username
        self.password = password
        self.user_id = user_id
        self.email = email
        self.language = language or Language.English.value
        self.is_active = is_active
        self.created_at = created_at or str(datetime.now())



