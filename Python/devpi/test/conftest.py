import pytest

import example_devpi


def pytest_addoption(parser):
    group = parser.getgroup('sober', 'sober specific options')
    group.addoption('--project-version',
                    default=example_devpi.get_version(),
                    dest='vstring',
                    help='expected project version - default %s' % example_devpi.get_version())


@pytest.fixture()
def example_devpi_expected_version(request):
    return request.config.getvalue('vstring')