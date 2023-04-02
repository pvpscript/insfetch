def chained_get(dict_data, chain):
    if dict_data is None or len(chain) < 1:
        return None

    if len(chain) == 1:
        return dict_data.get(chain[0])

    return chained_get(dict_data.get(chain.pop(0)), chain)
