from dataclasses import dataclass




@dataclass
class WorkFlowDecision:

    workflow_name : str
    confidence :  str
    reason : str

    def display(self) -> str:
        print(f"Workflow: {self.workflow_name}\nConfidence: {self.confidence}\nReason: {self.reason}")