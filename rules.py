import json
from typing import Union
from vkbottle.bot import Message
from vkbottle.dispatch.rules import ABCRule



class IsCommand(ABCRule[Message]):
    def __init__(self, command: str):
        self.command = command

    async def check(self, event: Message) -> bool:
        if event.text.startswith(f"/{self.command}") or event.text.startswith(f"!{self.command}"):
            return True
        return False