from typing_extensions import Generic, Self, Literal, Callable, Any, TYPE_CHECKING, overload

from .base import _base_property, _cached_property_mixin
from .types import (
    T, R, S, _NoValueT, _NoValue,

    _instancemethod_getter_default, _instancemethod_setter_default, _instancemethod_deleter_default,
    _instancemethod_getter_cache, _instancemethod_setter_cache, _instancemethod_deleter_cache,
    _instancemethod_getter_introspect, _instancemethod_setter_introspect, _instancemethod_deleter_introspect,
    _instancemethod_getter_cache_introspect, _instancemethod_setter_cache_introspect, _instancemethod_deleter_cache_introspect,

    _classmethod_getter_default, _classmethod_setter_default, _classmethod_deleter_default,
    _classmethod_getter_cache, _classmethod_setter_cache, _classmethod_deleter_cache,
    _classmethod_getter_introspect, _classmethod_setter_introspect, _classmethod_deleter_introspect,
    _classmethod_getter_cache_introspect, _classmethod_setter_cache_introspect, _classmethod_deleter_cache_introspect,
)

class _autoproperty(Generic[T, R, S], _base_property[T, R, S], pass_instance=True, pass_class=True, special_unwrap=classmethod):
    if TYPE_CHECKING:
        @overload
        def __init__(self,
            getter: _classmethod_getter_default[T, R],
            setter: _classmethod_setter_default[T, S]|None=None,
            deleter: _classmethod_deleter_default[T]|None=None,
            *,
            cache_default: R|_NoValueT=_NoValue,
            check_metaclass: bool=True,
        ) -> None: ...

        @overload
        def __init__(self,
            getter: _instancemethod_getter_default[T, R],
            setter: _instancemethod_setter_default[T, S]|None=None,
            deleter: _instancemethod_deleter_default[T]|None=None,
            *,
            cache_default: R|_NoValueT=_NoValue,
            check_metaclass: bool=True,
        ) -> None: ...

        def __init__(self, *args: Any, **kwargs: Any) -> None: ...

        @overload
        def getter(self, getter: _classmethod_getter_default[T, R]) -> Self: ...

        @overload
        def getter(self, getter: _instancemethod_getter_default[T, R]) -> Self: ...

        def getter(self, *args: Any, **kwargs: Any) -> Self: ...

        @overload
        def setter(self, setter: _classmethod_setter_default[T, S]) -> Self: ...

        @overload
        def setter(self, setter: _instancemethod_setter_default[T, S]) -> Self: ...

        def setter(self, *args: Any, **kwargs: Any) -> Self: ...

        @overload
        def deleter(self, deleter: _classmethod_deleter_default[T]) -> Self: ...

        @overload
        def deleter(self, deleter: _instancemethod_deleter_default[T]) -> Self: ...

        def deleter(self, *args: Any, **kwargs: Any) -> Self: ...

class cached_autoproperty(Generic[T, R, S], _base_property[T, R, S], _cached_property_mixin[R], pass_instance=True, pass_class=True, cache=True, special_unwrap=classmethod):
    if TYPE_CHECKING:
        @overload
        def __init__(self,
            getter: _classmethod_getter_cache[T, R],
            setter: _classmethod_setter_cache[T, R, S]|None=None,
            deleter: _classmethod_deleter_cache[T]|None=None,
            *,
            cache_default: R|_NoValueT=_NoValue,
            check_metaclass: bool=True,
        ) -> None: ...

        @overload
        def __init__(self,
            getter: _instancemethod_getter_cache[T, R],
            setter: _instancemethod_setter_cache[T, R, S]|None=None,
            deleter: _instancemethod_deleter_cache[T]|None=None,
            *,
            cache_default: R|_NoValueT=_NoValue,
            check_metaclass: bool=True,
        ) -> None: ...

        def __init__(self, *args: Any, **kwargs: Any) -> None: ...

        @overload
        def getter(self, getter: _classmethod_getter_cache[T, R]) -> Self: ...

        @overload
        def getter(self, getter: _instancemethod_getter_cache[T, R]) -> Self: ...

        def getter(self, *args: Any, **kwargs: Any) -> Self: ...

        @overload
        def setter(self, setter: _classmethod_setter_cache[T, R, S]) -> Self: ...

        @overload
        def setter(self, setter: _instancemethod_setter_cache[T, R, S]) -> Self: ...

        def setter(self, *args: Any, **kwargs: Any) -> Self: ...

        @overload
        def deleter(self, deleter: _classmethod_deleter_cache[T]) -> Self: ...

        @overload
        def deleter(self, deleter: _instancemethod_deleter_cache[T]) -> Self: ...

        def deleter(self, *args: Any, **kwargs: Any) -> Self: ...

