from agent.baseagent import BaseAgent
from prompts.researcherprompt import RESEARCH_PROMPT




class ResearchAgent(BaseAgent):
    def get_agent_name(self) -> str:
        return "Research"

    def get_memory_key(self) -> str:
        return "research"

    def build_prompt(self) -> str:
        planner_output = self.memory.get("plan")
        return RESEARCH_PROMPT.format(planner_output = planner_output)

    