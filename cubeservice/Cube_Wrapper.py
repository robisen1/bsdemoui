import hashlib
import cPickle as pickle
import numpy


def get_group_key(cube):
    if 'Unknown' in cube['Prediction']:
        return quantize_unknown_space(cube)

    return cube['Prediction']  # ML class type will map to: Vendor.Make.Model

def quantize_unknown_space(cube):
    fields_in_key = []
    for key in cube.keys():
        if 'Pulse' in key:
            fields_in_key.append(key)
        elif 'Wavelet' in key:
            fields_in_key.append(key)

    sorted(fields_in_key)

    # Create synthetic bins for a collection of ordered fields
    quantized_field_bins = []
    for key in fields_in_key:
        val = cube[key]
        if type(val) not in [str, list, dict, numpy.ndarray]:
            print type(val)
            quantized_field_bins.append(quantize_field(val))

    z = pickle.dumps(quantized_field_bins)
    return hashlib.md5(z).hexdigest()


def quantize_field(val):
    bin_id = int(val * 10)
    return bin_id