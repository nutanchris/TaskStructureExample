from src.core.base_task import BaseTask
from src.core.decorators import Engine, Task


# Sample Task: Unquiesce DB
@Task(task_name='unquiesce_db')
class UnquiesceDBTask(BaseTask):
    pass


@Engine(engine_type='mongo')
class MongoUnquiesceTask(UnquiesceDBTask):
    def execute(self, payload: dict):
        print(f"[MongoDB] Unquiescing database with payload: {payload}")


@Engine(engine_type='postgres')
class PostgresUnquiesceTask(UnquiesceDBTask):
    def execute(self, payload: dict):
        print(f"[Postgres] Unquiescing database with payload: {payload}")
