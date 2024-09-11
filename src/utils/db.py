from abc import ABC, abstractmethod

from tinydb import Query, TinyDB


class ProviderInterface(ABC):

    @abstractmethod
    def get_command(self, streamer, label) -> dict:
        pass

    @abstractmethod
    def add_custom_command(self, streamer: str, label: str, response: str) -> list[int]:
        pass

    @abstractmethod
    def get_streamer_custom_commands(self, streamer: str) -> dict:
        pass

    @abstractmethod
    def remove_custom_command(self, streamer: str, label: str) -> list[int]:
        pass

    @abstractmethod
    def custom_command_exists(self, streamer: str, label: str) -> bool:
        pass

    @abstractmethod
    def get_custom_command_response(self, streamer: str, label: str) -> str | None:
        pass

    @abstractmethod
    def get_streamers(self) -> list[str]:
        pass

    @abstractmethod
    def add_streamer(self, streamer: str):
        pass


class Database:
    def __init__(
        self,
        provider: ProviderInterface,
    ) -> None:
        self.provider = provider

    def populate_streamers(self, streamers: list[str]):
        existing_streamers = self.provider.get_streamers()
        for streamer in streamers:
            if streamer not in existing_streamers:
                self.provider.add_streamer(streamer)

    def get_streamer_custom_commands(self, streamer: str):
        return self.provider.get_streamer_custom_commands(streamer)

    def get_command(self, streamer: str, label: str):
        return self.provider.get_command(streamer, label)

    def add_custom_command(self, streamer: str, label: str, response: str):
        return self.provider.add_custom_command(streamer, label, response)

    def remove_custom_command(self, streamer: str, label: str):
        return self.provider.remove_custom_command(streamer, label)

    def custom_command_exists(self, streamer: str, label: str):
        return self.provider.custom_command_exists(streamer, label)

    def get_custom_command_response(self, streamer: str, label: str):
        return self.provider.get_custom_command_response(streamer, label)


class TinyDatabase(ProviderInterface):
    def __init__(self, filename: str) -> None:
        self.db = TinyDB(filename)
        self.streamers_table = self.db.table("streamers")
        self.commands_table = self.db.table("commands")

    def add_streamer(self, streamer: str):
        self.streamers_table.insert(
            {"name": streamer},
        )

    def get_streamers(self) -> list[str]:
        return [streamer.get("name", "None") for streamer in self.streamers_table.all()]

    def get_streamer_custom_commands(self, streamer: str) -> dict:
        Command = Query()
        return self.commands_table.search(Command.streamer == streamer)

    def get_command(self, streamer: str, label: str) -> dict:
        Command = Query()
        return self.commands_table.get(
            (Command.streamer == streamer) & (Command.label == label)
        )

    def add_custom_command(self, streamer: str, label: str, response: str):
        Command = Query()
        return self.commands_table.upsert(
            {"streamer": streamer, "label": label, "response": response},
            ((Command.streamer == streamer) & (Command.label == label)),
        )

    def remove_custom_command(self, streamer: str, label: str):
        command = self.get_command(streamer, label)
        return self.commands_table.remove(doc_ids=[command.doc_id])

    def custom_command_exists(self, streamer: str, label: str) -> bool:
        return bool(self.get_command(streamer, label))

    def get_custom_command_response(self, streamer: str, label: str) -> str | None:
        return self.get_command(streamer, label).get("response")
