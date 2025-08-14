"""Provide an alternative strategy class for counting words.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_character_counter
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import re


class CharacterCounter:

    XML_PATTERN = re.compile(r'\<note\>.*?\<\/note\>|\<comment\>.*?\<\/comment\>|\<.+?\>')

    def get_word_count(self, text):
        """Return the total character count of text as an integer."""
        return len(self.XML_PATTERN.sub('', text.strip()))
