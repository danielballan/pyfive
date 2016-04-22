
import numpy as np
from numpy.testing import assert_array_equal

import pyfive
import h5py

def test_read_basic_example():

    # reading with HDF5
    hfile = h5py.File('basic_example.hdf5', 'r')
    assert hfile['/example'].attrs['foo'] == 99.5
    assert hfile['/example'].attrs['bar'] == 42
    np.testing.assert_array_equal(
        hfile['/example'][:],
        np.arange(100, dtype='int32'))
    assert hfile['/example'].dtype == np.dtype('int32')
    assert hfile['/example'].shape == (100, )
    hfile.close()

    # reading with pyfive
    hfile = pyfive.HDF5File('basic_example.hdf5')
    assert 'example' in hfile.datasets

    dset = hfile.datasets['example']

    attrs = dset.get_attributes()
    assert 'bar' in attrs
    assert 'foo' in attrs
    assert attrs['bar'] == 42
    assert attrs['foo'] == 99.5

    data = dset.get_data()
    assert data.dtype == np.dtype('int32')
    assert data.shape == (100, )
    assert_array_equal(data, np.arange(100, dtype='int32'))

    hfile.close()

