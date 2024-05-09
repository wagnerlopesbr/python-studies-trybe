from typing import Protocol, Tuple
from queue import Queue


class MessagingProtocol(Protocol):
    def send_message(self, to: str, message: str) -> bool:
        ...
    
    def receive_message(self) -> Tuple[str, str] | None:
        ...


class InMemoryMessaging(MessagingProtocol):
    def __init__(self) -> None:
        self.messages: Queue[Tuple[str, str]] = Queue()
    
    def send_message(self, to: str, message: str) -> bool:
        self.messages.put((to, message))
        return True

    def receive_message(self) -> Tuple[str, str] | None:
        if self.messages.empty():
            return None
        return self.messages.get()


class FileMessaging(MessagingProtocol):
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
    
    def send_message(self, to: str, message: str) -> bool:
        with open(self.file_name, "a") as f:
            f.write(f"{to}:{message}\n")
        return True
    
    def receive_message(self) -> Tuple[str, str] | None:
        with open(self.file_name, "r") as f:
            lines = f.readlines()
            if not lines:
                return None
            line = lines[0]
            with open(self.file_name, "w") as f:
                f.writelines(lines[1:])
            return line.split(":")[0], line.split(":")[1].split("\n")[0]


def main() -> None:
    in_memory_messaging = InMemoryMessaging()
    file_messaging = FileMessaging("messages.txt")
    in_memory_messaging.send_message("Alice", "Hello Bob")
    in_memory_messaging.send_message("Bob", "Hello Alice")
    in_memory_messaging.send_message("Alice", "How are you?")
    in_memory_messaging.send_message("Bob", "I'm fine")
    file_messaging.send_message("Carla", "Hello David")
    file_messaging.send_message("David", "Hello Carla")
    file_messaging.send_message("Carla", "How are you?")
    file_messaging.send_message("David", "I'm fine")
    print(in_memory_messaging.receive_message())
    print(in_memory_messaging.receive_message())
    print(in_memory_messaging.receive_message())
    print(in_memory_messaging.receive_message())
    print(file_messaging.receive_message())
    print(file_messaging.receive_message())
    print(file_messaging.receive_message())
    print(file_messaging.receive_message())


if __name__ == "__main__":
    main()
