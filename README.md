# Task Executor with Dynamic Workflow and Task Mapping

## Project Structure
```
src/
├── core/
│   ├── base_task.py          # Base classes for tasks and workflows
│   ├── decorators.py         # Decorators for Task, Engine, and Workflow registration
│   ├── task_engine_map.py    # Manages mapping between tasks and engine-specific logic
│   ├── workflow_registry.py  # Manages the workflow registry
│
├── tasks/
│   ├── quiesce_db.py         # QuiesceDBTask and related engines
│   ├── unquiesce_db.py       # UnquiesceDBTask and related engines
│
├── workflows/
│   ├── __init__.py           # Empty to mark this as a package
│   ├── sales_workflow.py     # Example workflow linking tasks
│
└── main.py                   # Entry point with automatic discovery of workflows
```

## Design Rationale
This project is built to achieve:
- **Clean Separation of Concerns:**
  - Core logic (task execution, mapping, registration) resides in the `core/` folder.
  - Tasks are self-contained and managed independently.
  - Workflows act as lightweight task organizers, improving clarity during debugging.

- **Extensibility:**
  - Adding new tasks or engines only requires defining new classes with the appropriate decorators.
  - No modifications are needed in `main.py` when adding new workflows or tasks.

- **Robustness:**
  - Leveraging decorators eliminates the risk of forgetting to register a task or workflow.
  - Automatic discovery of workflows avoids manual imports, improving scalability.


## How It Works
1. **Task Creation:**
   - Each task is defined as a class and decorated with `@Task(task_name)`.
   - Engine-specific implementations inherit from the corresponding task and use `@Engine(engine_type)`.

2. **Workflow Definition:**
   - Workflows are simple classes that inherit from `BaseWorkflow`.
   - They list relevant tasks directly for debugging clarity and improved organization.
   - Each workflow is decorated with `@Workflow(workflow_name)` to register it.

3. **Execution Flow:**
   - `main.py` dynamically discovers workflows using `importlib` and `pkgutil`.
   - This approach ensures workflows are automatically registered without explicit imports.
   - The `executor()` function routes requests to the appropriate workflow and executes the requested task with the provided payload.


## Pros
- ✅ **Cleaner Codebase:** Encourages developers to follow a structured format without cluttering the core logic.
- ✅ **Extremely Scalable:** Adding new tasks, engines, or workflows requires minimal changes to the codebase.
- ✅ **Reduces Human Error:** Leveraging decorators ensures tasks, engines, and workflows are automatically registered.
- ✅ **Forces Consistency:** Developers must follow the defined patterns, promoting cleaner code in team environments.
- ✅ **Workflow Isolation:** The `core/` folder remains untouched when adding new workflows or tasks, improving long-term maintainability.


## Cons
❗️ **Empty-Looking Workflows:**
- Since workflows merely link together tasks, they may appear too lightweight. However, they still play a crucial role in improving code clarity and debugging.

