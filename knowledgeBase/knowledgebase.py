from pathlib import Path
import json
from typing import Any




class KnowledgeBase:
    def __init__(self , file):
        self.file = file
        self.data : dict = {}

    def get(self , key: str) -> str:
        return self.data.get(key , None)

    def load_data(self) -> Any:
        file_path = Path(self.file)

        if not file_path.exists():
            raise FileNotFoundError(
                f"File not Found: {file_path}"
            )
        with open(file_path , "r" , encoding="utf-8") as f:
            new_data = json.load(f)
            self.data = new_data
            return new_data

    def retrieve(self , user_query: str) -> str:
        user_query = user_query.lower()
        for key , value in self.data.items():
            simple_key = key.lower().replace("_" , " ")
            if simple_key in user_query:
                return value
        return {}

    def get_all(self) -> dict[str , Any]:
        return self.data

    def display(self) -> None:
        print("\n" + "=" * 60)
        print("KNOWLEDGE BASE")
        print("=" * 60)

        if not self.data:
            print("vKnowledge Base is empty")
        for key in self.data.keys():
            print(f"Key: {key}")



    

        