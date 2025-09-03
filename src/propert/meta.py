from typing_extensions import Type, Any, TYPE_CHECKING

from .common import _propert_setters_name, _propert_deleters_name
from .base import _base_property
from .types import T

_propert_meta_cache = dict[tuple[Type[type], bool, bool], Type[type]]()
def _create_propert_meta(base_meta: Type[type]=type, *, enable_setters: bool = False, enable_deleters: bool = False) -> Type[type]:
    _key = (base_meta, enable_setters, enable_deleters)

    _cached = _propert_meta_cache.get(_key, None)
    if _cached is not None:
        return _cached

    class _PropertMeta(base_meta): # type: ignore
        def __init__(self, name: str, bases: tuple[type, ...], namespace: dict[str, Any], /, **kwargs: Any) -> None:
            super().__init__(name, bases, namespace, **kwargs)

            self.__propert_setters_enabled__ = getattr(self, _propert_setters_name, enable_setters)
            self.__propert_deleters_enabled__ = getattr(self, _propert_deleters_name, enable_deleters)

        def __setattr__(self, name: str, value: Any, /) -> None:
            if getattr(self, _propert_setters_name, False):
                old_value = self.__dict__.get(name, None)
                if isinstance(old_value, _base_property):
                    old_value._set(None, self, value)
                    return
            super().__setattr__(name, value)

        def __delattr__(self, name: str, /) -> None:
            if self.__propert_deleters_enabled__:
                old_value = self.__dict__.get(name, None)
                if isinstance(old_value, _base_property):
                    old_value._del(None, self)
                    return
            super().__delattr__(name)

    _propert_meta_cache[_key] = _PropertMeta
    return _PropertMeta

def _try_enable_feature(cls: Type[T], name: str, enable: bool, *, force_disable: bool = False) -> bool:
    """
    Try enabling a setter/deleter/... feature for a class. If force_disable is set to true, it also allows disabling the feature, otherwise it will only try to enable it.
    Only works, when the class already inherits from a class that allows enabling/disabling the feature (see `_create_propert_meta(...)` for more info)
    Returns whether it was successful or if the class must be patched with the metaclass first
    """
    # If we are not forcing the feature to be disabled and we are not trying to disable the feature, return True to indicate success
    if not force_disable and not enable:
        return True

    # Check if the feature is already enabled
    is_enabled = getattr(cls, name, None)

    # If the feature is not even present, return False to indicate that the class must be patched with the metaclass first
    if is_enabled is None:
        return False

    # Enable the feature if it is not already enabled (or disable it if it is not already disabled, only ever called when `force_disable=True`)
    if is_enabled != enable:
        setattr(cls, name, enable)

    # Return True to indicate success
    return True

_propert_cls_cache = dict[tuple[type, bool, bool], type]()
def _patch_propert_meta_into_class(cls: Type[T], *, enable_setters: bool = False, enable_deleters: bool = False, force_disable: bool = False) -> Type[T]:
    """Enable the given features for the given class. Patches and returns a new class if necessary."""
    must_create_meta = (
        not _try_enable_feature(cls, _propert_setters_name, enable_setters, force_disable=force_disable) or 
        not _try_enable_feature(cls, _propert_deleters_name, enable_deleters, force_disable=force_disable)
    )

    if not must_create_meta:
        return cls
    
    _key = (cls, enable_setters, enable_deleters)

    new_cls = _propert_cls_cache.get(_key, None)
    
    if new_cls is not None:
        return new_cls

    new_meta = _create_propert_meta(type(cls), enable_setters=enable_setters, enable_deleters=enable_deleters)
    new_cls = new_meta(cls.__name__, (cls,), {})

    _propert_cls_cache[_key] = new_cls
    return new_cls

def enable_propert_setters(cls: Type[T], /) -> Type[T]:
    """Return a new class with the propert setters (@your_propert.setter) enabled."""
    return _patch_propert_meta_into_class(cls, enable_setters=True)

def enable_propert_deleters(cls: Type[T], /) -> Type[T]:
    """Return a new class with the propert deleters (@your_propert.deleter) enabled."""
    return _patch_propert_meta_into_class(cls, enable_deleters=True)

def enable_propert_modifications(cls: Type[T], /) -> Type[T]:
    """Return a new class with all propert modifications (e.g. @your_propert.setter and @your_propert.deleter) enabled."""
    return _patch_propert_meta_into_class(cls, enable_setters=True, enable_deleters=True)

if TYPE_CHECKING:
    PropertMeta = type
else:
    PropertMeta = _create_propert_meta(enable_setters=True, enable_deleters=True)
class PropertBase(metaclass=PropertMeta): """Base class for classes that use propert to enable setter and deleter features for class- and staticproperties provided by propert."""
