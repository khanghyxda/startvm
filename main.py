# Copyright 2016 Google Inc.
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

# [START app]
import logging

import json

import httplib2
 
from oauth2client.contrib import gce
from oauth2client.contrib.appengine import AppAssertionCredentials
from google.appengine.api import memcache
from googleapiclient.discovery import build
 
from flask import Flask

app = Flask(__name__)
if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8888)


@app.route('/')
def hello():
    return 'Hello World1111!'
	
@app.route('/vm/start')
def start_vm():
	credentials = AppAssertionCredentials(scope='https://www.googleapis.com/auth/compute')
	logging.debug(memcache)
	http = credentials.authorize(httplib2.Http(memcache))
	logging.debug(http)
	compute = build('compute', 'v1')

	# Start the VM!
	# result = compute.instances().start(instance='jocsub-1', zone='asia-northeast1-b', project='jocc-121ee').execute()
	result = compute.instances().start(instance='joc-singapore', zone='asia-southeast1-b', project='jocc-121ee').execute()
	logging.debug(result)
	return json.dumps(result, indent=4)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
