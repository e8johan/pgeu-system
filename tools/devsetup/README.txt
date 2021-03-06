Dependencies needed before running
----------------------------------

The following dependencies are required for manually rebuilding all the required
python modules. If using distribution packaged python modules most of them won't
be necessary, but then things usually just work out of the box and no need for
this script.

* virtualenv corresponding to python 3.5 (in path)
	* On debian, for example, this means virtualenv and python3-virtualenv packages
* c compiler and libs (typically build-essential)
* python development libraries (typically python-dev) -- for modules
* ffi development libraries (typically libffi-dev) -- for some modules
* openssl development libraries (typically libssl-dev) -- for crypto related modules
* libjpeg-dev and libpng-dev (*before* installing pillow in python)
* pg_config for postgresql, in path, for the correct version. Typically postgresql-dev package.
* libqrencode-dev
* uwsgi, uwsgi-plugin-python3


Database access
---------------

Access to the PostgreSQL database must work without password.


Other dependencies
------------------
For invoice generation to work, DejaVu needs to be installed in
/usr/share/fonts/truetype/ttf-dejavu/

On debian, just install ttf-dejavu.


macOS support
-------------
All required dependencies except virtualenv can be installed via Homebrew,
virtualenv is installed with pip.
