from typing import List, Dict, Any

class FilteredParams:
    def __init__(self, cls):
        self._cls = cls

    def __call__(self, *args, **kwargs):
        keys: List[str] = self._cls.__keys__
        ref_dict: Dict[str, Any] = kwargs.pop('__ref__', None)

        instance = self._cls(*args, **kwargs)

        if keys is not None and ref_dict is not None:
            for k in keys:
                if k in ref_dict.keys():
                    setattr(instance, k, ref_dict[k])

        return instance
