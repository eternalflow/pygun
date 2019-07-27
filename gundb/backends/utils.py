from collections import defaultdict

def uniquify(lst):
    res = []
    for item in lst:
        if not item in res:
            res.append(item)
    return res

def fix_lists(obj):
    if not isinstance(obj, dict):
        return obj
    res = {}
    for k, v in obj.items():
        if k.startswith('list_'):
            res[k] = listify(fix_lists(v))
        else:
            res[k] = fix_lists(v)
    return res

def listify(attr):
    if isinstance(attr, dict):
        return uniquify(fix_lists(attr).values())
    else:
        return attr

def get_first_list_prop(lst):
    for i, e in enumerate(lst):
        if e.startswith('list_'):
            return i
    return -1

rec_dd = lambda: defaultdict(rec_dd)

def defaultify(d):
    "Converts a dict to a nested default dicts"
    res = defaultdict(rec_dd)

    for k, v in d.items():
        if isinstance(v, dict):
            res[k] = defaultify(v)
        else:
            res[k] = v
    return res
