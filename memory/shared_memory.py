


class SharedMemory:
    def __init__(self):
        self._memory = {}

    def add(self , key , value) -> None:
        self._memory[key] =  value

    def get(self, key) -> str:
        return self._memory.get(key)

    def exists(self , key) -> bool:
        return key in self._memory

    def clear(self) -> None:
        self._memory.clear()

    def delete(self , key) -> None:
        self._memory.pop(key, None)

    def display(self) -> str:
        for key , value in self._memory.items():
            print(f"key: {key}")
            print(f"Value: {value}")
            print("")

    def get_all(self) -> dict:
        return self._memory