from propert import staticproperty

def test_basic_usage():
    class Test:
        @staticproperty
        def static_property():
            return 100

    assert Test.static_property == 100