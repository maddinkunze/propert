from __future__ import annotations

from typing_extensions import Type, TypeVar, TypeAliasType, ParamSpec, Callable, Concatenate, Any, TYPE_CHECKING

T = TypeVar("T")
R = TypeVar("R")
S = TypeVar("S")
P = TypeVar("P")
#Getter = TypeVar("Getter")
#Setter = TypeVar("Setter")
#Deleter = TypeVar("Deleter")
_ArgCallable = Callable[..., Any]
Params = ParamSpec("Params")
_AnyAction = TypeVar("_AnyAction")

class _NoValueT:
    pass
_NoValue = _NoValueT()
_CacheReset = _NoValueT()


_instancemethod_c_base = TypeAliasType("_instancemethod_c_base", Callable[Concatenate[T, Params], R], type_params=(T, Params, R))
_classmethod_c_base = TypeAliasType("_classmethod_c_base", Callable[Concatenate[Type[T], Params], R], type_params=(T, Params, R))
_staticmethod_c_base = TypeAliasType("_staticmethod_c_base", Callable[Concatenate[Params], R], type_params=(Params, R))

if TYPE_CHECKING:
    _classmethod_s_base = TypeAliasType("_classmethod_s_base", classmethod[T|Any, Params, R], type_params=(T, Params, R))
    _staticmethod_s_base = TypeAliasType("_staticmethod_s_base", staticmethod[Params, R], type_params=(Params, R))
else:
    _classmethod_s_base = TypeAliasType("_classmethod_s_base", classmethod, type_params=(T, Params, R))
    _staticmethod_s_base = TypeAliasType("_staticmethod_s_base", staticmethod, type_params=(Params, R))

_instancemethod_base = TypeAliasType("_instancemethod_base", _instancemethod_c_base[T, Params, R], type_params=(T, Params, R))
_classmethod_base = TypeAliasType("_classmethod_base", _classmethod_c_base[T, Params, R] | _classmethod_s_base[T, Params, R], type_params=(T, Params, R))
_staticmethod_base = TypeAliasType("_staticmethod_base", _staticmethod_c_base[Params, R] | _staticmethod_s_base[Params, R], type_params=(Params, R))

_instancemethod_getter = TypeAliasType("_instancemethod_getter", _instancemethod_base[T, Params, R], type_params=(T, Params, R))
_instancemethod_setter = TypeAliasType("_instancemethod_setter", _instancemethod_base[T, Concatenate[S, Params], R], type_params=(T, S, Params, R))
_instancemethod_deleter = TypeAliasType("_instancemethod_deleter", _instancemethod_base[T, Params, R], type_params=(T, Params, R))

_classmethod_getter = TypeAliasType("_classmethod_getter", _classmethod_base[T, Params, R], type_params=(T, Params, R))
_classmethod_setter = TypeAliasType("_classmethod_setter", _classmethod_base[T, Concatenate[S, Params], R], type_params=(T, S, Params, R))
_classmethod_deleter = TypeAliasType("_classmethod_deleter", _classmethod_base[T, Params, R], type_params=(T, Params, R))

_staticmethod_getter = TypeAliasType("_staticmethod_getter", _staticmethod_base[Params, R], type_params=(Params, R))
_staticmethod_setter = TypeAliasType("_staticmethod_setter", _staticmethod_base[Concatenate[S, Params], R], type_params=(S, Params, R))
_staticmethod_deleter = TypeAliasType("_staticmethod_deleter", _staticmethod_base[Params, R], type_params=(Params, R))


_instancemethod_getter_default = TypeAliasType("_instancemethod_getter_default", _instancemethod_getter[T, [], R], type_params=(T, R))
_instancemethod_setter_default = TypeAliasType("_instancemethod_setter_default", _instancemethod_setter[T, S, [], None], type_params=(T, S))
_instancemethod_deleter_default = TypeAliasType("_instancemethod_deleter_default", _instancemethod_deleter[T, [], None], type_params=(T,))

_instancemethod_getter_cache = TypeAliasType("_instancemethod_getter_cache", _instancemethod_getter[T, [], R], type_params=(T, R))
_instancemethod_setter_cache = TypeAliasType("_instancemethod_setter_cache", _instancemethod_setter[T, S, [], R|_NoValueT], type_params=(T, R, S))
_instancemethod_deleter_cache = TypeAliasType("_instancemethod_deleter_cache", _instancemethod_deleter[T, [], bool], type_params=(T,))