class introspected_autoproperty(Generic[T, R, S], _base_property[T, R, S], pass_instance=True, pass_class=True, pass_self=True, special_unwrap=classmethod):
    if TYPE_CHECKING:
        @overload
        def __init__(self,
            getter: _classmethod_getter_introspect[T, R, Self],
            setter: _classmethod_setter_introspect[T, S, Self],
            deleter: _classmethod_deleter_introspect[T, Self],
            *,
            cache_default: R|_NoValueT=_NoValue,
            check_metaclass: bool=True,
        ) -> None: ...

        @overload
        def __init__(self,
            getter: _instancemethod_getter_introspect[T, R, Self],
            setter: _instancemethod_setter_introspect[T, S, Self],
            deleter: _instancemethod_deleter_introspect[T, Self],
            *,
            cache_default: R|_NoValueT=_NoValue,
            check_metaclass: bool=True,
        ) -> None: ...

        def __init__(self, *args: Any, **kwargs: Any) -> None: ...

        @overload
        def getter(self, getter: _classmethod_getter_introspect[T, R, Self]) -> Self: ...

        @overload
        def getter(self, getter: _instancemethod_getter_introspect[T, R, Self]) -> Self: ...

        def getter(self, *args: Any, **kwargs: Any) -> Self: ...

        @overload
        def setter(self, setter: _classmethod_setter_introspect[T, S, Self]) -> Self: ...

        @overload
        def setter(self, setter: _instancemethod_setter_introspect[T, S, Self]) -> Self: ...

        def setter(self, *args: Any, **kwargs: Any) -> Self: ...

        @overload
        def deleter(self, deleter: _classmethod_deleter_introspect[T, Self]) -> Self: ...

        @overload
        def deleter(self, deleter: _instancemethod_deleter_introspect[T, Self]) -> Self: ...

        def deleter(self, *args: Any, **kwargs: Any) -> Self: ...

class introspected_cached_autoproperty(Generic[T, R, S], _base_property[T, R, S], _cached_property_mixin[R], pass_instance=True, pass_class=True, pass_self=True, cache=True, special_unwrap=classmethod):
    if TYPE_CHECKING:
        @overload
        def __init__(self,
            getter: _classmethod_getter_cache_introspect[T, R, Self],
            setter: _classmethod_setter_cache_introspect[T, R, S, Self],
            deleter: _classmethod_deleter_cache_introspect[T, Self],
            *,
            cache_default: R|_NoValueT=_NoValue,
            check_metaclass: bool=True,
        ) -> None: ...

        @overload
        def __init__(self,
            getter: _instancemethod_getter_cache_introspect[T, R, Self],
            setter: _instancemethod_setter_cache_introspect[T, R, S, Self],
            deleter: _instancemethod_deleter_cache_introspect[T, Self],
            *,
            cache_default: R|_NoValueT=_NoValue,
            check_metaclass: bool=True,
        ) -> None: ...

        def __init__(self, *args: Any, **kwargs: Any) -> None: ...

        @overload
        def getter(self, getter: _classmethod_getter_cache_introspect[T, R, Self]) -> Self: ...

        @overload
        def getter(self, getter: _instancemethod_getter_cache_introspect[T, R, Self]) -> Self: ...

        def getter(self, *args: Any, **kwargs: Any) -> Self: ...

        @overload
        def setter(self, setter: _classmethod_setter_cache_introspect[T, R, S, Self]) -> Self: ...

        @overload
        def setter(self, setter: _instancemethod_setter_cache_introspect[T, R, S, Self]) -> Self: ...

        def setter(self, *args: Any, **kwargs: Any) -> Self: ...

        @overload
        def deleter(self, deleter: _classmethod_deleter_cache_introspect[T, Self]) -> Self: ...

        @overload
        def deleter(self, deleter: _instancemethod_deleter_cache_introspect[T, Self]) -> Self: ...

        def deleter(self, *args: Any, **kwargs: Any) -> Self: ...

