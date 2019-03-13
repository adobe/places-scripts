#Copyright 2019 Adobe. All rights reserved.
#This file is licensed to you under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License. You may obtain a copy
#of the License at http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software distributed under
#the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR REPRESENTATIONS
#OF ANY KIND, either express or implied. See the License for the specific language
#governing permissions and limitations under the License.

import os.path
import csv
import config
from pprint import pprint as pp


csv_file_path = config.csv_file_path
required_keys = config.required_keys
valid_colors = config.valid_colors
valid_icons = config.valid_icons

minimum_latitude = config.minimum_latitude
maximum_latitude = config.maximum_latitude

minimum_longitude = config.minimum_longitude
maximum_longitude = config.maximum_longitude

minimum_radius = config.minimum_radius
maximum_radius = config.maximum_radius

def validate_file(file_path):
    errors = ''
    valid_file = True
    if not file_path[-4:] == '.csv':
        errors = 'Not a .csv file, please specify a csv file in file path.'
        valid_file = False
    if not os.path.isfile(file_path):
        errors = 'File not found, please correct file path.'
        valid_file = False
    return valid_file, errors


def ingest_csv(file_location):
    csv_dict = csv.DictReader(open(file_location))
    csv_as_list = list(csv_dict)
    # pp(csv_list)
    return csv_as_list


def verify_required_keys(key_list, required_key_list):
    keys_present = all(elem in key_list for elem in required_key_list)
    errors=''
    if not keys_present:
        errors = '\tThe following required headers are missing from the csv file: '
        for key in required_key_list:
            if (key not in key_list):
                errors += str(key) + ', '
        errors = errors[:-2]
    return keys_present, errors


def validate_entry(value, min, max):
    valid = False
    try:
        number = float(value)
        if number >= min and number <= max:
            valid = True
    except ValueError as e:
        e
    return valid


def verify_data(csv_dictionary_list):
    row_number = 2
    errors = ''
    for row in csv_dictionary_list:
        # print row
        if not len(row['lib_id']) == 36:
            errors += 'Row ' + str(row_number) + ' has an invalid lib_id.\n'
        if row['type'] != 'Point':
            errors += 'Row ' + str(row_number) + ' has incorrect value for the type, only "Point" is valid.\n'
        if not validate_entry(row['longitude'], minimum_longitude, maximum_longitude):
            errors += 'Row ' + str(row_number) + ' has an invalid longitude, it must be between ' \
                      + str(minimum_longitude) + ' and ' + str(maximum_longitude) + '.\n'
        if not validate_entry(row['latitude'], minimum_latitude, maximum_latitude):
            errors += 'Row ' + str(row_number) + ' has an invalid latitude, it must be between ' \
                      + str(minimum_latitude) + ' and ' + str(maximum_latitude) + '.\n'
        if not validate_entry(row['radius'], minimum_radius, maximum_radius):
            errors += 'Row ' + str(row_number) + ' has an invalid radius, it must be between ' \
                      + str(minimum_radius) + ' and ' + str(maximum_radius) + '.\n'
        if row['color'] not in valid_colors:
            errors += 'Row ' + str(row_number) + ' has an invalid color, see documentation for valid colors.\n'
        if row['icon'] not in valid_icons:
            errors += 'Row ' + str(row_number) + ' has an invalid icon, see documentation for valid icons.\n'

        row_number += 1
    return errors


def get_csv_data(file_path):
    errors = ''

    # check file
    valid_file, errors = validate_file(file_path)

    if not valid_file:
        return errors

    print 'File being read'
    # ingest file
    csv_list = ingest_csv(file_path)

    # check for required headers
    required_keys_present, errors = verify_required_keys(csv_list[0].keys(), required_keys)

    if not required_keys_present:
        return errors
    print 'File has required keys'
    # verify data
    errors = verify_data(csv_list)
    if not errors == '':
        return errors
    print 'No errors found in file' + errors
    return csv_list


if __name__ == '__main__':
    the_result = get_csv_data(csv_file_path)
    print(the_result)