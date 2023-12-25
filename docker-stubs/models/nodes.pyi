from typing import Any, Dict, Optional, List
from .resource import Collection as Collection, Model as Model

class Node(Model):
    id_attribute: str = "ID"
    @property
    def version(self) -> Dict[str, Any]: ...
    def update(self, node_spec: Dict[str, Any]) -> None: ...
    def remove(self, force: bool = False) -> None: ...

class NodeCollection(Collection):
    model = Node
    def get(self, node_id: str) -> Node: ...
    def list(self, *args: Any, **kwargs: Any) -> List[Node]: ...
