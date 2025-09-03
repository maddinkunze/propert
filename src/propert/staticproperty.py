from typing_extensions import Generic, Self, Literal, Callable, Any, TYPE_CHECKING, overload

from .base import _base_property, _cached_property_mixin
from .types import (
    R, S, _NoValueT, _NoValue,

    _staticmethod_getter_default, _staticmethod_setter_default, _staticmethod_deleter_default,
    _staticmethod_getter_cache, _staticmethod_setter_cache, _staticmethod_deleter_cache,
    _staticmethod_getter_introspect, _staticmethod_setter_introspect, _staticmethod_deleter_introspect,
    _staticmethod_getter_cache_introspect, _staticmethod_setter_cache_introspect, _staticmethod_deleter_cache_introspect,
)

class _staticproperty(Generic[R, S], _base_property[Any, R, S], special_unwrap=staticmethod):
    if TYPE_CHECKING:
        def __init__(self,
            getter: _staticmethod_getter_default[R],
            setter: _staticmethod_setter_default[S]|None=None,
            deleter: _staticmethod_deleter_default|None=None,
            *,
            cache_default: R|_NoValueT=_NoValue,
            check_metaclass: bool=True,
        ) -> None: ...

        def getter(self, getter: _staticmethod_getter_default[R]) -> Self: ...

        def setter(self, setter: _staticmethod_setter_default[S]) -> Self: ...

        def deleter(self, deleter: _staticmethod_deleter_default) -> Self: ...

class cached_staticproperty(Generic[R, S], _base_property[Any, R, S], _cached_property_mixin[R], cache=True, special_unwrap=staticmethod):
    if TYPE_CHECKING:
        def __init__(self,
            getter: _staticmethod_getter_cache[R],
            setter: _staticmethod_setter_cache[R, S]|None=None,
            deleter: _staticmethod_deleter_cache|None=None,
            *,
            cache_default: R|_NoValueT=_NoValue,
            check_metaclass: bool=True,
        ) -> None: ...

        def getter(self, getter: _staticmethod_getter_cache[R]) -> Self: ...

        def setter(self, setter: _staticmethod_setter_cache[R, S]) -> Self: ...

        def deleter(self, deleter: _staticmethod_deleter_cache) -> Self: ...

class introspected_staticproperty(Generic[R, S], _base_property[Any, R, S], pass_self=True, special_unwrap=staticmethod):
    if TYPE_CHECKING:
        def __init__(self,
            getter: _staticmethod_getter_introspect[R, Self],
            setter: _staticmethod_setter_introspect[S, Self],
            deleter: _staticmethod_deleter_introspect[Self],
            *,
            cache_default: R|_NoValueT=_NoValue,
            check_metaclass: bool=True,
        ) -> None: ...

        def getter(self, getter: _staticmethod_getter_introspect[R, Self]) -> Self: ...

        def setter(self, setter: _staticmethod_setter_introspect[S, Self]) -> Self: ...

        def deleter(self, deleter: _staticmethod_deleter_introspect[Self]) -> Self: ...

class introspected_cached_staticproperty(Generic[R, S], _base_property[Any, R, S], _cached_property_mixin[R], pass_self=True, cache=True, special_unwrap=staticmethod):
    if TYPE_CHECKING:
        def __init__(self,
            getter: _staticmethod_getter_cache_introspect[R, Self],
            setter: _staticmethod_setter_cache_introspect[R, S, Self],
            deleter: _staticmethod_deleter_cache_introspect[Self],
            *,
            cache_default: R|_NoValueT=_NoValue,
            check_metaclass: bool=True,
        ) -> None: ...

        def getter(self, getter: _staticmethod_getter_cache_introspect[R, Self]) -> Self: ...

        def setter(self, setter: _staticmethod_setter_cache_introspect[R, S, Self]) -> Self: ...

        def deleter(self, deleter: _staticmethod_deleter_cache_introspect[Self]) -> Self: ...


@overload
def staticproperty(
    getter: _staticmethod_getter_default[R],
    setter: _staticmethod_setter_default[S]|None = None,
    deleter: _staticmethod_deleter_default|None = None,
    *,
    cache: Literal[False] = False,
    cache_default: _NoValueT = _NoValue,
    introspect: Literal[False] = False,
    check_metaclass: bool = True,
) -> _staticproperty[R, S]: ...

