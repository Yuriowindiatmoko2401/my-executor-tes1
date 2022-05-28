from jina import Executor, DocumentArray, requests
from .helper import print_something

class MyExecutor98(Executor):
    """"""
    @requests
    def foo(self, docs: DocumentArray, **kwargs):
        print_something()