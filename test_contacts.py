
import unittest
import tempfile
import os
import json
from unittest.mock import patch

import contacts_manager


class TestContactManager(unittest.TestCase):

    def test_add_contact(self):
        contacts = {}

        with patch("builtins.input", side_effect=[
            "Kajal", "9876543210", "kajal@example.com"
        ]):
            with tempfile.TemporaryDirectory() as temp_dir:
                test_file = os.path.join(
                    temp_dir, "contacts_data.json"
                )

                with patch.object(
                    contacts_manager, "DATA_FILE", test_file
                ):
                    contacts_manager.add_contact(contacts)

                    self.assertIn("kajal", contacts)
                    self.assertEqual(
                        contacts["kajal"]["phone"], "9876543210"
                    )
                    self.assertTrue(os.path.exists(test_file))

    def test_load_contacts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            test_file = os.path.join(
                temp_dir, "contacts_data.json"
            )

            with open(test_file, "w") as file:
                json.dump({
                    "kajal": {
                        "name": "Kajal",
                        "phone": "9876543210",
                        "email": "kajal@example.com"
                    }
                }, file)

            with patch.object(
                contacts_manager, "DATA_FILE", test_file
            ):
                contacts = contacts_manager.load_contacts()

            self.assertIn("kajal", contacts)

    def test_invalid_phone(self):
        contacts = {}

        with patch("builtins.input", side_effect=[
            "Kajal", "123", "kajal@example.com"
        ]):
            contacts_manager.add_contact(contacts)

        self.assertNotIn("kajal", contacts)


if __name__ == "__main__":
    unittest.main()
  
