import math
import random
import logging
import argparse
import numpy as np

# Constants
NSRC = 1_000_000

# Configure logging
logging.basicConfig(format="%(name)s:%(levelname)s %(message)s", level=logging.INFO)
log = logging.getLogger("sky_sim")

def get_radec():
    """
    Generate the ra/dec coordinates of Andromeda
    in decimal degrees.

    Returns
    -------
    ra : float
        The RA, in degrees, for Andromeda
    dec : float
        The DEC, in degrees for Andromeda
    """
    log.debug("Entering get_radec()")
    # from wikipedia
    andromeda_ra = '00:42:44.3'
    andromeda_dec = '41:16:09'

    degrees, minutes, seconds = andromeda_dec.split(':')
    dec = int(degrees) + int(minutes) / 60 + float(seconds) / 3600

    hours, minutes, seconds = andromeda_ra.split(':')
    ra = 15 * (int(hours) + int(minutes) / 60 + float(seconds) / 3600)
    ra = ra / math.cos(dec * math.pi / 180)
    
    log.debug("Exiting get_radec()")
    return ra, dec

def crop_to_circle(ras, decs, ref_ra, ref_dec, radius):
    """
    Crop an input list of positions so that they lie within radius of
    a reference position.

    Parameters
    ----------
    ras, decs : list(float)
        The ra and dec in degrees of the data points.
    ref_ra, ref_dec: float
        The reference location.
    radius: float
        The radius in degrees.

    Returns
    -------
    ra_out, dec_out : list
        A list of ra and dec coordinates that pass our filter.
    """
    log.debug("Entering crop_to_circle()")
    ra_out = []
    dec_out = []
    for i in range(len(ras)):
        if (ras[i] - ref_ra) ** 2 + (decs[i] - ref_dec) ** 2 < radius ** 2:
            ra_out.append(ras[i])
            dec_out.append(decs[i])
    log.debug("Exiting crop_to_circle()")
    return ra_out, dec_out

def make_stars(ra, dec, nsrc=NSRC):
    log.debug("Entering make_stars()")
    ras = [random.uniform(ra - 1, ra + 1) for _ in range(nsrc)]
    decs = [random.uniform(dec - 1, dec + 1) for _ in range(nsrc)]
    
    ras, decs = crop_to_circle(ras, decs, ra, dec, 1.0)
    log.debug("Exiting make_stars()")
    return ras, decs

def skysim_parser():
    """
    Configure the argparse for skysim.

    Returns
    -------
    parser : argparse.ArgumentParser
        The parser for skysim.
    """
    log.debug("Entering skysim_parser()")
    parser = argparse.ArgumentParser(prog='sky_sim', prefix_chars='-')
    parser.add_argument('--ra', dest='ra', type=float, default=None,
                        help="Central ra (degrees) for the simulation location")
    parser.add_argument('--dec', dest='dec', type=float, default=None,
                        help="Central dec (degrees) for the simulation location")
    parser.add_argument('--out', dest='out', type=str, default='catalog.csv',
                        help='Destination for the output catalog')
    parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')
    log.debug("Exiting skysim_parser()")
    return parser

if __name__ == "__main__":
    parser = skysim_parser()
    options = parser.parse_args()

    if options.verbose:
        log.setLevel(logging.DEBUG)
    
    log.info("Starting sky_sim")

    if None in [options.ra, options.dec]:
        ra, dec = get_radec()
    else:
        ra = options.ra
        dec = options.dec

    ras, decs = make_stars(ra, dec)

    with open(options.out, 'w', encoding='utf8') as f:
        print("id,ra,dec", file=f)
        for i in range(min(len(ras), len(decs))):
            print(f"{i:07d}, {ras[i]:12f}, {decs[i]:12f}", file=f)
    
    log.info(f"Wrote {options.out}")
    log.info("Finished sky_sim")
