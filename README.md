# Newton Basins Python Implementation

A tiny Python package to generate newton basins images.


## Installation

### From PyPI
```
pip install nb-py
```

### From source code

```
pip install git+https://github.com/gmagno/nb-py.git
```

or

```
git clone git@github.com:gmagno/nb-py.git
cd nb-py/
make install
```

## Example Usage

Just run:

```
import matplotlib as mpl  # don't forget to `pip install matplotlib` first
import matplotlib.pyplot as plt
import nb_py
hsv = nb_py.compute(
    imw=32, imh=32, # for more details, run: help(nb_py.compute)
)
rgb = mpl.colors.hsv_to_rgb(hsv)
plt.figure()
plt.imshow(rgb)
plt.show()
```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
