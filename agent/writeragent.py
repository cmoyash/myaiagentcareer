from agent.baseagent import BaseAgent
from prompts.writerprompt import WRITER_PROMPT



class WriterAgent(BaseAgent):
    def get_agent_name(self):
        return "Writer"

    def get_memory_key(self):
        return "writer"

    def build_prompt(self):
        research_output = self.memory.get("research")
        return WRITER_PROMPT.format(research_output = research_output)

    