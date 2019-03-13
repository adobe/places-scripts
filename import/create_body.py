#Copyright 2019 Adobe. All rights reserved.
#This file is licensed to you under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License. You may obtain a copy
#of the License at http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software distributed under
#the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR REPRESENTATIONS
#OF ANY KIND, either express or implied. See the License for the specific language
#governing permissions and limitations under the License.

import csv_read
import config
import json

batch_size = config.batch_size
required_keys = config.required_keys
csv_path = config.csv_file_path
request_bodies = []

def create_request_body(key_value_list, required_keys):
    request_body = '''{
    "createPOIRequests": ['''
    for row in key_value_list:
        request_body += '''
        {{
            "lib_id": {lib_id},
            "name": {name},
            "description": {description},
            "location": {{
                "type": {type},
                "coordinates": [{longitude}, {latitude}]
            }},
            "radius": {radius},
            "country": {country},
            "state": {state},
            "city": {city},
            "street": {street},
            "category": {category},
            "icon": {icon},
            "color": {color}
        }},'''.format(lib_id=json.dumps(row['lib_id']), name=json.dumps(row['name']), description=json.dumps(row['description']), type=json.dumps(row['type']),
                              longitude=row['longitude'], latitude=row['latitude'], radius=row['radius'],
                              country=json.dumps(row['country']), state=json.dumps(row['state']), city=json.dumps(row['city']), street=json.dumps(row['street']),
                              category=json.dumps(row['category']), icon=json.dumps(row['icon']), color=json.dumps(row['color']))
        if len(row) > 14:
            request_body = request_body[:-11]
            request_body += ''',
            "metadata": {'''
            for key, value in row.iteritems():
                if (key not in required_keys):
                    request_body += '''
                {key}: {value},'''.format(key=json.dumps(key), value=json.dumps(value))
            request_body = request_body[:-1]
            request_body += '''
            }'''
            request_body += '''
        },'''
    request_body = request_body[:-1]
    request_body += '''
    ]
}'''
    return request_body


def batch_requests(all_data, max_batch_size):
    arrs = []
    while len(all_data) > max_batch_size:
        chunk = all_data[:max_batch_size]
        arrs.append(chunk)
        all_data = all_data[max_batch_size:]
    arrs.append(all_data)
    return arrs


def create_request_bodies_list(file_path, batch_size, required_keys):
    csv_list = csv_read.get_csv_data(file_path)
    if not isinstance(csv_list, list):
        print 'The following errors were found in the CSV file, please correct and try again:'
        print csv_list
        return
    print 'Good File'
    # create batchs
    data_batches = batch_requests(csv_list, batch_size)
    for batch in data_batches:
        # print batch
        request_bodies.append(create_request_body(batch,required_keys))
    return request_bodies

# requests_bodies = create_request_bodies_list(csv_path, batch_size, required_keys)
#
# for body in request_bodies:
#     print body