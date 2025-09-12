from typing_extensions import Type, Literal, Callable, Any, overload
from inspect import signature, isclass

from .autoproperty import _autoproperty, cached_autoproperty, introspected_autoproperty, introspected_cached_autoproperty
from .classproperty import _classproperty, cached_classproperty, introspected_classproperty, introspected_cached_classproperty
from .staticproperty import _staticproperty, cached_staticproperty, introspected_staticproperty, introspected_cached_staticproperty
from .meta import enable_propert_setters, enable_propert_deleters, enable_propert_modifications
from .types import (
    T, R, S, _NoValueT, _NoValue, _CacheReset,
    _instancemethod_getter_default, _instancemethod_setter_default, _instancemethod_deleter_default,
    _instancemethod_getter_introspect, _instancemethod_setter_introspect, _instancemethod_deleter_introspect,
    _instancemethod_getter_cache, _instancemethod_setter_cache, _instancemethod_deleter_cache,
    _instancemethod_getter_cache_introspect, _instancemethod_setter_cache_introspect, _instancemethod_deleter_cache_introspect,

    _classmethod_getter_default, _classmethod_setter_default, _classmethod_deleter_default,
    _classmethod_getter_introspect, _classmethod_setter_introspect, _classmethod_deleter_introspect,
    _classmethod_getter_cache, _classmethod_setter_cache, _classmethod_deleter_cache,
    _classmethod_getter_cache_introspect, _classmethod_setter_cache_introspect, _classmethod_deleter_cache_introspect,

    _staticmethod_getter_default, _staticmethod_setter_default, _staticmethod_deleter_default,
    _staticmethod_getter_introspect, _staticmethod_setter_introspect, _staticmethod_deleter_introspect,
    _staticmethod_getter_cache, _staticmethod_setter_cache, _staticmethod_deleter_cache,
    _staticmethod_getter_cache_introspect, _staticmethod_setter_cache_introspect, _staticmethod_deleter_cache_introspect,
)

def _is_classmethod(func: Any) -> bool:
    if isinstance(func, classmethod):
        return True
    if callable(func) and len(signature(func).parameters) == 1:
        return True
    return False

def _is_staticmethod(func: Any) -> bool:
    if isinstance(func, staticmethod):
        return True
    if callable(func) and len(signature(func).parameters) == 0:
        return True
    return False

