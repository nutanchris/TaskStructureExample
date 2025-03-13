import importlib
import pkgutil
import src.workflows as workflows  # Import the workflows package directly
from src.core.workflow_registry import workflow_registry


# Auto-import all workflow modules to trigger @Workflow decorators
def load_workflows():
    package = workflows
    for _, module_name, _ in pkgutil.iter_modules(package.__path__):
        print("importing", module_name)
        importlib.import_module(f"{package.__name__}.{module_name}")


# Executor Function
def executor(workflow_name: str, task_name: str, payload: dict):
    workflow_class = workflow_registry.get(workflow_name)
    if not workflow_class:
        raise ValueError(f"Workflow '{workflow_name}' not found.")

    workflow = workflow_class()
    workflow.execute_task(task_name, payload)


# Sample Execution
payload_example = {
    "engine_type": "mongo",
    "data": "Sample Data"
}
load_workflows()  # Ensure all workflows are imported before lookup
executor("create_snapshot", "quiesce_db", payload_example)
