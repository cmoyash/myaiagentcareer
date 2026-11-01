from dataclasses import dataclass
from typing import Optional , Any



@dataclass
class AgentResponse:
    agent_name : str
    output : Any
    status : str = "success"
    error : Optional[str] = None

    def is_success(self) -> bool:
        return self.status.lower() == "success"

    