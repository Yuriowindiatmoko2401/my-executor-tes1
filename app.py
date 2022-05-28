from docarray import Document
from jina import Flow

f = Flow().add(uses='config.yml')

with f:
    f.post(on='/random_work', inputs=Document(), on_done=print)