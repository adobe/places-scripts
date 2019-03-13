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
import create_body
import urllib2

csv_file = config.csv_file_path
batch_size = config.batch_size
required_keys = config.required_keys
places_domain = config.places_domain
headers = config.headers

def check_availability(domain):
    places_api = 'ping'
    url = domain + places_api
    service_availability = False
    print 'Checking availability of service: ' + url
    try:
        result = urllib2.urlopen(url)
        contents = result.read()
        # print content
        if contents == 'pong':
            service_availability = True
        print 'Service available with code: '+ str(result.code)
    except urllib2.HTTPError, e:
        print 'Error code is: ' + str(e.code)
        # print 'Message is : ' + str(e.read())
        service_availability = False
    except urllib2.URLError, e:
        print e.reason
    return service_availability

def add_pois_to_library(body_list, domain, headers):
    print 'Adding to library'
    places_api = '/places/placesapi/v1/pois/batchCreate'
    places_url = domain + places_api
    for body in body_list:
        data = body
        request = urllib2.Request(places_url, data, headers)
        # print 'Request = ' + str(request)
        try:
            # content = urllib2.urlopen(request).read()
            result = urllib2.urlopen(request)
            # print 'Result = ' + str(result)
            contents = result.read()
            # print 'Contents = ' +str(contents)
            print 'Status Code is ' + str(result.getcode())
        except urllib2.HTTPError, e:
            print 'Error code is: ' + str(e.code)
            print 'Message is : ' + str(e.read())
        except urllib2.URLError, e:
            print e.reason


def add_pois_to_places(file_path, batch_size, required_keys, domain, headers):
    request_bodies = create_body.create_request_bodies_list(file_path, batch_size, required_keys)
    if not isinstance(request_bodies, list):
        # print request_bodies
        return

    service_available = check_availability(places_domain)
    if not service_available:
        print 'Server not available, try again later.'
        return

    add_pois_to_library(request_bodies, domain, headers)


if __name__ == '__main__':
    add_pois_to_places(csv_file, batch_size, required_keys, places_domain, headers)