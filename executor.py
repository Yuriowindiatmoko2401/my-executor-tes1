from jina import Executor, DocumentArray, requests


class MyExecutor98(Executor):
    """"""
    @requests
    def foo(self, docs: DocumentArray, **kwargs):
        pass
