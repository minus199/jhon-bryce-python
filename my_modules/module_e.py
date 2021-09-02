def foo(special, *args, param_b="bar", param_a="foo", **kw):
    for arg in args:
        print(arg)
    if kw.get('fuzz'):
        return

    print(kw['fuzz'])
    # return [special, param_a * 10, param_b.upper()]


data = {
    'param_a': "%%%%%%",
    'fuzz': "!!!!!!!"
}
letters = ["a", "b", "c"]

output1 = foo("special value", "a", "b", "c", **data)
output = foo(param_a="this_is_a", param_b="this_is_b")

print(output)
