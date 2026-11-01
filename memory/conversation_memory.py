from typing import List


class ConversationMemory:
    """Maintains conversation history."""

    def __init__(self):
        self._messages: List[str] = []

    def add_user_message(self, message: str) -> None:
        self._messages.append(f"User: {message}")

    def add_ai_message(self, message: str) -> None:
        self._messages.append(f"AI: {message}")

    def get_context(self) -> str:
        return "\n".join(self._messages)

    def clear(self) -> None:
        self._messages.clear()

    def display(self, max_length: int = 120) -> None:
        print("\n" + "=" * 60)
        print("CONVERSATION MEMORY")
        print("=" * 60)

        if not self._messages:
            print("No conversation available")
        else:
            for message in self._messages:
                preview = message[:max_length] + "..." if len(message) > max_length else message
                print(preview)

        print("=" * 60)
    