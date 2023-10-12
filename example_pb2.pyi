from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class eventData(_message.Message):
    __slots__ = ["id", "interface", "money"]
    ID_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    id: int
    interface: str
    money: int
    def __init__(self, id: _Optional[int] = ..., interface: _Optional[str] = ..., money: _Optional[int] = ...) -> None: ...

class CustomerRequest(_message.Message):
    __slots__ = ["id", "event"]
    ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_FIELD_NUMBER: _ClassVar[int]
    id: int
    event: eventData
    def __init__(self, id: _Optional[int] = ..., event: _Optional[_Union[eventData, _Mapping]] = ...) -> None: ...

class responseData(_message.Message):
    __slots__ = ["interface", "result", "balance"]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    interface: str
    result: str
    balance: int
    def __init__(self, interface: _Optional[str] = ..., result: _Optional[str] = ..., balance: _Optional[int] = ...) -> None: ...
