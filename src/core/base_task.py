from src.core.task_engine_map import task_engine_map


# Base Task Class
class BaseTask:
    def execute(self, payload: dict):
        engine_type = payload.get("engine_type")
        task_name = getattr(self, '_task_name', None)
        engine_class = task_engine_map.get_task_engine_class(task_name, engine_type)
        if not engine_class:
            raise ValueError(f"Engine '{engine_type}' not supported for task '{task_name}'.")
        engine_class().execute(payload)


# Base Workflow Class
class BaseWorkflow:
    tasks = []

    def execute_task(self, task_name: str, payload: dict):
        task_class = next((task for task in self.tasks if getattr(task, '_task_name', '') == task_name), None)
        if task_class:
            task_class().execute(payload)
        else:
            raise ValueError(f"Task '{task_name}' not found.")
