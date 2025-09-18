from __future__ import annotations

from propert import PropertBase, staticproperty, classproperty
from typing_extensions import Type

def test_mypy_default_syntax() -> None:
    class Test(PropertBase):
        @classproperty
        @classmethod
        def class_prop(cls) -> int:
            _: Type[Test] = cls
            return 100

        @staticproperty
        @staticmethod
        def static_prop() -> int:
            return 101

        @class_prop.setter
        @classmethod
        def _(cls, value: int) -> None:
            _: Type[Test] = cls
            #reveal_type(cls.static_prop)
            #cls.static_prop = value

        @class_prop.deleter
        @classmethod
        def _(cls) -> None:
            _: Type[Test] = cls
            #cls.static_prop = 101

        @static_prop.setter
        @staticmethod
        def _(value: int) -> None:
            pass

        @static_prop.deleter
        @staticmethod
        def _() -> None:
            pass

    x: int = Test.class_prop
    y: int = Test.static_prop

    Test.class_prop = 200 # type: ignore[assignment, method-assign]
