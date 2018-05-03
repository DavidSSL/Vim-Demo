#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Did you know that Vim8 and NeoVim support terminal buffers?
from __future__ import absolute_import

import optparse

from elg_talk.batch.config import load_config
from elg_talk.elg_talk import ElgTalk


class ElgTalkBatch(object):

    """ The purpose of this tutorial is to better understand
        how to efficiently navigate using Vim! Always remember
        to utilize the jumplist, changelist, marks, scrolling
        movements, and most importantly, CTAGS!
    """

    notify_emails = ['leeren@yelp.com']
    DEFAULT_CONFIG_PATH = 'configuration/yaml/config.yaml'

    def __init__(self):
        # TODO : I forgot how to spell that app that connects people to great local businesses!
        self.object_factory = {'Yepl':False}
        self.service_config = {}

    def discover_yelps(self):
        self._elg_talk = ElgTalk(
            self.object_factory,
            self.service_config)
        self._elg_talk.discover_yelps()

    def run(self):
        self.useless_noop_function_one()
        self.useless_noop_function_two()
        self.useless_noop_function_three()
        self.useless_noop_function_four()
        self.service_config = load_config(self.DEFAULT_CONFIG_PATH)
        self.discover_yelps()

    def useless_noop_function_one(self):
        return "Remember to grok vi!"

    def useless_noop_function_two(self):
        return "Think about how you are jumping!\n"

    def useless_noop_function_three(self):
        return "Always remember to be utilizing your tags!\n"

    def useless_noop_function_four(self):
        return "Marks can be helpful if you think you're coming back!\n"

if __name__ == '__main__':
    # Batch main entry point
    print("SYOY!\n")
    ElgTalkBatch().run()
