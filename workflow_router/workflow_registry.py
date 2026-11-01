from typing import Any , Dict , List




class WorkFlowRegistry:
    def __init__(self) -> None:
        self.workflows: Dict[str , Any] = {
            "roadmap": ["planner", "researcher", "writer", "reviewer"],
            "certification": ["researcher", "writer"],
            "project": ["researcher", "writer"],
            "review": ["reviewer"],
        }

    def exists(self , workflow_name: str) -> bool:
        return workflow_name.lower() in self.workflows

    def get_workflow(self , workflow_name: str) -> List[str]:
        workflow_name = workflow_name.lower().strip()
        if not self.exists(workflow_name=workflow_name):
            raise ValueError(
                f"{workflow_name} not found in workflows"
            )
        return self.workflows.get(workflow_name)

    def get_available_workflows(self) -> List[str]:
        return list(self.workflows.keys())

    def register(self , workflow_name: str , agents_list: List[str]) -> None:
        workflow_name = workflow_name.lower().strip()
        self.workflows[workflow_name] = agents_list

    def display(self) -> str:
        print("=" * 60)
        print("WORKFLOW REGISTRY")
        print("=" * 60)
        for workflow_name , agents_list in self.workflows.items():
            for index , agent in enumerate(agents_list , start=1):
                print(f"Workflow - {workflow_name}\n{index}. {agent}")
            print("")
        print("=" * 60)

        