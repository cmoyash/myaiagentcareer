from agent.baseagent import BaseAgent
from typing import List , Dict
from memory.shared_memory import SharedMemory
from memory.conversation_memory import ConversationMemory
import time






class AgentOrchestrator:
    def __init__(self , memory: SharedMemory , conversation_memory: ConversationMemory):
        self.memory = memory
        self.agents: Dict[str , BaseAgent] = {}
        self.conversation_memory = conversation_memory

    def register(self , agent_name: str , agent: BaseAgent):
        self.agents[agent_name.lower()] = agent

    def execute(self , workflow_list: List[str]):
        print(f"Initilizing The multi-Agent Workflow\n")
        for agent_name in workflow_list:
            agent_name = agent_name.lower().strip()
            agent = self.agents.get(agent_name)

            if agent is None:
                raise ValueError(
                    f"{agent_name} is not registered"
                )

            print(f"\nExecuting {agent_name.title()}📊")
            final_response = agent.execute()
            print(f"Collected Enough Information from {agent_name.title()}✅")
        return final_response
    