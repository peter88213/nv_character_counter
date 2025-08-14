"""Provide an alternative strategy class for counting words.

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/novelibre
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""


class CharacterCounter:

    def get_word_count(self, text):
        """Return the total character count of text as an integer."""
        return len(text)
