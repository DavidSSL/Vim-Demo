# -*- coding: utf-8 -*-
from __future__ import absolute_import

class Tabs():

    """ Remember to utilize tabs, buffers, and windows properly!
        This class will talk specifically about tabs.
        With a purely one-tab one-buffer workflow, you will have a hard time.
         - Tabs are meant to be the primary containers for bigger workspaces.
         - Tabs are specifically designed for containing windows (which hold buffers)
         - You should use tabs as a means of separating disparate workspaces
         - `:tabs` allows you to inspect all opened tabs
         - Use gt to go back to the next tab, and gT to go to the previous tab
         - `:tabc` to close a tab, and `:tabn` to add a new tab
         - `:tabdo {command}` allows execution of an ex command across all tabs
         SYOY
    """

    # TODO: Understand that VIM tabs != classical understanding of tabs
    def __init__(self):
        self._name = "TABS"
        self._purpose = "Window container"

    # TODO: Remember to only use tabs as a means of window multiplexing!
    def learn_tabs(self):
        for (i in range(1, 100)):
            print("I will NOT create a new tab for every new file I edit")
            print("I will always remember to use tabs as a window multiplexer")
            print('Yelp is AWESOME!\n')
