from src.core.task_engine_map import task_engine_map
from src.core.workflow_registry import register_workflow


# Task Decorator
def Task(task_name: str):
    def decorator(cls):
        cls._task_name = task_name
        return cls

    return decorator


# Engine Decorator
def Engine(engine_type: str):
    def decorator(cls):
        base_task = cls.__bases__[0]
        task_name = getattr(base_task, '_task_name', None)
        if not task_name:
            raise ValueError(f"Engine '{engine_type}' registered without a valid task name.")
        task_engine_map.register_task(task_name, engine_type, cls)
        return cls

    return decorator


# Workflow Decorator
def Workflow(workflow_name: str):
    def decorator(cls):
        register_workflow(workflow_name, cls)
        return cls

    return decorator
