# -*- coding: utf-8 -*-
from __future__ import absolute_import

import staticconf


def load_config(config_path):
    """Reads the configuration from a YAML file located at
    `config_path`.
    """
    config = {}
    staticconf.YamlConfiguration(config_path)

    # Get all brands for the ELG talk
    config['brands'] = staticconf.read('brands')

    return config
