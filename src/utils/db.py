from tinydb import Query, TinyDB

db = TinyDB("db.json")
streamers_table = db.table("streamers")
commands_table = db.table("commands")


def init_db(streamers: list[str]):
    Streamer = Query()
    for streamer in streamers:
        if streamers_table.contains(Streamer.name == streamer):
            continue

        streamers_table.insert(
            {"name": streamer},
        )


def get_streamer_custom_commands(streamer: str) -> dict:
    Command = Query()
    return commands_table.get(Command.streamer == streamer)


def get_command(streamer: str, label: str) -> dict:
    Command = Query()
    return commands_table.get((Command.streamer == streamer) & (Command.label == label))


def add_custom_command(streamer: str, label: str, response: str):
    Command = Query()
    return commands_table.upsert(
        {"streamer": streamer, "label": label, "response": response},
        ((Command.streamer == streamer) & (Command.label == label)),
    )


def remove_custom_command(streamer: str, label: str):
    command = get_command(streamer, label)
    return commands_table.remove(doc_ids=[command.doc_id])


def custom_command_exists(streamer: str, label: str) -> bool:
    return bool(get_command(streamer, label))


def get_custom_command_response(streamer: str, label: str) -> str | None:
    return get_command(streamer, label).get("response")