# Classmethod definitions
@overload
def autoproperty(
    getter: _classmethod_getter_default[T, R],
    setter: _classmethod_setter_default[T, S]|None = None,
    deleter: _classmethod_deleter_default[T]|None = None,
    *,
    cache: Literal[False] = False,
    cache_default: _NoValueT = _NoValue,
    introspect: Literal[False] = False,
    check_metaclass: bool = True,
) -> _autoproperty[T, R, S]:
    """Create an autoproperty"""

@overload
def autoproperty(
    getter: _classmethod_getter_cache[T, R],
    setter: _classmethod_setter_cache[T, R, S]|None = None,
    deleter: _classmethod_deleter_cache[T]|None = None,
    *,
    cache: Literal[True],
    cache_default: R|_NoValueT = _NoValue,
    introspect: Literal[False] = False,
    check_metaclass: bool = True,
) -> cached_autoproperty[T, R, S]:
    """Create a cached autoproperty"""

@overload
def autoproperty(
    getter: _classmethod_getter_introspect[T, R, introspected_autoproperty[T, R, S]],
    setter: _classmethod_setter_introspect[T, S, introspected_autoproperty[T, R, S]]|None=None,
    deleter: _classmethod_deleter_introspect[T, introspected_autoproperty[T, R, S]]|None=None,
    *,
    cache: Literal[False]=False,
    cache_default: _NoValueT=_NoValue,
    introspect: Literal[True],
    check_metaclass: bool=True,
) -> introspected_autoproperty[T, R, S]:
    """Create an introspected autoproperty"""

@overload
def autoproperty(
    getter: _classmethod_getter_cache_introspect[T, R, introspected_cached_autoproperty[T, R, S]],
    setter: _classmethod_setter_cache_introspect[T, R, S, introspected_cached_autoproperty[T, R, S]]|None=None,
    deleter: _classmethod_deleter_cache_introspect[T, introspected_cached_autoproperty[T, R, S]]|None=None,
    *,
    cache: Literal[True],
    cache_default: R|_NoValueT=_NoValue,
    introspect: Literal[True],
    check_metaclass: bool=True,
) -> introspected_cached_autoproperty[T, R, S]:
    """Create an introspected cached autoproperty"""

# Instance method definitions
@overload
def autoproperty(
    getter: _instancemethod_getter_default[T, R],
    setter: _instancemethod_setter_default[T, S]|None = None,
    deleter: _instancemethod_deleter_default[T]|None = None,
    *,
    cache: Literal[False] = False,
    cache_default: _NoValueT = _NoValue,
    introspect: Literal[False] = False,
    check_metaclass: bool = True,
) -> _autoproperty[T, R, S]:
    """Create an autoproperty"""

@overload
def autoproperty(
    getter: _instancemethod_getter_cache[T, R],
    setter: _instancemethod_setter_cache[T, R, S]|None = None,
    deleter: _instancemethod_deleter_cache[T]|None = None,
    *,
    cache: Literal[True],
    cache_default: R|_NoValueT = _NoValue,
    introspect: Literal[False] = False,
    check_metaclass: bool = True,
) -> cached_autoproperty[T, R, S]:
    """Create a cached autoproperty"""