_instancemethod_getter_introspect = TypeAliasType("_instancemethod_getter_introspect", _instancemethod_getter[T, [P], R], type_params=(T, R, P))
_instancemethod_setter_introspect = TypeAliasType("_instancemethod_setter_introspect", _instancemethod_setter[T, P, [S], None], type_params=(T, S, P))
_instancemethod_deleter_introspect = TypeAliasType("_instancemethod_deleter_introspect", _instancemethod_deleter[T, [P], None], type_params=(T, P))

_instancemethod_getter_cache_introspect = TypeAliasType("_instancemethod_getter_cache_introspect", _instancemethod_getter[T, [P], R], type_params=(T, R, P))
_instancemethod_setter_cache_introspect = TypeAliasType("_instancemethod_setter_cache_introspect", _instancemethod_setter[T, P, [S], R|_NoValueT], type_params=(T, R, S, P))
_instancemethod_deleter_cache_introspect = TypeAliasType("_instancemethod_deleter_cache_introspect", _instancemethod_deleter[T, [P], bool], type_params=(T, P))


_classmethod_getter_default = TypeAliasType("_classmethod_getter_default", _classmethod_getter[T, [], R], type_params=(T, R))
_classmethod_setter_default = TypeAliasType("_classmethod_setter_default", _classmethod_setter[T, S, [], None], type_params=(T, S))
_classmethod_deleter_default = TypeAliasType("_classmethod_deleter_default", _classmethod_deleter[T, [], None], type_params=(T,))

_classmethod_getter_cache = TypeAliasType("_classmethod_getter_cache", _classmethod_getter[T, [], R], type_params=(T, R))
_classmethod_setter_cache = TypeAliasType("_classmethod_setter_cache", _classmethod_setter[T, S, [], R|_NoValueT], type_params=(T, R, S))
_classmethod_deleter_cache = TypeAliasType("_classmethod_deleter_cache", _classmethod_deleter[T, [], bool], type_params=(T,))

_classmethod_getter_introspect = TypeAliasType("_classmethod_getter_introspect", _classmethod_getter[T, [P], R], type_params=(T, R, P))
_classmethod_setter_introspect = TypeAliasType("_classmethod_setter_introspect", _classmethod_setter[T, P, [S], None], type_params=(T, S, P))
_classmethod_deleter_introspect = TypeAliasType("_classmethod_deleter_introspect", _classmethod_deleter[T, [P], None], type_params=(T, P))

_classmethod_getter_cache_introspect = TypeAliasType("_classmethod_getter_cache_introspect", _classmethod_getter[T, [P], R], type_params=(T, R, P))
_classmethod_setter_cache_introspect = TypeAliasType("_classmethod_setter_cache_introspect", _classmethod_setter[T, P, [S], R|_NoValueT], type_params=(T, R, S, P))
_classmethod_deleter_cache_introspect = TypeAliasType("_classmethod_deleter_cache_introspect", _classmethod_deleter[T, [P], bool], type_params=(T, P))


_staticmethod_getter_default = TypeAliasType("_staticmethod_getter_default", _staticmethod_getter[[], R], type_params=(R,))
_staticmethod_setter_default = TypeAliasType("_staticmethod_setter_default", _staticmethod_setter[S, [], None], type_params=(S,))
_staticmethod_deleter_default = TypeAliasType("_staticmethod_deleter_default", _staticmethod_deleter[[], None], type_params=())

_staticmethod_getter_cache = TypeAliasType("_staticmethod_getter_cache", _staticmethod_getter[[], R], type_params=(R,))
_staticmethod_setter_cache = TypeAliasType("_staticmethod_setter_cache", _staticmethod_setter[S, [], R|_NoValueT], type_params=(R, S))
_staticmethod_deleter_cache = TypeAliasType("_staticmethod_deleter_cache", _staticmethod_deleter[[], bool], type_params=())

_staticmethod_getter_introspect = TypeAliasType("_staticmethod_getter_introspect", _staticmethod_getter[[P], R], type_params=(R, P))
_staticmethod_setter_introspect = TypeAliasType("_staticmethod_setter_introspect", _staticmethod_setter[P, [S], None], type_params=(S, P))
_staticmethod_deleter_introspect = TypeAliasType("_staticmethod_deleter_introspect", _staticmethod_deleter[[P], None], type_params=(P,))

_staticmethod_getter_cache_introspect = TypeAliasType("_staticmethod_getter_cache_introspect", _staticmethod_getter[[P], R], type_params=(R, P))
_staticmethod_setter_cache_introspect = TypeAliasType("_staticmethod_setter_cache_introspect", _staticmethod_setter[P, [S], R|_NoValueT], type_params=(R, S, P))
_staticmethod_deleter_cache_introspect = TypeAliasType("_staticmethod_deleter_cache_introspect", _staticmethod_deleter[[P], bool], type_params=(P,))
