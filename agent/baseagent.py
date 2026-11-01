from abc import abstractmethod , ABC
from models.agentresponse import AgentResponse
from memory.conversation_memory import ConversationMemory
from memory.shared_memory import SharedMemory
from services.gemini_services import GeminiService
from knowledgeBase.knowledgebase import KnowledgeBase


class BaseAgent(ABC):
    def __init__(self , memory: SharedMemory , gemini : GeminiService  , conversation: ConversationMemory ,
                 knowledge: KnowledgeBase):
        self.memory = memory
        self.gemini = gemini
        self.conversation = conversation
        self.knowledge = knowledge


    @abstractmethod
    def get_memory_key(self) -> str:
        pass

    @abstractmethod
    def get_agent_name(self) -> str:
        pass

    @abstractmethod
    def build_prompt(self) -> str:
        pass

    def execute(self) -> AgentResponse:
        agent_prompt = self.build_prompt()
        key = self.get_memory_key()
        agent_name = self.get_agent_name()
        query = self.conversation.get_context()
        knowledge_context = self.knowledge.retrieve(user_query=query)
        context = self.conversation.get_context()
        prompt = f"""
Conversation History:
---------------------------
{context}
---------------------------

Current Task:
---------------------------
{agent_prompt}
---------------------------

Knowledge Base:
{knowledge_context}
"""

        responce = self.gemini.generate_response(prompt)
        agent_response = AgentResponse(
            agent_name= agent_name , output= responce.text
        )
        self.conversation.add_ai_message(responce.text)
        self.memory.add(key , agent_response)
        return agent_response