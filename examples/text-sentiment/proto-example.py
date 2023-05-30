from dataclasses import dataclass
from enum import Enum
from typing import Annotated, Dict, List
import py_to_proto

# Define the Foo structure as a python dataclass, including a nested enum
@dataclass
class Foo:

    class BarEnum(Enum):
        EXAM: 0
        JOKE_SETTING: 1

    foo: bool
    bar: List[BarEnum]

# Define the Foo protobuf message class
FooProto = py_to_proto.descriptor_to_message_class(
    py_to_proto.dataclass_to_proto(
        package="foobar",
        dataclass_=Foo,
    )
)

# Declare the Bar structure as a python dataclass with a reference to the
# FooProto type
@dataclass
class Bar:
    baz: FooProto

# Define the Bar protobuf message class
BarProto = py_to_proto.descriptor_to_message_class(
    py_to_proto.dataclass_to_proto(
        package="foobar",
        dataclass_=Bar,
    )
)

# Instantiate a BarProto
# print(BarProto(baz=FooProto(foo=True, bar=[Foo.BarEnum.EXAM.value])))
print(BarProto(baz=FooProto()))

def write_protos(proto_dir: str):
    """Write out the .proto files for FooProto and BarProto to the given
    directory
    """
    FooProto.write_proto_file(proto_dir)
    BarProto.write_proto_file(proto_dir)

write_protos('protos')