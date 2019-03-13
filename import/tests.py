#Copyright 2019 Adobe. All rights reserved.
#This file is licensed to you under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License. You may obtain a copy
#of the License at http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software distributed under
#the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR REPRESENTATIONS
#OF ANY KIND, either express or implied. See the License for the specific language
#governing permissions and limitations under the License.

import unittest
import csv_read
import os

class PlacesImportTests(unittest.TestCase):
    """Tests for Places import"""


    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os.remove(self.filename)
        except:
            pass


    def test_csv_read_validate_file_non_exist(self):
        """Check that non existant file fails correctly"""
        self.assertEqual(csv_read.validate_file('notValidLocation/file.csv'), (False, 'File not found, please correct file path.'))


    def test_csv_read_validate_file_not_csv(self):
        """Check that non csv file fails correctly"""
        self.filename = 'places_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('lib_id, name, description, type\n'
                    'dd6b54fa-5f93-4922-bb70-606fb4416c69, sample_name, sample_decription, Point')
        self.assertEqual(csv_read.validate_file(self.filename), (False, 'Not a .csv file, please specify a csv file in file path.'))


    def test_csv_read_validate_file_valid_csv(self):
        """Check that valid csv file is read correctly without errors"""
        self.filename = 'places_test_file.csv'
        with open(self.filename, 'w') as f:
            f.write('lib_id, name, description, type\n'
                    'dd6b54fa-5f93-4922-bb70-606fb4416c69, sample_name, sample_decription, Point')
        self.assertEqual(csv_read.validate_file(self.filename), (True, ''))


    def test_csv_read_ingest_csv(self):
        """Check that csv file returns correct list"""
        self.filename = 'places_test_file.csv'
        with open(self.filename, 'w') as f:
            f.write('lib_id,name,description,type\n'
                    'dd6b54fa-5f93-4922-bb70-606fb4416c69,sample_name,sample_description,Point')
        self.assertEqual(csv_read.ingest_csv(self.filename), [{'lib_id': 'dd6b54fa-5f93-4922-bb70-606fb4416c69', 'name': 'sample_name', 'description': 'sample_description', 'type': 'Point'}])


    def test_csv_read_verify_required_keys_present(self):
        """Check that correct keys are present"""
        random_key_list = ['key1', 'key2', 'key4', 'key10', 'key9', 'key3', 'key8', 'key5']
        required_key_list = ['key1', 'key2', 'key3', 'key4']
        self.assertEqual(csv_read.verify_required_keys(random_key_list, required_key_list), (True, ''))


    def test_csv_read_verify_required_keys_not_present(self):
        """Check that not all keys present"""
        random_key_list = ['key1', 'key2', 'key4', 'key10', 'key9', 'key3', 'key8', 'key5']
        required_key_list = ['key1', 'key7', 'key6', 'key4']
        self.assertEqual(csv_read.verify_required_keys(random_key_list, required_key_list), (False, '\tThe following required headers are missing from the csv file: key7, key6'))


    def test_csv_read_validate_entry_valid_number(self):
        """Confirm max boundary with number"""
        value = 50
        min = 10
        max = 50
        self.assertEqual(csv_read.validate_entry(value, min, max), True)


    def test_csv_read_validate_entry_valid_string(self):
        """Confirm min boundary with string"""
        value = '10'
        min = 10
        max = 50
        self.assertEqual(csv_read.validate_entry(value, min, max), True)


    def test_csv_read_validate_entry_not_valid_number(self):
        """Confirm below minimum with number"""
        value = 9
        min = 10
        max = 50
        self.assertEqual(csv_read.validate_entry(value, min, max), False)


    def test_csv_read_validate_entry_not_valid_string(self):
        """Confirm above max boundary with string"""
        value = '51'
        min = 10
        max = 50
        self.assertEqual(csv_read.validate_entry(value, min, max), False)

    def test_csv_read_validate_entry_empty_string(self):
        """Confirm empty strting is invalid"""
        value = ''
        min = 0
        max = 50
        self.assertEqual(csv_read.validate_entry(value, min, max), False)

    def test_csv_read_verify_data_invalid_data(self):
        """Make sure finding bad data"""
        places_dictionary = [{'category': 'Category_data1', 'city': 'City_data1', 'name': 'Name_data1', 'color': 'blue', 'lib_id': 'not_valid', 'metadataA': 'metadataA_1', 'longitude': '500', 'state': 'State_data1', 'street': 'Street_data1', 'radius': '3000', 'country': 'Country_data1', 'latitude': '100', 'icon': 'anchor', 'type': 'Circle', 'description': 'Description_data1'}, {'category': 'Category_data2', 'city': 'City_data2', 'name': 'Name_data2', 'color': '#AA99E8', 'lib_id': 'dd6b54fa-5f93-4922-bb70-606fb4416c69', 'metadataA': 'metadataA_2', 'longitude': '-400', 'state': 'State_data2', 'street': 'Street_data2', 'radius': '0', 'country': 'Country_data2', 'latitude': '-90', 'icon': '', 'type': 'Point', 'description': 'Description_data2'}, {'category': 'Category_data3', 'city': 'City_data3', 'name': 'Name_data3', 'color': '', 'lib_id': 'dd6b54fa-5f93-4922-bb70-606fb4416c69', 'metadataA': 'metadataA_3', 'longitude': '-121.898389', 'state': 'State_data3', 'street': 'Street_data3', 'radius': '25', 'country': 'Country_data3', 'latitude': '37.334305', 'icon': 'anchor', 'type': 'Point', 'description': 'Description_data3'}, {'category': 'Category_data4', 'city': 'City_data4', 'name': 'Name_data4', 'color': '#AA99E8', 'lib_id': 'dd6b54fa-5f93-4922-bb70-606fb4416c69', 'metadataA': 'metadataA_4', 'longitude': '-121.898389', 'state': 'State_data4', 'street': 'Street_data4', 'radius': '25', 'country': 'Country_data4', 'latitude': '37.334305', 'icon': 'anchor', 'type': 'Point', 'description': 'Description_data4'}, {'category': 'Category_data5', 'city': 'City_data5', 'name': 'Name_data5', 'color': '#AA99E8', 'lib_id': 'dd6b54fa-5f93-4922-bb70-606fb4416c69', 'metadataA': 'metadataA_5', 'longitude': '-121.898389', 'state': 'State_data5', 'street': 'Street_data5', 'radius': '25', 'country': 'Country_data5', 'latitude': '37.334305', 'icon': 'anchor', 'type': 'Point', 'description': 'Description_data5'}]
        self.assertEqual(csv_read.verify_data(places_dictionary), 'Row 2 has an invalid lib_id.\nRow 2 has incorrect value for the type, only "Point" is valid.\nRow 2 has an invalid longitude, it must be between -180 and 180.\nRow 2 has an invalid latitude, it must be between -85 and 85.\nRow 2 has an invalid radius, it must be between 10 and 2000.\nRow 2 has an invalid color, see documentation for valid colors.\nRow 3 has an invalid longitude, it must be between -180 and 180.\nRow 3 has an invalid latitude, it must be between -85 and 85.\nRow 3 has an invalid radius, it must be between 10 and 2000.\n')


    def test_csv_read_verify_data_invalid_data(self):
        """Make sure valid data passes"""
        places_dictionary = [{'category': 'Category_data1', 'city': 'City_data1', 'name': 'Name_data1', 'color': '#AA99E8', 'lib_id': 'dd6b54fa-5f93-4922-bb70-606fb4416c69', 'metadataA': 'metadataA_1', 'longitude': '-121.898389', 'state': 'State_data1', 'street': 'Street_data1', 'radius': '25', 'country': 'Country_data1', 'latitude': '37.334305', 'icon': 'anchor', 'type': 'Point', 'description': 'Description_data1'}, {'category': 'Category_data2', 'city': 'City_data2', 'name': 'Name_data2', 'color': '#AA99E8', 'lib_id': 'dd6b54fa-5f93-4922-bb70-606fb4416c69', 'metadataA': 'metadataA_2', 'longitude': '-121.898389', 'state': 'State_data2', 'street': 'Street_data2', 'radius': '25', 'country': 'Country_data2', 'latitude': '37.334305', 'icon': '', 'type': 'Point', 'description': 'Description_data2'}, {'category': 'Category_data3', 'city': 'City_data3', 'name': 'Name_data3', 'color': '', 'lib_id': 'dd6b54fa-5f93-4922-bb70-606fb4416c69', 'metadataA': 'metadataA_3', 'longitude': '-121.898389', 'state': 'State_data3', 'street': 'Street_data3', 'radius': '25', 'country': 'Country_data3', 'latitude': '37.334305', 'icon': 'anchor', 'type': 'Point', 'description': 'Description_data3'}, {'category': 'Category_data4', 'city': 'City_data4', 'name': 'Name_data4', 'color': '#AA99E8', 'lib_id': 'dd6b54fa-5f93-4922-bb70-606fb4416c69', 'metadataA': 'metadataA_4', 'longitude': '-121.898389', 'state': 'State_data4', 'street': 'Street_data4', 'radius': '25', 'country': 'Country_data4', 'latitude': '37.334305', 'icon': 'anchor', 'type': 'Point', 'description': 'Description_data4'}, {'category': 'Category_data5', 'city': 'City_data5', 'name': 'Name_data5', 'color': '#AA99E8', 'lib_id': 'dd6b54fa-5f93-4922-bb70-606fb4416c69', 'metadataA': 'metadataA_5', 'longitude': '-121.898389', 'state': 'State_data5', 'street': 'Street_data5', 'radius': '25', 'country': 'Country_data5', 'latitude': '37.334305', 'icon': 'anchor', 'type': 'Point', 'description': 'Description_data5'}]
        self.assertEqual(csv_read.verify_data(places_dictionary), '')


if __name__ == '__main__':
    unittest.main()

