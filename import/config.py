#Copyright 2019 Adobe. All rights reserved.
#This file is licensed to you under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License. You may obtain a copy
#of the License at http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software distributed under
#the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR REPRESENTATIONS
#OF ANY KIND, either express or implied. See the License for the specific language
#governing permissions and limitations under the License.

csv_file_path = '{enter_file_path_of_csv}'


# access code, update every 24 hours
#  sample: access_code = 'olorhtndOiJpbXNfbmExLXN0ZzEta2V5LTEuY2VyIiwiYWxnIjoiUlMyNTYifQ.eyJpZCI6IjE1NDg4ODM4NzY0NzRfODBiYTFmMWYtZWRjYS00NTkzLWI3MjQtZWJiYWRhM2M0OTFlX3VlMSIsImNsaWVudF9pZCI6IlZBX0FQSV9UZXN0aW5nIiwidXNlcl9pZCI6IjkwQkM3NjU4NUJBRDZGQzkwQTQ5NDIzM0BBZG9iZUlEIiwidHlwZSI6ImFjY2Vzc190b2tlbiIsImFzIjoiaW1zLW5hMS1zdGcxIiwiZmciOiJURVMyWFNVRldYV0s1NTczNVgzTktUQUFRVT09PT09PSIsInJ0aWQiOiIxNTQ4ODgzODc2NDc1XzQ3NmM2ODAxLTZiMjEtNDhmZS05NjZlLTdkZmZlNjY1OGNjOV91ZTEiLCJydGVhIjoiMTU1MDA5MzQ3NjQ3NSIsIm1vaSI6ImUzMDcyM2Y1IiwiYyI6ImVRWGxBTC9sU2dMM0xLZFZhamV5M0E9PSIsImV4cGlyZXNfaW4iOiI4NjQwMDAwMCIsInNjb3BlIjoiQWRvYmVJRCxvcGVuaWQscmVhZF9vcmdhbml6YXRpb25zLGFkZGl0aW9uYWxfaW5mby5wcm9qZWN0ZWRQcm9kdWN0Q29udGV4dCxhZGRpdGlvbmFsX2luZm8ucm9sZXMsYWRkaXRpb25hbF9pbmZvLnVzZXJfaW1hZ2VfdXJsIiwiY3JlYXRlZF9hdCI6IjE1NDg4ODM4NzY0NzQifQ.fR0nTXYLLa4ZbzBMQIanH_qyLW1pIH2qBZAEgmhv6zENv88_qqeENnJP4Q4KgjxUGU8J6uxd65PIvinS4wrlXgKi8ZAysd0yErv-jjOBk-bVHA-I0Jwy1vdwcI8Cc9R9jlq5V-kssm7mxEnNFXfwGIUGpHX7cVOW-3ciyuXLpOHpWO5utfgh0w0CbvP2zWa4Q-v5-OMR7jKJYdMv7ch1ZZpMI5ZRat89okOJe_RTn4PpSMwo4gcPrTQuigkDBXr3KkUIkguRCpQtdZcHuxgJaIvdf8YSojYvjo2hEKkXDAaVODZWKbzxRGnc9JzT-MqsIYpcG8_bz1q4Q4eifSStZg'
access_code = '{enter_access_token}'

# Experience Cloud orgID that POIs will be added to
#  sample: org_id = '77FB611457777FFB0A494107@AdobeOrg'
org_id = '{enter_org_ID}'

# API key to use
api_key = '{enter_api_key}'



#  Do not change edit the items below
# Headers required in csv file
required_keys = ['lib_id', 'name', 'description', 'type', 'longitude', 'latitude', 'radius', 'country', 'state',
                     'city', 'street', 'category', 'icon', 'color']

valid_colors = ['', '#AA99E8', '#FC685B', '#3DC8DE', '#F6C436', '#3E76D0', '#DC2ABA', '#BECE5D', '#61B56B', '#FC962E']
valid_icons = ['', 'anchor', 'beaker', 'bell', 'browse', 'book', 'brush', 'building', 'calculator', 'camera', 'shoppingCart', 'clock', 'box', 'flashlight', 'follow', 'bid', 'ribbon', 'education', 'hammer', 'heart', 'home', 'key', 'mailbox', 'male', 'promote', 'money', 'trap', 'game', 'gift', 'launch', 'star', 'lightbulb', 'pin', 'target', 'teapot', 'thumbDown', 'thumbUp', 'briefcase', 'trophy', 'female', 'wrench']

# Max number of POIs sent in each request
batch_size = 1000

#  URL for Places REST APIs
places_domain = 'https://api-places.adobe.io/'

#  Headers used in request
headers = {'Content-Type': 'application/json', 'Authorization': access_code,
           'x-api-key': api_key, 'x-gw-ims-org-id': org_id}

# Minimum and maximum latitude accepted
minimum_latitude = -85
maximum_latitude = 85

# Mimimum and maximum longitude accepted
minimum_longitude = -180
maximum_longitude = 180

# Minimum and maximum radius accepted
minimum_radius = 10
maximum_radius = 2000