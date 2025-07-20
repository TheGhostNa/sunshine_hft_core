def test_import_freqtrade_constants():
    try:
        import freqtrade.constants  # noqa: F401
    except ImportError:
        assert False, "freqtrade.constants not found"
