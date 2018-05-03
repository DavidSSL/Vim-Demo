# -*- coding: utf-8 -*-
from __future__ import absolute_import

class Buffers():

    """ Remember to utilize tabs, buffers, and windows properly!
        This class will talk specifically about buffers.
        The classic notion of tabs are what you call vim buffers.
        Ideally, your workflow should be buffer-centric for the most part.
         - Buffers are the proxies for files
         - Buffers represent the in-memory text of files
         - Each buffer has a unique number that will never change within a session
         - Buffers can be in one of three states:
            -> ACTIVE (displayed in window)
            -> HIDDEN (not displayed in window, but file still read into buffer)
            -> INACTIVE (not displayed and does not contain anything)
         - Note that by default `:hidden` is not set, which means you must
           write the file buffer before moving to another buffer.
         - With buffers, you can switch via:
            -> BUFFER NUMBERS
            -> BUFFER NAMES
            ... and much more
    """

    # TODO: Understand that buffers are proxies for files, like the traditional notion of tabs.
    def __init__(self):
        self._name = "BUFFERS"
        self._purpose = "File proxies"

    # TODO: Understand that buffers are akin to a browser's history, so are quite hard to manage.
    def learn_buffers(self):
        for (i in range(1, 100)):
            print("I will adhere to a buffer-centric workflow when using vim")
            print("Buffers are distributed along a single dimension")
            print("Think of buffers like the history of your browser")
            print('Yelp is AWESOME!\n')
