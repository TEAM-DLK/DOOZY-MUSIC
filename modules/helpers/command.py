from typing import Union, List
from pyrogram import filters

other_filters = filters.group & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded
other_filters2 = filters.private & ~ filters.edited & ~ filters.via_bot & ~ filters.forwarded


def commandpro(commands: Union[str, List[str]]):
    return filters.command(commands,"")

def commandproo(commands: Union[str, List[str]]):
    return filters.command(commands1,"")

def commandprooo(commands: Union[str, List[str]]):
    return filters.command(commands2,"")
