from typing import Dict, Type


class TaskEngineMapping:
    def __init__(self):
        self.tasks: Dict[str, Dict[str, Type]] = {}

    def register_task(self, task_name: str, engine_type: str, cls: Type):
        print("Registering task", task_name, engine_type)
        if task_name not in self.tasks:
            self.tasks[task_name] = {}
        self.tasks[task_name][engine_type] = cls

    def get_task_engine_class(self, task_name: str, engine_type: str) -> Type:
        return self.tasks.get(task_name, {}).get(engine_type)


task_engine_map = TaskEngineMapping()
