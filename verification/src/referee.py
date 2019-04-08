from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "middle"
    FUNCTION_NAMES = {
        "python_3": "middle",
        "js_node": "middle"
    }
    ENV_COVERCODE = {
        
    }