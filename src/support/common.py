import time
from support.path_helper import *
import support.log_helper as lh

# ---------------------------------------------------------------------
# --- Config & Constants
# ---------------------------------------------------------------------



# ---------------------------------------------------------------------
# --- Globals
# ---------------------------------------------------------------------

logger = lh.init_logger('main')

# ---------------------------------------------------------------------
# --- Commonly used functions
# ---------------------------------------------------------------------

__start_times = {}


def start_timing(id, msg=''):
    __start_times[id] = time.time()

    print()
    print('v'*20)
    print(f'START of timing {id}: {msg}')


def end_timing(id, msg=''):
    start_time = __start_times[id]
    duration = time.time() - start_time
    minutes = int(duration // 60)
    secs = duration % 60

    print(f'END of timing {id}: {msg} ({minutes}m, {secs:.1f}s)')
    print('^'*20)
    print()


# ---------------------------------------------------------------------
# --- Executing
# ---------------------------------------------------------------------

# run these to create dir structure first time if not existing
from_src_root('', create_if_needed=True)
from_data_root('', create_if_needed=True)

if __name__ == '__main__':
    # test
    print(from_src_root('some_src'))
    print(from_data_root('some_data'))