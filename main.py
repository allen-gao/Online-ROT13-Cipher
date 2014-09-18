#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#
import webapp2
import cgi

form="""
<h3>Welcome to Allen's ROT13 Cipher!</h3>
<form method="post">
Enter some text to ROT13: 
<br>
<textarea style="height: 100px; width: 400px;" name="text" placeholder="Enter your message here">%(old_text)s</textarea>
<br>
<input type="submit" value="Click here to submit!">
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form % {"old_text": ""})
    def post(self):
    	old = self.request.get("text")
    	old = rot(old)
    	old = escape_html(old)
    	self.response.write(form % {"old_text": old})


def rot(s):
	new = ""
	i = 0
	length = len(s)
	while i < length:
		if (ord(s[i]) >= 65 and ord(s[i]) <= 77) or (ord(s[i]) >= 97 and ord(s[i]) <= 109):
			new += chr(ord(s[i]) + 13)
			i += 1
			continue
		if (ord(s[i]) >= 78 and ord(s[i]) <= 90) or (ord(s[i]) >= 110 and ord(s[i]) <= 122):
			new += chr(ord(s[i]) - 13)
			i += 1
			continue
		else:
			new += s[i]
			i += 1
	return new

def escape_html(s):
	return cgi.escape(s, quote = True)


app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)
