from agent.baseagent import BaseAgent
from prompts.plannerprompt import PLANNER_PROMPT




class PlannerAgent(BaseAgent):
    def get_agent_name(self) -> str:
        return "Planner"

    def get_memory_key(self) -> str:
        return "plan"

    def build_prompt(self) -> str:
        user_query = self.memory.get("user_query")
        return PLANNER_PROMPT.format(user_query = user_query)
    