class _propert_shorthand:
    NO_VALUE = _NoValue
    CACHE_RESET = _CacheReset

    # --- autoproperty ---

    # Classmethod definitions
    @overload
    @classmethod
    def auto(cls,
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
    @classmethod
    def auto(cls,
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
    @classmethod
    def auto(cls,
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
    @classmethod
    def auto(cls,
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
    @classmethod
    def auto(cls,
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
    @classmethod
    def auto(cls,
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
    @classmethod
    def auto(cls,
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
    @classmethod
    def auto(cls,
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
    @classmethod
    def auto(cls,
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
    @classmethod
    def auto(cls,
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
    @classmethod
    def auto(cls,
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
    @classmethod
    def auto(cls,
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
    @classmethod
    def auto(cls,
        getter: Any=None,
        setter: Any=None,
        deleter: Any=None,
        *,
        cache: bool=False,
        cache_default: Any=_NoValue,
        introspect: bool=False,
        check_metaclass: bool=True,
    ) -> Any:
        if getter is None:
            def _decorator(getter_dec: Any) -> Any:
                return cls.auto(getter_dec, setter, deleter, cache=cache, cache_default=cache_default, introspect=introspect, check_metaclass=check_metaclass) # type: ignore
            return _decorator

        _cls: type|None = None

        if cache and introspect:
            _cls = introspected_cached_autoproperty
        elif cache:
            _cls = cached_autoproperty
        elif introspect:
            _cls = introspected_autoproperty
        else:
            _cls = _autoproperty

        return _cls(getter, setter, deleter, cache_default=cache_default, check_metaclass=check_metaclass)


    # --- classproperty ---

    # Classmethod definitions
    @overload
    @classmethod
    def cls(cls,
        getter: _classmethod_getter_default[T, R],
        setter: _classmethod_setter_default[T, S]|None = None,
        deleter: _classmethod_deleter_default[T]|None = None,
        *,
        cache: Literal[False] = False,
        cache_default: _NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> _classproperty[T, R, S]:
        """Create a classproperty"""

    @overload
    @classmethod
    def cls(cls,
        getter: _classmethod_getter_cache[T, R],
        setter: _classmethod_setter_cache[T, R, S]|None = None,
        deleter: _classmethod_deleter_cache[T]|None = None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> cached_classproperty[T, R, S]:
        """Create a cached classproperty"""

    @overload
    @classmethod
    def cls(cls,
        getter: _classmethod_getter_introspect[T, R, introspected_classproperty[T, R, S]],
        setter: _classmethod_setter_introspect[T, S, introspected_classproperty[T, R, S]]|None=None,
        deleter: _classmethod_deleter_introspect[T, introspected_classproperty[T, R, S]]|None=None,
        *,
        cache: Literal[False]=False,
        cache_default: _NoValueT=_NoValue,
        introspect: Literal[True],
        check_metaclass: bool=True,
    ) -> introspected_classproperty[T, R, S]:
        """Create an introspected classproperty"""

    @overload
    @classmethod
    def cls(cls,
        getter: _classmethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]],
        setter: _classmethod_setter_cache_introspect[T, R, S, introspected_cached_classproperty[T, R, S]]|None=None,
        deleter: _classmethod_deleter_cache_introspect[T, introspected_cached_classproperty[T, R, S]]|None=None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT=_NoValue,
        introspect: Literal[True],
        check_metaclass: bool=True,
    ) -> introspected_cached_classproperty[T, R, S]:
        """Create an introspected cached classproperty"""

    # Instance method definitions
    @overload
    @classmethod
    def cls(cls,
        getter: _instancemethod_getter_default[T, R],
        setter: _instancemethod_setter_default[T, S]|None = None,
        deleter: _instancemethod_deleter_default[T]|None = None,
        *,
        cache: Literal[False] = False,
        cache_default: _NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> _classproperty[T, R, S]:
        """Create a classproperty"""

    @overload
    @classmethod
    def cls(cls,
        getter: _instancemethod_getter_cache[T, R],
        setter: _instancemethod_setter_cache[T, R, S]|None = None,
        deleter: _instancemethod_deleter_cache[T]|None = None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> cached_classproperty[T, R, S]:
        """Create a cached classproperty"""

    @overload
    @classmethod
    def cls(cls,
        getter: _instancemethod_getter_introspect[T, R, introspected_classproperty[T, R, S]],
        setter: _instancemethod_setter_introspect[T, S, introspected_classproperty[T, R, S]]|None=None,
        deleter: _instancemethod_deleter_introspect[T, introspected_classproperty[T, R, S]]|None=None,
        *,
        cache: Literal[False]=False,
        cache_default: _NoValueT=_NoValue,
        introspect: Literal[True],
        check_metaclass: bool=True,
    ) -> introspected_classproperty[T, R, S]:
        """Create an introspected classproperty"""

    @overload
    @classmethod
    def cls(cls,
        getter: _instancemethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]],
        setter: _instancemethod_setter_cache_introspect[T, R, S, introspected_cached_classproperty[T, R, S]]|None=None,
        deleter: _instancemethod_deleter_cache_introspect[T, introspected_cached_classproperty[T, R, S]]|None=None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT=_NoValue,
        introspect: Literal[True],
        check_metaclass: bool=True,
    ) -> introspected_cached_classproperty[T, R, S]:
        """Create an introspected cached classproperty"""

    # Deferred definitions
    @overload
    @classmethod
    def cls(cls,
        getter: None=None,
        setter: None=None,
        deleter: None=None,
        *,
        cache: Literal[False]=False,
        cache_default: _NoValueT=_NoValue,
        introspect: Literal[False]=False,
        check_metaclass: bool=True,
    ) -> Callable[[_classmethod_getter_default[T, R]|_instancemethod_getter_default[T, R]], _classproperty[T, R, S]]:
        """Return a decorator to create a classproperty"""

    @overload
    @classmethod
    def cls(cls,
        getter: None=None,
        setter: None=None,
        deleter: None=None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT=_NoValue,
        introspect: Literal[False]=False,
        check_metaclass: bool=True,
    ) -> Callable[[_classmethod_getter_cache[T, R]|_instancemethod_getter_cache[T, R]], cached_classproperty[T, R, S]]:
        """Return a decorator to create a cached classproperty"""

    @overload
    @classmethod
    def cls(cls,
        getter: None=None,
        setter: None=None,
        deleter: None=None,
        *,
        cache: Literal[False]=False,
        cache_default: _NoValueT=_NoValue,
        introspect: Literal[True],
        check_metaclass: bool=True,
    ) -> Callable[[_classmethod_getter_introspect[T, R, introspected_classproperty[T, R, S]]|_instancemethod_getter_introspect[T, R, introspected_classproperty[T, R, S]]], introspected_classproperty[T, R, S]]:
        """Return a decorator to create an introspected classproperty"""

    @overload
    @classmethod
    def cls(cls,
        getter: None=None,
        setter: None=None,
        deleter: None=None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT=_NoValue,
        introspect: Literal[True],
        check_metaclass: bool=True,
    ) -> Callable[[_classmethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]]|_instancemethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]]], introspected_cached_classproperty[T, R, S]]:
        """Return a decorator to create an introspected cached classproperty"""


    # Actual implementation
    @classmethod
    def cls(cls,
        getter: Any=None,
        setter: Any=None,
        deleter: Any=None,
        *,
        cache: bool=False,
        cache_default: Any=_NoValue,
        introspect: bool=False,
        check_metaclass: bool=True,
    ) -> Any:
        if getter is None:
            def _decorator(getter_dec: Any) -> Any:
                return cls.cls(getter_dec, setter, deleter, cache=cache, cache_default=cache_default, introspect=introspect, check_metaclass=check_metaclass) # type: ignore
            return _decorator

        _cls: type|None = None

        if cache and introspect:
            _cls = introspected_cached_classproperty
        elif cache:
            _cls = cached_classproperty
        elif introspect:
            _cls = introspected_classproperty
        else:
            _cls = _classproperty

        return _cls(getter, setter, deleter, cache_default=cache_default, check_metaclass=check_metaclass)


    # --- staticproperty ---

    @overload
    @classmethod
    def static(cls,
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
    @classmethod
    def static(cls,
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
    @classmethod
    def static(cls,
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
    @classmethod
    def static(cls,
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
    @classmethod
    def static(cls,
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
    @classmethod
    def static(cls,
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
    @classmethod
    def static(cls,
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
    @classmethod
    def static(cls,
        getter: None = None,
        setter: None = None,
        deleter: None = None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[True],
        check_metaclass: bool = True,
    ) -> Callable[[_staticmethod_getter_cache_introspect[R, introspected_cached_staticproperty[R, S]]], introspected_cached_staticproperty[R, S]]: ...

    @classmethod
    def static(cls,
        getter: Any = None,
        setter: Any = None,
        deleter: Any = None,
        *,
        cache: bool = False,
        cache_default: Any = _NoValue,
        introspect: bool = False,
        check_metaclass: bool = True,
    ) -> Any:
        if getter is None:
            def _decorator(getter_dec: Any) -> Any:
                return cls.static(getter_dec, setter, deleter, cache_default=cache_default, check_metaclass=check_metaclass)
            return _decorator

        _cls: type|None = None

        if cache and introspect:
            _cls = introspected_cached_staticproperty
        elif cache:
            _cls = cached_staticproperty
        elif introspect:
            _cls = introspected_staticproperty
        else:
            _cls = _staticproperty

        return _cls(getter, setter, deleter, cache_default=cache_default, check_metaclass=check_metaclass)


    # --- implicit call ---

    @overload
    def __call__(self,
        getter: _classmethod_getter_default[T, R],
        setter: _classmethod_setter_default[T, S]|None = None,
        deleter: _classmethod_deleter_default[T]|None = None,
        *,
        cache: Literal[False] = False,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> _classproperty[T, R, S]: ...

    @overload
    def __call__(self,
        getter: _classmethod_getter_cache[T, R],
        setter: _classmethod_setter_cache[T, R, S]|None = None,
        deleter: _classmethod_deleter_cache[T]|None = None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> cached_classproperty[T, R, S]: ...

    @overload
    def __call__(self,
        getter: _classmethod_getter_introspect[T, R, introspected_classproperty[T, R, S]],
        setter: _classmethod_setter_introspect[T, S, introspected_classproperty[T, R, S]]|None = None,
        deleter: _classmethod_deleter_introspect[T, introspected_classproperty[T, R, S]]|None = None,
        *,
        cache: Literal[False] = False,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[True],
        check_metaclass: bool = True,
    ) -> introspected_classproperty[T, R, S]: ...

    @overload
    def __call__(self,
        getter: _classmethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]],
        setter: _classmethod_setter_cache_introspect[T, R, S, introspected_cached_classproperty[T, R, S]]|None = None,
        deleter: _classmethod_deleter_cache_introspect[T, introspected_cached_classproperty[T, R, S]]|None = None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[True],
        check_metaclass: bool = True,
    ) -> introspected_cached_classproperty[T, R, S]: ...

    @overload
    def __call__(self,
        getter: _instancemethod_getter_default[T, R],
        setter: _instancemethod_setter_default[T, S]|None = None,
        deleter: _instancemethod_deleter_default[T]|None = None,
        *,
        cache: Literal[False] = False,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> _classproperty[T, R, S]: ...

    @overload
    def __call__(self,
        getter: _instancemethod_getter_cache[T, R],
        setter: _instancemethod_setter_cache[T, R, S]|None = None,
        deleter: _instancemethod_deleter_cache[T]|None = None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> cached_classproperty[T, R, S]: ...

    @overload
    def __call__(self,
        getter: _instancemethod_getter_introspect[T, R, introspected_classproperty[T, R, S]],
        setter: _instancemethod_setter_introspect[T, S, introspected_classproperty[T, R, S]]|None = None,
        deleter: _instancemethod_deleter_introspect[T, introspected_classproperty[T, R, S]]|None = None,
        *,
        cache: Literal[False] = False,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[True],
        check_metaclass: bool = True,
    ) -> introspected_classproperty[T, R, S]: ...

    @overload
    def __call__(self,
        getter: _instancemethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]],
        setter: _instancemethod_setter_cache_introspect[T, R, S, introspected_cached_classproperty[T, R, S]]|None = None,
        deleter: _instancemethod_deleter_cache_introspect[T, introspected_cached_classproperty[T, R, S]]|None = None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[True],
        check_metaclass: bool = True,
    ) -> introspected_cached_classproperty[T, R, S]: ...

    @overload
    def __call__(self,
        getter: _staticmethod_getter_introspect[R, introspected_staticproperty[R, S]],
        setter: _staticmethod_setter_introspect[S, introspected_staticproperty[R, S]]|None = None,
        deleter: _staticmethod_deleter_introspect[introspected_staticproperty[R, S]]|None = None,
        *,
        cache: Literal[False] = False,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[True],
        check_metaclass: bool = True,
    ) -> introspected_staticproperty[R, S]: ...

    @overload
    def __call__(self,
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
    def __call__(self,
        getter: None = None,
        setter: None = None,
        deleter: None = None,
        *,
        cache: Literal[False] = False,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> (
        Callable[[_classmethod_getter_default[T, R]], _classproperty[T, R, S]] |
        Callable[[_instancemethod_getter_default[T, R]], _classproperty[T, R, S]] |
        Callable[[_staticmethod_getter_default[R]], _staticproperty[R, S]]
    ): ...

    @overload
    def __call__(self,
        getter: None = None,
        setter: None = None,
        deleter: None = None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> (
        Callable[[_classmethod_getter_cache[T, R]], cached_classproperty[T, R, S]] |
        Callable[[_instancemethod_getter_cache[T, R]], cached_classproperty[T, R, S]] |
        Callable[[_staticmethod_getter_cache[R]], cached_staticproperty[R, S]]
    ): ...

    @overload
    def __call__(self,
        getter: None = None,
        setter: None = None,
        deleter: None = None,
        *,
        cache: Literal[False] = False,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[True],
        check_metaclass: bool = True,
    ) -> (
        Callable[[_classmethod_getter_introspect[T, R, introspected_classproperty[T, R, S]]], introspected_classproperty[T, R, S]] |
        Callable[[_instancemethod_getter_introspect[T, R, introspected_classproperty[T, R, S]]], introspected_classproperty[T, R, S]] |
        Callable[[_staticmethod_getter_introspect[R, introspected_staticproperty[R, S]]], introspected_staticproperty[R, S]]
    ): ...

    @overload
    def __call__(self,
        getter: None = None,
        setter: None = None,
        deleter: None = None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[True],
        check_metaclass: bool = True,
    ) -> (
        Callable[[_classmethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]]], introspected_cached_classproperty[T, R, S]] |
        Callable[[_instancemethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]]], introspected_cached_classproperty[T, R, S]] |
        Callable[[_staticmethod_getter_cache_introspect[R, introspected_cached_staticproperty[R, S]]], introspected_cached_staticproperty[R, S]]
    ): ...

    @overload
    def __call__(self,
        getter: Type[T],
        setter: None = None,
        deleter: None = None,
        *,
        cache: Literal[False] = False,
        cache_default: _NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> Type[T]: ...

    def __call__(self,
        getter: Any = None,
        setter: Any = None,
        deleter: Any = None,
        *,
        cache: bool = False,
        cache_default: Any = _NoValue,
        introspect: bool = False,
        check_metaclass: bool = True,
    ) -> Any:
        if getter is None:
            def _decorator(getter_dec: Any) -> Any:
                return self.__call__(getter_dec, setter, deleter, cache=cache, cache_default=cache_default, introspect=introspect, check_metaclass=check_metaclass) # type: ignore

            return _decorator

        if isclass(getter):
            return enable_propert_modifications(getter)

        _cls: type|None = None

        if _is_classmethod(getter):
            if cache and introspect:
                _cls = introspected_cached_classproperty
            elif introspect:
                _cls = introspected_classproperty
            elif cache:
                _cls = cached_classproperty
            else:
                _cls = _classproperty

        elif _is_staticmethod(getter):
            if cache and introspect:
                _cls = introspected_cached_staticproperty
            elif introspect:
                _cls = introspected_staticproperty
            elif cache:
                _cls = cached_staticproperty
            else:
                _cls = _staticproperty
        
        if not _cls:
            raise ValueError("Could not determine correct property type for the given function")

        return _cls(getter, setter, deleter, cache_default=cache_default, check_metaclass=check_metaclass)

    # --- cached ---

    @overload
    @classmethod
    def cached(cls,
        getter: _classmethod_getter_cache[T, R],
        setter: _classmethod_setter_cache[T, R, S]|None = None,
        deleter: _classmethod_deleter_cache[T]|None = None,
        *,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> cached_classproperty[T, R, S]: ...

    @overload
    @classmethod
    def cached(cls,
        getter: _classmethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]],
        setter: _classmethod_setter_cache_introspect[T, R, S, introspected_cached_classproperty[T, R, S]]|None = None,
        deleter: _classmethod_deleter_cache_introspect[T, introspected_cached_classproperty[T, R, S]]|None = None,
        *,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[True],
        check_metaclass: bool = True,
    ) -> introspected_cached_classproperty[T, R, S]: ...

    @overload
    @classmethod
    def cached(cls,
        getter: _instancemethod_getter_cache[T, R],
        setter: _instancemethod_setter_cache[T, R, S]|None = None,
        deleter: _instancemethod_deleter_cache[T]|None = None,
        *,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> cached_classproperty[T, R, S]: ...

    @overload
    @classmethod
    def cached(cls,
        getter: _instancemethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]],
        setter: _instancemethod_setter_cache_introspect[T, R, S, introspected_cached_classproperty[T, R, S]]|None = None,
        deleter: _instancemethod_deleter_cache_introspect[T, introspected_cached_classproperty[T, R, S]]|None = None,
        *,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[True],
        check_metaclass: bool = True,
    ) -> introspected_cached_classproperty[T, R, S]: ...

    @overload
    @classmethod
    def cached(cls,
        getter: _staticmethod_getter_cache[R],
        setter: _staticmethod_setter_cache[R, S]|None = None,
        deleter: _staticmethod_deleter_cache|None = None,
        *,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> cached_staticproperty[R, S]: ...

    @overload
    @classmethod
    def cached(cls,
        getter: _staticmethod_getter_cache_introspect[R, introspected_cached_staticproperty[R, S]],
        setter: _staticmethod_setter_cache_introspect[R, S, introspected_cached_staticproperty[R, S]]|None = None,
        deleter: _staticmethod_deleter_cache_introspect[introspected_cached_staticproperty[R, S]]|None = None,
        *,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[True],
        check_metaclass: bool = True,
    ) -> introspected_cached_staticproperty[R, S]: ...

    @overload
    @classmethod
    def cached(cls,
        getter: None = None,
        setter: None = None,
        deleter: None = None,
        *,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[False] = False,
        check_metaclass: bool = True,
    ) -> (
        Callable[[_classmethod_getter_cache[T, R]], cached_classproperty[T, R, S]] |
        Callable[[_instancemethod_getter_cache[T, R]], cached_classproperty[T, R, S]] |
        Callable[[_staticmethod_getter_cache[R]], cached_staticproperty[R, S]]
    ): ...

    @overload
    @classmethod
    def cached(cls,
        getter: None = None,
        setter: None = None,
        deleter: None = None,
        *,
        cache_default: R|_NoValueT = _NoValue,
        introspect: Literal[True],
        check_metaclass: bool = True,
    ) -> (
        Callable[[_classmethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]]], introspected_cached_classproperty[T, R, S]] |
        Callable[[_instancemethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]]], introspected_cached_classproperty[T, R, S]] |
        Callable[[_staticmethod_getter_cache_introspect[R, introspected_cached_staticproperty[R, S]]], introspected_cached_staticproperty[R, S]]
    ): ...

    @classmethod
    def cached(cls,
        getter: Any = None,
        setter: Any = None,
        deleter: Any = None,
        *,
        cache_default: Any = _NoValue,
        introspect: bool = False,
        check_metaclass: bool = True,
    ) -> Any:
        if getter is None:
            def _decorator(getter_dec: Any) -> Any:
                return cls.cached(getter_dec, setter, deleter, cache_default=cache_default, introspect=introspect, check_metaclass=check_metaclass) # type: ignore

            return _decorator

        _cls: type|None = None

        if _is_classmethod(getter):
            if introspect:
                _cls = introspected_cached_classproperty
            else:
                _cls = cached_classproperty

        elif _is_staticmethod(getter):
            if introspect:
                _cls = introspected_cached_staticproperty
            else:
                _cls = cached_staticproperty
        
        if not _cls:
            raise ValueError("Could not determine correct property type for the given function")

        return _cls(getter, setter, deleter, cache_default=cache_default, check_metaclass=check_metaclass)


    # --- introspected ---

    @overload
    @classmethod
    def introspected(cls,
        getter: _classmethod_getter_introspect[T, R, introspected_classproperty[T, R, S]],
        setter: _classmethod_setter_introspect[T, S, introspected_classproperty[T, R, S]]|None=None,
        deleter: _classmethod_deleter_introspect[T, introspected_classproperty[T, R, S]]|None=None,
        *,
        cache: Literal[False]=False,
        cache_default: _NoValueT=_NoValue,
        check_metaclass: bool=True,
    ) -> introspected_classproperty[T, R, S]: ...

    @overload
    @classmethod
    def introspected(cls,
        getter: _classmethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]],
        setter: _classmethod_setter_cache_introspect[T, R, S, introspected_cached_classproperty[T, R, S]]|None=None,
        deleter: _classmethod_deleter_cache_introspect[T, introspected_cached_classproperty[T, R, S]]|None=None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT=_NoValue,
        check_metaclass: bool=True,
    ) -> introspected_cached_classproperty[T, R, S]: ...

    @overload
    @classmethod
    def introspected(cls,
        getter: _instancemethod_getter_introspect[T, R, introspected_staticproperty[R, S]],
        setter: _instancemethod_setter_introspect[T, S, introspected_staticproperty[R, S]]|None=None,
        deleter: _instancemethod_deleter_introspect[T, introspected_staticproperty[R, S]]|None=None,
        *,
        cache: Literal[False]=False,
        cache_default: _NoValueT=_NoValue,
        check_metaclass: bool=True,
    ) -> introspected_classproperty[T, R, S]: ...

    @overload
    @classmethod
    def introspected(cls,
        getter: _instancemethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]],
        setter: _instancemethod_setter_cache_introspect[T, R, S, introspected_cached_classproperty[T, R, S]]|None=None,
        deleter: _instancemethod_deleter_cache_introspect[T, introspected_cached_classproperty[T, R, S]]|None=None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT=_NoValue,
        check_metaclass: bool=True,
    ) -> introspected_cached_classproperty[T, R, S]: ...

    @overload
    @classmethod
    def introspected(cls,
        getter: _staticmethod_getter_introspect[R, introspected_staticproperty[R, S]],
        setter: _staticmethod_setter_introspect[S, introspected_staticproperty[R, S]]|None=None,
        deleter: _staticmethod_deleter_introspect[introspected_staticproperty[R, S]]|None=None,
        *,
        cache: Literal[False]=False,
        cache_default: _NoValueT=_NoValue,
        check_metaclass: bool=True,
    ) -> introspected_staticproperty[R, S]: ...

    @overload
    @classmethod
    def introspected(cls,
        getter: _staticmethod_getter_cache_introspect[R, introspected_staticproperty[R, S]],
        setter: _staticmethod_setter_cache_introspect[R, S, introspected_staticproperty[R, S]]|None=None,
        deleter: _staticmethod_deleter_cache_introspect[introspected_staticproperty[R, S]]|None=None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT=_NoValue,
        check_metaclass: bool=True,
    ) -> introspected_cached_staticproperty[R, S]: ...

    @overload
    @classmethod
    def introspected(cls,
        getter: None = None,
        setter: None = None,
        deleter: None = None,
        *,
        cache: Literal[False]=False,
        cache_default: _NoValueT=_NoValue,
        check_metaclass: bool=True,
    ) -> (
        Callable[[_classmethod_getter_introspect[T, R, introspected_classproperty[T, R, S]]], introspected_classproperty[T, R, S]] |
        Callable[[_instancemethod_getter_introspect[T, R, introspected_classproperty[T, R, S]]], introspected_classproperty[T, R, S]] |
        Callable[[_staticmethod_getter_introspect[R, introspected_staticproperty[R, S]]], introspected_staticproperty[R, S]]
    ): ...

    @overload
    @classmethod
    def introspected(cls,
        getter: None = None,
        setter: None = None,
        deleter: None = None,
        *,
        cache: Literal[True],
        cache_default: R|_NoValueT=_NoValue,
        check_metaclass: bool=True,
    ) -> (
        Callable[[_classmethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]]], introspected_cached_classproperty[T, R, S]] |
        Callable[[_instancemethod_getter_cache_introspect[T, R, introspected_cached_classproperty[T, R, S]]], introspected_cached_classproperty[T, R, S]] |
        Callable[[_staticmethod_getter_cache_introspect[R, introspected_cached_staticproperty[R, S]]], introspected_cached_staticproperty[R, S]]
    ): ...

    @classmethod
    def introspected(cls,
        getter: Any = None,
        setter: Any = None,
        deleter: Any = None,
        *,
        cache: bool = False,
        cache_default: Any = _NoValue,
        check_metaclass: bool = True,
    ) -> Any:
        if getter is None:
            def _decorator(getter_dec: Any) -> Any:
                return cls.introspected(getter_dec, setter, deleter, cache=cache, cache_default=cache_default, check_metaclass=check_metaclass) # type: ignore

            return _decorator

        _cls: type|None = None

        if _is_classmethod(getter):
            if cache:
                _cls = introspected_cached_classproperty
            else:
                _cls = introspected_classproperty

        elif _is_staticmethod(getter):
            if cache:
                _cls = introspected_cached_staticproperty
            else:
                _cls = introspected_staticproperty
        
        if not _cls:
            raise ValueError("Could not determine correct property type for the given function")

        return _cls(getter, setter, deleter, cache_default=cache_default, check_metaclass=check_metaclass)
    
    # --- modification enablers ---

    def enable_setters(self, cls: Type[T]) -> Type[T]:
        return enable_propert_setters(cls)

    def enable_deleters(self, cls: Type[T]) -> Type[T]:
        return enable_propert_deleters(cls)

    def enable_modifications(self, cls: Type[T]) -> Type[T]:
        return enable_propert_modifications(cls)

propert = _propert_shorthand()
