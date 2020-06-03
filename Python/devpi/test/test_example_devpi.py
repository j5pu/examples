import example_devpi


def test_version(example_devpi_expected_version):
    assert example_devpi_expected_version == example_devpi.get_version()