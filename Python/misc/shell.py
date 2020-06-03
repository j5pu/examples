from utils import log_exc, dirpkg
from lib.log import Log
from sh import sudo, ErrorReturnCode
import inspect
import configparser
from pprint import pprint

directory, package = dirpkg(__file__)

logger = Log(directory, package)


@log_exc(logger)
def extract_command(full_cmd, log):
    log.spam('full_cmd == {}'.format(full_cmd))
    command = ''
    record = False
    first = False
    for char in full_cmd:
        if record:
            if char in "(\\":
                record = False
            elif char not in '["] ':
                command = command + char
        else:
            if char == '=' and first is False:
                first = True
                record = True
            elif char == ')':
                record = True

    log.spam('command == {}'.format(command))
    return command.rstrip('\n')


@log_exc(logger)
def my_sudo(*args, log, **kwargs):
    command = extract_command(str(inspect.stack()[2][4]))
    line_nr = extract_command(str(inspect.stack()[1][5]))
    for i in range (0, 2):
        for j in range (0, 5):
            print('[{}]:[{}] = {}'.format(i, j, str(inspect.stack()[2][4])))
            exit(0)
    log.spam('line_nr == {}'.format(line_nr))
    log.spam('{} == {}'.format(line_nr.__name__, line_nr))
    # spam(log, line_nr)
    log.spam('command == {}'.format(command))
    ini_file = '{0}/{1}.ini'.format(directory, 'shell')
    try:
        file = open(ini_file, 'r')
    except FileNotFoundError:
        raise

    ini = configparser.RawConfigParser()
    ini.read(ini_file)
    file.close()

    root = False
    if ini['root']:
        for key, value in ini.items('root'):
            if key == command:
                root = True
    if not root:
        sudo_options = ('-i', '-ufp', command, )
        command = sudo_options
    log.spam('command == {}'.format(command))

    return_code = 0
    output = ''
    error_output = ''
    options = (command,) + args
    log.spam('options == {}'.format(options))

    for key, element in kwargs.items():
        kwarg = '{0}={1}'.format(key, element)
        new_options = (options,) + kwarg
        options = new_options
        log.spam('options == {}'.format(options))
    try:
        output = sudo(options)
        log.success('Executed: {}'.format(options))
    except ErrorReturnCode as exception:
        return_code = exception.exit_code
        error_output = exception.stderr.decode()
        log.error('ErrorReturnCode: {} - Code: {} - Stderr: {}'.format(options, return_code, error_output))
    finally:
        return output, error_output, return_code


service = my_sudo
curl = my_sudo
ls = my_sudo
stdout, stderr, code = service('tor', 'restart')
stdout, stderr, code = ls()
