"""Tests for `mbed_targets`."""

import unittest
import mock

# Import from top level as this is the expected interface for users
from mbed_targets import MbedTargets, MbedTarget


class TestMbedTarget(unittest.TestCase):
    """Tests for the class `MbedTarget`."""

    def test_nominal_database_entry(self):
        """Given database entry data, an MbedTarget is generated with the correct information."""
        fake_target_database_entry = {
            "attributes": {
                "features": {
                    "mbed_os_support": [
                        "Mbed OS 5.15"
                    ],
                    "mbed_enabled": [
                        "Basic"
                    ]
                },
                "board_type": "B_1",
                "name": "Board 1",
                "product_code": "P1",
            }
        }
        mbed_target = MbedTarget(fake_target_database_entry)
        self.assertEqual("B_1", mbed_target.board_type)
        self.assertEqual("Board 1", mbed_target.platform_name)
        self.assertEqual(["Mbed OS 5.15"], mbed_target.mbed_os_support)
        self.assertEqual(["Basic"], mbed_target.mbed_enabled)
        self.assertEqual("P1", mbed_target.product_code)

    def test_empty_database_entry(self):
        """Given no data, and MbedTarget is created with no information."""
        mbed_target = MbedTarget({})
        self.assertEqual("", mbed_target.board_type)
        self.assertEqual("", mbed_target.platform_name)
        self.assertEqual([], mbed_target.mbed_os_support)
        self.assertEqual([], mbed_target.mbed_enabled)
        self.assertEqual("", mbed_target.product_code)


@mock.patch('mbed_targets._internal.target_database.get_target_data')
class TestMbedTargets(unittest.TestCase):
    """Tests for the class `MbedTargets`."""

    def test_iterator(self, mocked_get_target_data):
        """An MbedTargets object is iterable and on each iteration returns the next target data in the list."""
        # Mock the return value of the target data with something that can be validated in a iterator
        fake_target_data = [{"count": 0}, {"count": 1}, {"count": 2}]
        mocked_get_target_data.return_value = fake_target_data

        # Create an instance of the class which is to be used as the iterator
        mbed_targets = MbedTargets()

        mbed_target_list = [mbed_target._target_entry for mbed_target in mbed_targets]
        self.assertEqual(fake_target_data, mbed_target_list, "The list comprehension should match the fake data")

        # Check the iteration is repeatable
        mbed_target_list = [mbed_target._target_entry for mbed_target in mbed_targets]
        self.assertEqual(fake_target_data, mbed_target_list, "The list comprehension should match the fake data")

        # Iterate through the list checking the value returned matched the enumerated count
        for count, target in enumerate(mbed_targets):
            self.assertEqual(count, target._target_entry["count"], "Iterator count values should match")
