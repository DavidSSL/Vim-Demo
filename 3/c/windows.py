# -*- coding: utf-8 -*-
from __future__ import absolute_import

class Windows():

    """ Remember to utilize tabs, buffers, and windows properly!
        This class will talk specifically about windows.
        Windows are the the viewports for buffers.
        Windows should only be used to offer a desired view for sets of buffers.
         - Windows allow cartesian physical distribution of buffers via viewports
         - By utilizing Vim's splitting functionality you can easily glimpse more
           than one buffer at the same time (or even the same buffer) tailored
           to your viewing pleasures
         - An example use case is comparing the diff between two files like earlier
    """

    # TODO: Understand that windows are VIEWPORTS into buffers. They are for tailored viewing.
    def __init__(self):
        self._name = "WINDOWS"
        self._purpose = "Buffer viewports"

    # TODO: Remember to always :sp and :vs for horizontal and vertical splitting!
    def learn_windows(self):
        for (i in range(1, 100)):
            print("Windows help me get a better view of my files")
            print("Moving windows does not necessarily move files")
            print("Windows are viewports of files, not actual files")
            print('Yelp is AWESOME!\n')
