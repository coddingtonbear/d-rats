D-Rats
======

Note: This software was **not** written by me; this was originally fetched from the [D-Rats Yahoo Group](https://groups.yahoo.com/neo/groups/d-rats_group/files/D-RATS%20Program%20Files/) and exists here only to provide a venue for fixes and changes.


Vague Instructions for installation on OSX
------------------------------------------

* When creating your virtualenv, use the system Python.
* Install PyGTK 2.0
    * `brew install --env=std --verbose --with-libglade pygtk`
    * Link into the virtualenv:
        * `ln -s /usr/local/lib/python2.7/site-packages/glib/ lib/python2.7/site-packages/`
        * `ln -s /usr/local/lib/python2.7/site-packages/gobject/ lib/python2.7/site-packages/`
        * `ln -s /usr/local/lib/python2.7/site-packages/gtk-2.0* lib/python2.7/site-packages/`
        * `ln -s /usr/local/lib/python2.7/site-packages/pygtk* lib/python2.7/site-packages/`
        * `ln -s /usr/local/lib/python2.7/site-packages/cairo lib/python2.7/site-packages/`
* Install libxml2
    * `brew install libxml2`
    * `echo /usr/local/opt/libxml2/lib/python2.7/site-packages >> lib/python2.7/site-packages/libxml2.pth`
* libxslt
    * `brew install libxslt`
    * `echo /usr/local/opt/libxslt/lib/python2.7/site-packages >> lib/python2.7/site-packages/libxslt.pth`
