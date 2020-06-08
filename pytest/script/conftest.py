# -*- coding:utf-8 -*-
import logging
import pytest
import time
import os

root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
log_path = root_path + '\\log'


def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    print ("setting up", item)


def pytest_configure(config):
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    if not config.option.htmlpath:
        config.option.htmlpath = log_path + '\\' + time.strftime('%m-%d %H-%M', time.localtime()) + '.html'


def generate_dir_name():
    return time.strftime('%Y-%m-%d %H-%M-%S', time.localtime())


@pytest.fixture(scope="session", autouse=True)
def set_logging():
    # create log dir
    dir_name = log_path + '\\' + str(generate_dir_name())
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    test_module_raw = os.environ.get('PYTEST_CURRENT_TEST')
    logging.basicConfig(level=logging.DEBUG,
                        filename=dir_name+'\\'+os.environ.get('PYTEST_CURRENT_TEST').split(':')[-1].split(' ')[0]+'.log',
                        filemode="w",
                        format='%(asctime)s : %(name)-12s : %(levelname)-8s : %(message)s')
    console = logging.StreamHandler()
    console_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    console.setFormatter(console_format)
    console.setLevel(logging.WARN)
    logging.getLogger('').addHandler(console)

