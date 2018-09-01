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

import httplib2
 
from oauth2client.contrib import gce
 
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'
	
@app.route('/vm/start')
def start_vm():
	credentials = AppAssertionCredentials(scope='https://www.googleapis.com/auth/compute')
	http = credentials.authorize(httplib2.Http(memcache))
	compute = discovery.build('compute', 'v1', http=http)

	# Start the VM!
	result = compute.instances().start(instance=jocsub-1, zone=asia-northeast1-b, project=Jocc).execute()
	logging.debug(result)
	return json.dumps(result, indent=4)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
