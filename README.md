# 🍵 `@propert` - Static and class-level properties in python

## ⚙️ Features

You may know the `@property` decorator in python, which sadly does not work with static and class methods.

Introducing `@propert` - a small library to add static and class-level properties to your code:

```python
from propert import classproperty, staticproperty

class Test:
    @classproperty
    def class_prop(cls):
        return ...

    @staticproperty
    def static_prop():
        return ...
```

### 📝 Overview

 - 🛠️ properties for [class and static methods](#-static--class--and-autoproperties)
 - 🔀 properties getting called on both instance and class level (see [`@autoproperty`](#-static--class--and-autoproperties))
 - 🌟 custom [setters and deleters](#%EF%B8%8F-setters-and-deleters)
 - 📦 [cached](#-cached-properties) and [introspected](#-introspection) properties
 - 🤏 versatile and powerful [shorthands](#-shorthands)
 - 🤸‍♂️ highly flexible [syntax](#-your-code-your-style)
 - ⚔️ decent type-checking support (see [below](#-type-checking-and-mypy))

### 🏷️ Setters and Deleters

All properties provided by this library support setters and deleters:

```python
class Test:
    @classproperty
    def class_prop(cls):
        return ...

    @class_prop.setter
    def class_prop(cls, value: ...):
        ...

    @class_prop.deleter
    def class_prop(cls):
        ...

x = Test.class_prop # calls getter
Test.class_prop = x # calls setter
del Test.class_prop # calls deleter
```

### 📦 Cached Properties

There are cached properties equivalent to the `@cached_property` in the `functools` library:

```python
from propert import cached_classproperty, cached_staticproperty

class Test:
    @cached_classproperty
    def cached_class_prop(cls):
        return ...

    @cached_staticproperty
    def cached_static_prop():
        return ...
```

A custom setter on a cached property can return a value that will be saved in the cache. Alternatively, it can return `propert.CACHE_RESET` to reset the cache or `propert.NO_VALUE` to not change the cache.

Calling `del Tes.cached_class_prop` will reset the cached value by default causing the property to be re-evaluated on the next access. A custom deleter for a cached property should return `True` to reset the cache or `False` to leave the cache unchanged. This allows conditional cache invalidation.

### 🔎 Introspection

There is a special type of properties that can be used to introspect the property when a getter, setter or deleter is called:

```python
from propert import introspected_classproperty, introspected_staticproperty

class Test:
    @introspected_classproperty
    def class_prop(cls, prop):
        prop._some_internal_var = 42
        return ...

    @introspected_staticproperty
    def static_prop(prop):
        prop._some_internal_var = 42
        return ...
```

This behaviour can be useful if you want to declare custom property subclasses meant for decorating methods requiring access to the property object itself.


### 🤏 Shorthands

You can also use shorthands to avoid importing and typing the full name of each decorator:

```python
from propert import propert

class Test:
    @propert
    def class_prop(cls):
        return ...

    @propert
    def static_prop():
        return ...

    @propert.cached
    def cached_class_prop(cls):
        return ...

    @propert.cached
    def cached_static_prop():
        return ...
```

This will automatically determine if the property is a class or static property based on the number of arguments.

### 💎 Static-, Class- and Autoproperties


|                        |   `@staticproperty`   |   `@classproperty`   |   `@autoproperty`   |
|------------------------|-----------------------|----------------------|---------------------|
| Syntax                 | `def prop(): ...`     | `def prop(cls): ...` | `def prop(cls_or_self): ...` |
| `x = Test.prop`        |                       | `cls = Test`         | `cls_or_self = Test` |
| `x = Test().prop`      |                       | `cls = Test`         | `cls_or_self = Test()` |
|                        |                       |                      |                     |
| Supports Cache         | ✅                     | ✅                    | ✅ (instance and class share cache) |
| Supports Introspection | ✅                     | ✅                    | ✅                   |
| Supported by `@propert` shorthand | ✅          | ✅                    | ❌                   |


### 🎨 Your code, your style

Every syntax you can think of is supported with `propert` to suit your needs.
For example, all of these are valid ways to create a cached class property:

```python
class Test:
    @propert(cached=True)
    def prop(cls):
        return ...

    @propert.cached
    def prop(cls):
        return ...

    @classproperty(cached=True)
    def prop(cls):
        return ...

    @cached_classproperty
    def prop():
        return ...

    prop = propert(lambda cls: ..., cached=True)
    prop = propert.cached(lambda cls: ...)
    prop = classproperty(lambda cls: ..., cached=True)
    prop = cached_classproperty(lambda cls: ...)
```

Or let's say your entire project uses the `@propert.introspected` shorthand and now you need an introspected class property that is also cached:

```python
class Test:
    @propert.introspected
    def prop_1(cls, prop):
        return ...

    @propert.introspected
    def prop_2(cls, prop):
        return ...

    @propert.introspected(cached=True)
    def prop_cached(cls, prop):
        return ...

    @propert.introspected
    def prop_3(cls, prop):
        return ...
```

Blends right in, doesn't it?

### 📊 Type Checking and MyPy

#### Classmethod/Staticmethod

If you are planning to use this library with mypy, you may need to add `@classmethod` or `@staticmethod` between the decorator and the property method, like this:

```python
class Test:
    @classproperty
    @classmethod
    def class_property(cls):
        return ...

    @staticproperty
    @staticmethod
    def static_property():
        return ...

    @classproperty
    def class_property_instance(cls):
        # will work, but mypy will assume that cls: Self@Test instead of cls: Type[Self@Test]
        return ...
```

Using a classmethod will also solve the issue, that type checkers show the wrong type annotation in the method of a classproperty: `cls: Self@Test` instead of `cls: Type[Self@Test]`, even though at runtime, the type will be `Type[Test]`.

#### Redefinition

Additionally, when using custom setters and deleters, you may run into a redefinition error. You can solve that error in three ways:

```python
class Test:
    @classproperty
    def class_prop(cls):
        return ...

    # 1. Use and underscore as the function name for setters and deleters
    @class_prop.setter
    def _(cls, value: ...):
        ...

    @class_prop.deleter
    def _(cls):
        ...

    # 2. Suppress the redefinition error
    @class_prop.setter # type: ignore[no-redef]
    def class_prop(cls, value: ...):
        ...

    # 3. Use a different function name for setters and deleters (not recommended)
    @class_prop.setter
    def class_prop_set(cls, value: int) -> None:
        pass

    @class_prop.deleter
    def class_prop_del(cls) -> None:
        pass
```

#### Invalid Assignment

Finally, when using setters, mypy will not allow you to assign to the property, because it thinks that it is a method (and/or a property object of some sort). You can suppress this warning by using `# type: ignore[assignment, method-assign]`.

#### Runtime

The library itself will still work without the `@classmethod` or `@staticmethod` decorators, but mypy and type-checking may show warnings. The same applies for the "redefinitions" and "method assignments", which are properly resolved at runtime but may cause issues with type-checking.

#### Plugin

In the future, a mypy plugin might be added, but this will require at least the following PR to be merged: https://github.com/python/mypy/pull/9925

## 💻 Development

### 📁 Code structure

The code is structured as follows:

- `src/propert/` contains the source code
- `tests/` contains the tests
- `tests/test_mypy.py` contains the mypy tests

Most of the actual logic is in the `src/propert/base.py` and `src/propert/meta.py` files.
The `src/propert/common.py` file contains some values that are used by both files.
All remaining files primarily contain type hints and some decision logic for the shorthands they represent.

### 📦 Distribution

To build the package, you can do the following:

```bash
uv run build
```

<details>
<summary>Publishing</summary>

> [!NOTE]
> This section is primarily relevant for the maintainers of this package (me), as it requires permission to push a package to the `propert` repository on PyPI.

```bash
uv run publish --token <token>
```

</details>

### 🎯 Tests

To run all tests, you can do the following:

```bash
uv run pytest
uv run mypy src tests/test_mypy.py
```
