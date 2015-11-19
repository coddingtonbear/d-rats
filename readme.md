D-Rats
======

Note: This software was **not** written by me; this was originally fetched from the [D-Rats Yahoo Group](https://groups.yahoo.com/neo/groups/d-rats_group/files/D-RATS%20Program%20Files/) and exists here only to provide a venue for fixes and changes.


Special Requirements
--------------------

* PyGTK 2.0
    * With `libglade`: `brew install --verbose --with-libglade pygtk`
    * Link into the virtualenv:
        * ln -s /usr/lib/python2.7/dist-packages/glib/ lib/python2.7/dist-packages/
        * ln -s /usr/lib/python2.7/dist-packages/gobject/ lib/python2.7/dist-packages/
        * ln -s /usr/lib/python2.7/dist-packages/gtk-2.0* lib/python2.7/dist-packages/
        * ln -s /usr/lib/python2.7/dist-packages/pygtk.pth lib/python2.7/dist-packages/
        * ln -s /usr/lib/python2.7/dist-packages/cairo lib/python2.7/dist-packages/
* libxml2
    * Link into the virtualenv
