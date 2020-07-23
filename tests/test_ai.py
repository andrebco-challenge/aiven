

def test_version():
    from ai import __version__

    assert __version__ == '0.1.0'


def test_nothing():
    """Test the CLI."""
    assert 1 == 1
