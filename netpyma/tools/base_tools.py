from typing import Any


class NullValue:
    """
    Null value is used to distinguish with None
    """

    def __str__(self):
        return 'NUL'


NUL = NullValue()


def kv_args(cls: type, inp: dict, **kwargs) -> dict[str, Any]:
    class_fields: dict[str, Any] = cls.__dataclass_fields__
    if not class_fields:
        raise Exception('Input is not type of dataclass')

    reskw: dict[str, Any] = {}
    for fld in class_fields.keys():
        cfgval = inp.get(fld, NUL)
        argval = kwargs.get(fld, NUL)
        if callable(argval):
            # Function for change default value
            reskw[fld] = argval(cfgval)
            continue
        if cfgval != NUL:
            # Get value from input directly
            reskw[fld] = cfgval
            continue
        if argval != NUL:
            reskw[fld] = argval
    return reskw


############################################################
######################## Deprecated ########################

def get_kvals(dic: dict, *args: list[str]):
    result: dict[str, object] = {}
    for arg in args:
        value = dic.get(arg)
        if value != None:
            result[arg] = value
    return result


def get_kargs(dic: dict, *args: list[str]):
    result = []
    for arg in args:
        result.append(dic.get(arg))
    return result


def get_args(lst: list, lenght):
    result = []
    i = 0
    l = len(lst)
    while i < lenght:
        if i < l:
            result.append(lst[i])
        else:
            result.append(None)
        i += 1
    return result
