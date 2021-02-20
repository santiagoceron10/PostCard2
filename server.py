Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@santiagoceron10 
mrfrancej
/
Postcard
1
00
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Postcard/server.py /
@alesanchezr
alesanchezr added support for html strings
Latest commit 77f807d on May 17, 2020
 History
 1 contributor
37 lines (32 sloc)  1.58 KB
  
try:
    # try to import flask, or return error if has not been installed
    from flask import Flask
    from flask import send_from_directory
except ImportError:
    print("You don't have Flask installed, run `$ pip3 install flask` and try again")
    exit(1)

import os, subprocess

static_file_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), './')
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 #disable cache

# Serving the index file
@app.route('/', methods=['GET'])
def serve_dir_directory_index():
    if os.path.exists("app.py"):
        # if app.py exists we use the render function
        out = subprocess.Popen(['python3','app.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        stdout,stderr = out.communicate()
        return stdout if out.returncode == 0 else f"<pre style='color: red;'>{stdout.decode('utf-8')}</pre>"
    if os.path.exists("index.html"):
        return send_from_directory(static_file_dir, 'index.html')
    else:
        return "<h1 align='center'>404</h1><h2 align='center'>Missing index.html file</h2><p align='center'><img src='https://ucarecdn.com/3a0e7d8b-25f3-4e2f-add2-016064b04075/rigobaby.jpg' /></p>"

# Serving any other image
@app.route('/<path:path>', methods=['GET'])
def serve_any_other_file(path):
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = os.path.join(path, 'index.html')
    response = send_from_directory(static_file_dir, path)
    response.cache_control.max_age = 0 # avoid cache memory
    return response

app.run(host='0.0.0.0',port=3000, debug=True, extra_files=['./',])
© 2021 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
