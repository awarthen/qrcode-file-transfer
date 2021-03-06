import logging
import os
import sys
from contextlib import contextmanager

LOGGER = logging.getLogger(__name__)

def confirm_dir(dir):
    ''' Confirms that a directory can be written to.

    This function does the following:
      (1) If `dir` doesn't exist, to creates it.
      (2) If `dir` exists, checks that it is a directory.

    If this function returns True, then the directory exists.
    '''
    if dir == '':
        return True
    elif not os.path.exists(dir):
        LOGGER.debug('Ouput directory doesn\'t exist! Creating.')
        try:
            os.makedirs(dir)
            return True
        except OSError as e:
            print('Unable to create output directory. More info below:')
            print('\t{e}'.format(e=e))
            return False
    elif not os.path.isdir(dir):
        print('Output directory already exists and is not a directory. ({d})'.format(d=dir))
        return False
    else:
        return True

@contextmanager
def open_file(filename, mode='r'):
    '''Attempt to open a file.

    Yields (file_handle, error) depending on outcome.

    Adapted from: https://stackoverflow.com/a/6090497
    '''
    try:
        f = open(filename, mode)
    except OSError as err:
        yield None, err
    else:
        try:
            yield f, None
        finally:
            f.close()
