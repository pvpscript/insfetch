from typing import List, Dict, Any

class AutorefferingAttributes:
    def __init__(self, cls):
        self._cls = cls

    def _split_dict(self, ref_dict):
        return next((k, v) for k, v in ref_dict.items())

    def __call__(self, *args, **kwargs):
        attributes: List[str] = self._cls.__attributes__
        dict_attributes: List[dict] = self._cls.__dict_attributes__
        ref_dict: Dict[str, Any] = kwargs.pop('__ref__', None)

        instance = self._cls(*args, **kwargs)

        if attributes is not None and ref_dict is not None:
            for attr in attributes:
                if attr in ref_dict.keys():
                    setattr(instance, attr, ref_dict[attr])

        if dict_attributes is not None and ref_dict is not None:
            for attr in dict_attributes:
                orig_attr, new_attr = self._split_dict(attr)

                if orig_attr in ref_dict.keys():
                    setattr(instance, new_attr, ref_dict[orig_attr])

        return instance
