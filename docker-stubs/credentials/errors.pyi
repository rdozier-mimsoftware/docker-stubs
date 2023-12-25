from typing import Any

class StoreError(RuntimeError): ...
class CredentialsNotFound(StoreError): ...
class InitializationError(StoreError): ...

def process_store_error(cpe: Any, program: str) -> None: ...
