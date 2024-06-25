import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_module_import():
    from mymodule.sky_sim import get_radec
    expected_ra = 14.215420962967535
    expected_dec = 41.26916666666667
        
    ra, dec = get_radec()
        
    assert abs(ra - expected_ra) < 1e-10, f"RA value is incorrect: {ra} != {expected_ra}"
    assert abs(dec - expected_dec) < 1e-10, f"Dec value is incorrect: {dec} != {expected_dec}"
