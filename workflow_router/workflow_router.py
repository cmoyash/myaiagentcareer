from models.workflow_decision import WorkFlowDecision
from workflow_router.workflow_registry import WorkFlowRegistry
from services.gemini_services import GeminiService
from google.genai import types






class WorkflowRouter:
    def __init__(self , gemini:  GeminiService , registry:  WorkFlowRegistry):
        self.gemini = gemini
        self.registry = registry

    def build_prompt(self , user_query: str) -> str:
        main_workflows = []
        for index , workflow_name in enumerate(self.registry.get_available_workflows() , start=1):
            main_workflows.append(f"{index}. {workflow_name}")
        workflow_text = ("\n").join(main_workflows)

        prompt = f"""You are an enterprise AI workflow router.
        Your job is to determine which workflow should execute.

        Available Workflows:
        {workflow_text}

        Instructions:
        1. Select only one workflow.
        2. Return your answer using the provided schema.
        3. Do not explain everything.

        User Request: {user_query}
        """ 

        return prompt

    def route(self , user_query: str) -> WorkFlowDecision:
        prompt = self.build_prompt(user_query=user_query)
        response  = self.gemini.generate_response(
            prompt=prompt , 
            config=types.GenerateContentConfig(
                response_mime_type="application/json" ,
                response_schema=WorkFlowDecision
            )
        )

        return response.parsed



