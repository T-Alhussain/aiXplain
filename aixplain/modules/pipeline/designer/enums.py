from enum import Enum


class RouteType(str, Enum):
    CHECK_TYPE = "checkType"
    CHECK_VALUE = "checkValue"


class Operation(str, Enum):
    GREATER_THAN = "greaterThan"
    GREATER_THAN_OR_EQUAL = "greaterThanOrEqual"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL = "lessThanOrEqual"
    EQUAL = "equal"
    DIFFERENT = "different"
    CONTAIN = "contain"
    NOT_CONTAIN = "notContain"


class NodeType(str, Enum):
    ASSET = "ASSET"
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"
    SCRIPT = "SCRIPT"
    SEGMENTOR = "SEGMENT"
    RECONSTRUCTOR = "RECONSTRUCT"
    ROUTER = "ROUTER"
    DECISION = "DECISION"


class AssetType(str, Enum):
    MODEL = "MODEL"


class FunctionType(str, Enum):
    AI = "AI"
    SEGMENTOR = "SEGMENTOR"
    RECONSTRUCTOR = "RECONSTRUCTOR"


class ParamType:
    INPUT = "INPUT"
    OUTPUT = "OUTPUT"