@overload
def staticproperty(
    getter: _staticmethod_getter_cache[R],
    setter: _staticmethod_setter_cache[R, S]|None = None,
    deleter: _staticmethod_deleter_cache|None = None,
    *,
    cache: Literal[True],
    cache_default: R|_NoValueT = _NoValue,
    introspect: Literal[False] = False,
    check_metaclass: bool = True,
) -> cached_staticproperty[R, S]: ...

@overload
def staticproperty(
    getter: _staticmethod_getter_introspect[R, introspected_staticproperty[R, S]],
    setter: _staticmethod_setter_introspect[S, introspected_staticproperty[R, S]]|None = None,
    deleter: _staticmethod_deleter_introspect[introspected_staticproperty[R, S]]|None = None,
    *,
    cache: Literal[False] = False,
    cache_default: _NoValueT = _NoValue,
    introspect: Literal[True],
    check_metaclass: bool = True,
) -> introspected_staticproperty[R, S]: ...

@overload
def staticproperty(
    getter: _staticmethod_getter_cache_introspect[R, introspected_cached_staticproperty[R, S]],
    setter: _staticmethod_setter_cache_introspect[R, S, introspected_cached_staticproperty[R, S]]|None = None,
    deleter: _staticmethod_deleter_cache_introspect[introspected_cached_staticproperty[R, S]]|None = None,
    *,
    cache: Literal[True],
    cache_default: R|_NoValueT = _NoValue,
    introspect: Literal[True],
    check_metaclass: bool = True,
) -> introspected_cached_staticproperty[R, S]: ...

@overload
def staticproperty(
    getter: None = None,
    setter: None = None,
    deleter: None = None,
    *,
    cache: Literal[False] = False,
    cache_default: _NoValueT = _NoValue,
    introspect: Literal[False] = False,
    check_metaclass: bool = True,
) -> Callable[[_staticmethod_getter_default[R]], _staticproperty[R, S]]: ...

@overload
def staticproperty(
    getter: None = None,
    setter: None = None,
    deleter: None = None,
    *,
    cache: Literal[True],
    cache_default: R|_NoValueT = _NoValue,
    introspect: Literal[False] = False,
    check_metaclass: bool = True,
) -> Callable[[_staticmethod_getter_cache[R]], cached_staticproperty[R, S]]: ...

@overload
def staticproperty(
    getter: None = None,
    setter: None = None,
    deleter: None = None,
    *,
    cache: Literal[False] = False,
    cache_default: _NoValueT = _NoValue,
    introspect: Literal[True],
    check_metaclass: bool = True,
) -> Callable[[_staticmethod_getter_introspect[R, introspected_staticproperty[R, S]]], introspected_staticproperty[R, S]]: ...

@overload
def staticproperty(
    getter: None = None,
    setter: None = None,
    deleter: None = None,
    *,
    cache: Literal[True],
    cache_default: R|_NoValueT = _NoValue,
    introspect: Literal[True],
    check_metaclass: bool = True,
) -> Callable[[_staticmethod_getter_cache_introspect[R, introspected_cached_staticproperty[R, S]]], introspected_cached_staticproperty[R, S]]: ...

def staticproperty(
    getter: Any = None,
    setter: Any = None,
    deleter: Any = None,
    *,
    cache: bool = False,
    cache_default: Any = _NoValue,
    introspect: bool = False,
    check_metaclass: bool = True,
) -> Any:
    _cls: type|None = None

    if cache and introspect:
        _cls = introspected_cached_staticproperty
    elif cache:
        _cls = cached_staticproperty
    elif introspect:
        _cls = introspected_staticproperty
    else:
        _cls = _staticproperty

    if getter:
        return _cls(getter, setter, deleter, cache_default=cache_default, check_metaclass=check_metaclass)

    def _decorator(getter_dec: Any) -> Any:
        return _cls(getter_dec, setter, deleter, cache_default=cache_default, check_metaclass=check_metaclass)
    return _decorator
