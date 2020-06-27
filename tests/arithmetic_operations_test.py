import numpy as np

import vaex


def test_chain_floor_divide_and_mod():
    time = np.array([1200, 1500, 1830, 1245, 1115])
    df = vaex.from_arrays(time=time)
    df['hour'] = ((df.time // 100) % 24) + ((df.time % 100) / 60)
    assert df[['hour']].values.tolist() == [[12.0], [15.0], [18.5], [12.75], [11.25]]
