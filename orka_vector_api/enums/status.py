from enum import Enum


class Status(Enum):
    INIT = 'INIT'
    RUNNING = 'RUNNING'
    CREATED = 'CREATED'
    ERROR = 'ERROR'
    TIMEOUT = 'TIMEOUT'
    BBOX_TOO_BIG = 'BBOX_TOO_BIG'
    BBOX_INVALID = 'BBOX_INVALID'
    LAYERS_INVALID = 'LAYERS_INVALID'
    NO_THREADS_AVAILABLE = 'NO_THREADS_AVAILABLE'
