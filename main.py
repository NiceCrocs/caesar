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
import cgi
import webapp2
from caesar import encrypt, alphabet_position, rotate_character

form_data = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            p.error {
                color: red;
            }
        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label for="rot">Rotate by: </label>
                <input type="text" name="rot" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">%(value)s</textarea>
            <br>
            <input type="submit">
        </form>
    </body>
</html>"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form_data % {"value": ""})

    def post(self):
        rot = self.request.get("rot")
        rot = int(rot)
        text = self.request.get("text")
        text = cgi.escape(text, quote = True)
        user_encrypt = encrypt(text, rot)
        self.response.write(form_data % {"value": user_encrypt})

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
