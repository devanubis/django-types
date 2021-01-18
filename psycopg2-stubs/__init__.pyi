from typing import Any, Optional

from psycopg2 import errors as errors
from psycopg2 import extensions as extensions
from psycopg2 import tz as tz

paramstyle: str
threadsafety: int

def connect(
    dsn: Optional[str] = ...,
    connection_factory: Optional[Any] = ...,
    cursor_factor: Optional[Any] = ...,
    async_: bool = ...,
    dbname: str = ...,
    user: str = ...,
    password: str = ...,
    host: str = ...,
    port: str = ...,
    **kwargs: str
) -> extensions.connection: ...

class Warning(Exception): ...

class Error(Exception):
    @property
    def pgerror(self) -> Optional[str]: ...
    @property
    def pgcode(self) -> Optional[str]: ...
    @property
    def cursor(self) -> Optional[extensions.cursor]: ...
    @property
    def diag(self) -> extensions.Diagnostics: ...

class InterfaceError(Error): ...
class DatabaseError(Error): ...
class DataError(DatabaseError): ...
class OperationalError(DatabaseError): ...
class IntegrityError(DatabaseError): ...
class InternalError(DatabaseError): ...
class ProgrammingError(DatabaseError): ...
class NotSupportedError(DatabaseError): ...

class Date:
    def __init__(self, year: int, month: int, day: int) -> None: ...

class Time:
    def __init__(self, hour: int, minute: int, second: int) -> None: ...

class Timestamp:
    def __init__(
        self, year: int, month: int, day: int, hour: int, minute: int, second: int
    ) -> None: ...

class DateFromTicks:
    def __init__(self, ticks: int) -> None: ...

class TimeFromTicks:
    def __init__(self, ticks: int) -> None: ...

class TimestampFromTicks:
    def __init__(self, ticks: int) -> None: ...

class Binary:
    def __init__(self, string: bytes) -> None: ...

class STRING: ...
class BINARY: ...
class NUMBER: ...
class DATETIME: ...
class ROWID: ...
