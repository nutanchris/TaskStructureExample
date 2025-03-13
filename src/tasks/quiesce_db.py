from src.core.base_task import BaseTask
from src.core.decorators import Engine, Task


# Sample Task: Quiesce DB
@Task(task_name='quiesce_db')
class QuiesceDBTask(BaseTask):
    pass


# Engine-specific classes inheriting from respective task
@Engine(engine_type='mongo')
class MongoQuiesceDBTask(QuiesceDBTask):
    def execute(self, payload: dict):
        print(f"[MongoDB] Quiescing database with payload: {payload}")


@Engine(engine_type='postgres')
class PostgresQuiesceDBTask(QuiesceDBTask):
    def execute(self, payload: dict):
        print(f"[Postgres] Quiescing database with payload: {payload}")
