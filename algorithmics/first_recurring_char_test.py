# Copyright 2020 Daniel J. Beutel. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


import unittest

from algorithmics.first_recurring_char import first_recurring_char


class Test(unittest.TestCase):
    def test_first_recurring_char_found(self):
        # Prepare
        s = "DBCABA"
        expected = "B"
        # Execute
        actual = first_recurring_char(s)
        # Assert
        assert actual == expected

    def test_first_recurring_char_not_found(self):
        # Prepare
        s = "DBCA"
        expected = None
        # Execute
        actual = first_recurring_char(s)
        # Assert
        assert actual == expected

    def test_first_recurring_char_found_min(self):
        # Prepare
        s = "AA"
        expected = "A"
        # Execute
        actual = first_recurring_char(s)
        # Assert
        assert actual == expected


if __name__ == "__main__":
    unittest.main()
