# Workflow Class Example
from src.core.base_task import BaseWorkflow
from src.core.decorators import Workflow
from src.tasks.quiesce_db import QuiesceDBTask
from src.tasks.unquiesce_db import UnquiesceDBTask


@Workflow(workflow_name='create_snapshot')
class CreateSnapshot(BaseWorkflow):
    tasks = [QuiesceDBTask, UnquiesceDBTask]  # Reference classes directly for clarity
