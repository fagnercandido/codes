import os
import re
import sys
import errno
import requests
from subprocess import call
from gitlab import Gitlab
import requests

session = requests.Session()


URL = 'http://gitlab.com'
SIGN_IN_URL = 'http://gitlab.com/users/sign_in'
LOGIN_URL = 'http://gitlab.com/users/sign_in'

sign_in_page = session.get(SIGN_IN_URL).content
print (sign_in_page)
for l in sign_in_page.split('\n'):
    m = re.search('name="authenticity_token" value="([^"]+)"', l)
    if m:
        break

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

token = None
if m:
    token = m.group(1)

if not token:
    print('Unable to find the authenticity token')
    sys.exit(1)
data = {'user[login]': 'user',
        'user[password]': 'pass',
        'authenticity_token': token}
r = session.post(LOGIN_URL, data=data)
if r.status_code != 200:
    print('Failed to log in')
    sys.exit(1)

gitBasePathRelative = "/home/git"

# Register a connection to a gitlab instance, using its URL and a user private token
gl = Gitlab(URL, email='user', password='pass', api_version=3)

gl.auth() # Connect to get the current user


groupsToSkip = ['grupos']



for p in gl.projects.list(all=True):
    if not any(p.namespace.path in s for s in groupsToSkip):
        pathToFolder = gitBasePathRelative + p.namespace.name + "/" + p.name
        commandArray = ["mr", "config", pathToFolder, "checkout=git clone '" + p.ssh_url_to_repo + "' '" + p.name + "'"]
        comando = "git clone "+p.ssh_url_to_repo
        print comando
        call(["git", "clone", p.ssh_url_to_repo])
