from propert import classproperty, PropertBase

def test_classproperty() -> None:
    class Test(PropertBase):
        internal = 0
        @classproperty
        def class_prop(cls) -> int:
            assert isinstance(cls, type)
            assert cls == Test
            return 100

        @class_prop.setter
        def class_prop(cls, value: int) -> None:
            cls.internal = value

        @class_prop.deleter
        def class_prop(cls) -> None:
            cls.internal = 0

    assert Test.class_prop == 100
    Test.class_prop = 200
    assert Test.internal == 200
    del Test.class_prop
    assert Test.internal == 0

def test_cached_classproperty() -> None:
    class Test(PropertBase):
        internal = 0
        @classproperty(cache=True)
        def class_prop(cls) -> int:
            return cls.internal

        @class_prop.deleter
        @classmethod
        def class_prop(cls) -> bool: # Conditional reset, only reset if the value stored is 0 or less
            if cls.class_prop > 0:
                return False
            return True


    assert Test.class_prop == 0
    Test.internal = 100
    assert Test.class_prop == 0
    del Test.class_prop
    assert Test.class_prop == 100

    Test.internal = 200
    del Test.class_prop # should not reset, because the currently stored value is >0
    assert Test.class_prop == 100

def test_introspected_classproperty() -> None:
    class Test(PropertBase):
        internal = 0
        @classproperty(introspect=True)
        def class_prop(cls, prop) -> int:
            assert hasattr(prop, 'getter')
            assert hasattr(prop, 'setter')
            assert hasattr(prop, 'deleter')
            return 100

    assert Test.class_prop == 100
