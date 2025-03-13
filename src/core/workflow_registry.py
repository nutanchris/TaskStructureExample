from typing import Dict, Type, List

workflow_registry: Dict[str, Type] = {}


def register_workflow(workflow_name: str, cls: Type):
    workflow_registry[workflow_name] = cls
