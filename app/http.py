from typing import Optional


class Response:
    def __init__(self, data, status_code: Optional[int] = None):
        self.data = data
        self.status_code = status_code or 202


