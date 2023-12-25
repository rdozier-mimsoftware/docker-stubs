from typing import Generator, Tuple, Any
from ..transport import NpipeSocket

STDOUT: int
STDERR: int

class SocketError(Exception): ...

NPIPE_ENDED: int

def read(socket: NpipeSocket, n: int = 4096) -> bytes: ...
def read_exactly(socket: NpipeSocket, n: int) -> bytes: ...
def next_frame_header(socket: NpipeSocket) -> Tuple[int, int]: ...
def frames_iter(
    socket: NpipeSocket, tty: bool = False
) -> Generator[Tuple[int, bytes], None, None]: ...
def frames_iter_no_tty(
    socket: NpipeSocket,
) -> Generator[Tuple[int, bytes], None, None]: ...
def frames_iter_tty(
    socket: NpipeSocket,
) -> Generator[Tuple[int, bytes], None, None]: ...
def consume_socket_output(
    frames: Generator[Tuple[int, bytes], None, None], demux: bool = False
) -> Tuple[bytes, bytes]: ...
def demux_adaptor(stream_id: int, data: bytes) -> Tuple[int, bytes]: ...
