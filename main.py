"""
AI Career Coach - Version 2
Entry point utilizing centralized Agent Orchestration
"""

from agent.planneragent import PlannerAgent
from agent.researchagent import ResearchAgent
from agent.writeragent import WriterAgent
from agent.reviewragent import ReviewerAgent
from orchestrator.agent_orchestrator import AgentOrchestrator
from memory.shared_memory import SharedMemory
from services.gemini_services import GeminiService
from memory.conversation_memory import ConversationMemory
from workflow_router.workflow_router import WorkflowRouter


def main() -> None:
    print("=" * 70)
    print("AI Career Coach")
    print("=" * 70)

    user_query = input("Enter your career goal: \n")

    # Initialize shared components
    memory = SharedMemory()
    gemini_service = GeminiService()
    ConversationMemory
    # Store user query in shared memory
    router = WorkflowRouter()
    memory.add("user_query", user_query)


    # Create Agent Instances (Dependency Injection)
    planner = PlannerAgent(memory, gemini_service )
    researcher = ResearchAgent(memory, gemini_service)
    writer = WriterAgent(memory, gemini_service)
    reviewer = ReviewerAgent(memory, gemini_service)

    # Initialize Orchestrator
    orchestrator = AgentOrchestrator(memory)

    # Register Agents dynamically
    orchestrator.register(planner)
    orchestrator.register(researcher)
    orchestrator.register(writer)
    orchestrator.register(reviewer)

    # Execute Orchestrated Workflow
    final_response = orchestrator.execute()

    print("=" * 70)
    print("FINAL CAREER ROADMAP")
    print("=" * 70)
    print(final_response.output)


if __name__ == "__main__":
    main()