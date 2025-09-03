from typing_extensions import Type, TypeVar

T = TypeVar("T")

_propert_setters_name = "__propert_setters_enabled__"
_propert_deleters_name = "__propert_deleters_enabled__"

def _check_feature_enabled(cls: Type[T], name: str) -> bool:
    return getattr(cls, name, False)