import pytest


# passar dados de configuração para os testes
def pytest_addoption(parser):
    parser.addoption("--browser_selenium", default='chrome', help='Select browser to run tests.')
