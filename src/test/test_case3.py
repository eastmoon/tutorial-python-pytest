#
import os
import logging
#
from mymath import *
#
LOGGER = logging.getLogger(__name__)

#
def test_system_echo(capfdbinary):
    os.system('echo "hello"')
    captured = capfdbinary.readouterr()
    assert captured.out == b"hello\n"

def test_output(capsys):
    print("hello")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"

def test_foo(caplog):
    caplog.set_level(logging.INFO)
    LOGGER.info("boo %s", "arg")
    assert caplog.record_tuples == [(__name__, logging.INFO, "boo arg")]

def test_eggs():
    LOGGER.info('eggs info')
    LOGGER.warning('eggs warning')
    LOGGER.error('eggs error')
    LOGGER.critical('eggs critical')
    assert True
