# -*- coding: utf-8 -*-
from __future__ import absolute_import

class ElgTalk():

    """ The purpose of this talk is to better understand 
        navigation in vim! Remember to always utilize the
        following:
         - H / M / L for sectional screen navigation (high / mid / low)
         - Ctrl + (d / u / f / b) to scroll (down / up / fwd / backward)
         - Marks! Set via m{a-zA-Z}, go via'{a-zA-Z} or `{a-zA-Z}
         - Special marks! i.e. '. or `. goes to your latest change
         - Utilize the jumplist via <Ctrl-I/O> or look via :ju[umps]
         - Jumps include marks, 'G', searches, tags, H/M/L, and editing new files!
         - Utilize the changelist via g, and g; or look via :changes
         - Utilize the tag stack via Ctrl-] or look via :tags
    """

    def __init__(self, object_factory, config):
        self._yelp = object_factory
        self._brands = config["brands"]

    def discover_yelps(self):
        if 'yelp' not in self._yelp or not self._yelp['yelp']:
            print('Yelp is MEDIOCRE!\n')
        else:
            print('Yelp is AWESOME!\n')
        print('These are the Yelp brands:\n')
        for brand in self._brands:
            print(brand)