@overload
def autoproperty(
    getter: _instancemethod_getter_introspect[T, R, introspected_autoproperty[T, R, S]],
    setter: _instancemethod_setter_introspect[T, S, introspected_autoproperty[T, R, S]]|None=None,
    deleter: _instancemethod_deleter_introspect[T, introspected_autoproperty[T, R, S]]|None=None,
    *,
    cache: Literal[False]=False,
    cache_default: _NoValueT=_NoValue,
    introspect: Literal[True],
    check_metaclass: bool=True,
) -> introspected_autoproperty[T, R, S]:
    """Create an introspected autoproperty"""

@overload
def autoproperty(
    getter: _instancemethod_getter_cache_introspect[T, R, introspected_cached_autoproperty[T, R, S]],
    setter: _instancemethod_setter_cache_introspect[T, R, S, introspected_cached_autoproperty[T, R, S]]|None=None,
    deleter: _instancemethod_deleter_cache_introspect[T, introspected_cached_autoproperty[T, R, S]]|None=None,
    *,
    cache: Literal[True],
    cache_default: R|_NoValueT=_NoValue,
    introspect: Literal[True],
    check_metaclass: bool=True,
) -> introspected_cached_autoproperty[T, R, S]:
    """Create an introspected cached autoproperty"""

# Deferred definitions
@overload
def autoproperty(
    getter: None=None,
    setter: None=None,
    deleter: None=None,
    *,
    cache: Literal[False]=False,
    cache_default: _NoValueT=_NoValue,
    introspect: Literal[False]=False,
    check_metaclass: bool=True,
) -> Callable[[_classmethod_getter_default[T, R]|_instancemethod_getter_default[T, R]], _autoproperty[T, R, S]]:
    """Return a decorator to create a autoproperty"""

@overload
def autoproperty(
    getter: None=None,
    setter: None=None,
    deleter: None=None,
    *,
    cache: Literal[True],
    cache_default: R|_NoValueT=_NoValue,
    introspect: Literal[False]=False,
    check_metaclass: bool=True,
) -> Callable[[_classmethod_getter_cache[T, R]|_instancemethod_getter_cache[T, R]], cached_autoproperty[T, R, S]]:
    """Return a decorator to create a cached autoproperty"""

@overload
def autoproperty(
    getter: None=None,
    setter: None=None,
    deleter: None=None,
    *,
    cache: Literal[False]=False,
    cache_default: _NoValueT=_NoValue,
    introspect: Literal[True],
    check_metaclass: bool=True,
) -> Callable[[_classmethod_getter_introspect[T, R, introspected_autoproperty[T, R, S]]|_instancemethod_getter_introspect[T, R, introspected_autoproperty[T, R, S]]], introspected_autoproperty[T, R, S]]:
    """Return a decorator to create an introspected autoproperty"""

@overload
def autoproperty(
    getter: None=None,
    setter: None=None,
    deleter: None=None,
    *,
    cache: Literal[True],
    cache_default: R|_NoValueT=_NoValue,
    introspect: Literal[True],
    check_metaclass: bool=True,
) -> Callable[[_classmethod_getter_cache_introspect[T, R, introspected_cached_autoproperty[T, R, S]]|_instancemethod_getter_cache_introspect[T, R, introspected_cached_autoproperty[T, R, S]]], introspected_cached_autoproperty[T, R, S]]:
    """Return a decorator to create an introspected cached autoproperty"""


# Actual implementation
def autoproperty(
    getter: Any=None,
    setter: Any=None,
    deleter: Any=None,
    *,
    cache: bool=False,
    cache_default: Any=_NoValue,
    introspect: bool=False,
    check_metaclass: bool=True,
) -> Any:
    _cls: type|None = None
    
    if cache and introspect:
        _cls = introspected_cached_autoproperty
    elif cache:
        _cls = cached_autoproperty
    elif introspect:
        _cls = introspected_autoproperty
    else:
        _cls = _autoproperty

    if getter:
        return _cls(getter, setter, deleter, cache_default=cache_default, check_metaclass=check_metaclass)

    def _decorator(getter_dec: Any) -> Any:
        return _cls(getter_dec, setter, deleter, cache_default=cache_default, check_metaclass=check_metaclass)
    return _decorator
