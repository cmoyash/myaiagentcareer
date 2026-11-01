from agent.baseagent import BaseAgent
from prompts.reviewerprompt import REVIEWER_PROMPT


class ReviewerAgent(BaseAgent):
    def get_agent_name(self):
        return "Reviewer"

    def get_memory_key(self):
        return "review"

    def build_prompt(self):
        roadmap = self.memory.get("writer")
        return REVIEWER_PROMPT.format(roadmap = roadmap)
    