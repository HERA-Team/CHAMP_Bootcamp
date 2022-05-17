import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from pyuvdata import UVData
from uvtools import plot

if __name__ == "__main__":
    plt.ion()
    
    # Load the sample data.
    this_dir = Path(".")
    test_file = list(this_dir.glob("*.uvh5"))[0]
    uvd = UVData()
    uvd.read(test_file)

    # Check that making a plot works.
    freqs = np.unique(uvd.freq_array)
    fselect = (freqs > 110e6) & (freqs < 190e6)
    uvd.select(frequencies=freqs[fselect])
    antpairpol = uvd.get_antpairpols()[0]
    fig, ax = plot.labeled_waterfall(uvd, antpairpol=antpairpol)
    plt.pause(5)
    plt.close()
