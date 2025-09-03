from propert import propert

def test_basic_shorthands() -> None:
    class Test:
        @propert.auto
        def expl_auto_property(self_or_cls):
            return self_or_cls

        @propert.cls
        def expl_cls_property(cls):
            return 99

        @propert.static
        def expl_static_property():
            return 100

        @propert
        def auto_class_property(cls):
            return cls

        @propert
        def auto_static_property():
            return 101


    assert Test.expl_cls_property == 99
    assert Test.expl_static_property == 100
    assert Test.expl_auto_property == Test
    assert Test.auto_class_property == Test
    assert Test.auto_static_property == 101

    inst = Test()
    assert inst.expl_cls_property == 99
    assert inst.expl_static_property == 100
    assert inst.expl_auto_property == inst
    assert inst.auto_class_property == Test
    assert inst.auto_static_property == 101

def test_classmethod_shorthand() -> None:
    class Test:
        @propert.cls
        def class_property(cls):
            return cls

    assert Test.class_property == Test