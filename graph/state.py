from typing import TypedDict


class NewsState(TypedDict):
    topic: str
    news: list
    summary: str