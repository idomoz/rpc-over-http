import re
apiFile = 'path/to/api.py'

with open(apiFile) as f:
    api = re.compile('def (.*?)\((.*?),? ?request').findall(f.read())

functions = 'server = {\n    %s\n};' % ',\n    '.join('%s: (%s) => {}' % func for func in api)
with open('path/to/server.js') as f:
    data = f.read()
old_funcs = re.compile('server = {.*?};', re.DOTALL).findall(data)[0]
data = data.replace(old_funcs, functions)
with open(apiFile, 'w') as f:
    f.write(data)
