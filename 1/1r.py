# -*- coding: utf-8 -*-

class ELGExampleOne(object):

    BASE_VARIABLE_1 = "Your problem with Vim is that you don't grok vi"
    BASE_VARIABLE_2 = "Think in terms of verbs, prepositions, and nouns."
    BASE_VARIABLE_3 = "SYOY!"

    def __init__(self, exampleA):
        """ This header has been changed.

        """
        self.yelp_brands = ["eat24", "seatme", "nowait", "yelp"]

    def print_base_variables(self):
        print(BASE_VARIABLE_1)
        print(BASE_VARIABLE_2)
        print(BASE_VARIABLE_3)
