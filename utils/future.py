from protocol.server import ServerMessage


async def async_result(f) -> ServerMessage:
    await f
    return f.result()
