"""Alternative word count plugin class for novelibre.

Requires Python 3.7+
Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_character_counter
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""
from nvcharcnt.character_counter import CharacterCounter
from nvlib.controller.plugin.plugin_base import PluginBase


class Plugin(PluginBase):
    """Alternative word count plugin class."""
    VERSION = '@release'
    API_VERSION = '5.30'
    DESCRIPTION = 'Replace word count with character count'
    URL = 'https://github.com/peter88213/nv_character_counter'

    def install(self, model, view, controller):
        """Install the plugin.
        
        Positional arguments:
            model -- reference to the novelibre main model instance.
            view -- reference to the novelibre main view instance.
            controller -- reference to the novelibre main controller instance.

        Extends the superclass method.
        """
        super().install(model, view, controller)
        self._mdl.nvService.change_word_counter(CharacterCounter())

