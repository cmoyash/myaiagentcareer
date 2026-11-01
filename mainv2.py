from agent.planneragent import PlannerAgent
from agent.researchagent import ResearchAgent
from agent.writeragent import WriterAgent
from agent.reviewragent import ReviewerAgent
from memory.shared_memory import SharedMemory
from memory.conversation_memory import ConversationMemory
from services.gemini_services import GeminiService
from orchestrator.agent_orchestrator import AgentOrchestrator
from knowledgeBase.knowledgebase import KnowledgeBase
from workflow_router.workflow_router import WorkflowRouter
from workflow_router.workflow_registry import WorkFlowRegistry


gemini = GeminiService()
context = ConversationMemory()   # Loop ke bahar (history)
registry = WorkFlowRegistry()
router = WorkflowRouter(gemini=gemini , registry=registry)

while True:
    print("\n" + "=" * 60)
    user_query = input("Enter Your AI Goal (or 'bye'): ")
    if user_query.lower() in ["bye", "exit", "quit"]:
        print("Goodbye!")
        break

    knowledgee = KnowledgeBase("knowledge_data.json")
    context.add_user_message(message=user_query)



    # User message history mein save karo
    context.add_user_message(user_query)


    # Fresh shared memory per turn
    mem = SharedMemory()
    mem.add("user_query", user_query)

    # Agents ko conversation_memory pass karo
    planner = PlannerAgent(memory=mem, gemini=gemini, conversation=context , knowledge=knowledgee)
    researcher = ResearchAgent(memory=mem, gemini=gemini, conversation=context , knowledge=knowledgee)
    writer = WriterAgent(memory=mem, gemini=gemini, conversation=context , knowledge=knowledgee)
    reviewer = ReviewerAgent(memory=mem, gemini=gemini, conversation=context , knowledge=knowledgee)

    # Orchestrator ko bhi conversation_memory pass karo
    manager = AgentOrchestrator(memory=mem, conversation_memory=context)
    manager.register("planner" , planner)
    manager.register("researcher" ,researcher)
    manager.register("writer" , writer)
    manager.register("reviewer" , reviewer)

    decision = router.route(user_query=user_query)
    decision.display()
    main_list = registry.get_workflow(decision.workflow_name)
    print()
    print("=" * 60)
    for index , agent in enumerate(main_list , start=1):
        print(f"{index}. {agent}")
    print("=" * 60)
    print()

    final_result = manager.execute(main_list)

    print("\n" + "=" * 60)
    print("FINAL RESULT")
    print("=" * 60)
    print(final_result.output)
    print("=" * 60)
  