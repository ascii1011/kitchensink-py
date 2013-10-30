import os, sys

search_for_this = sys.argv[1]

location = '/opt'
if len(sys.argv) > 2:
    if sys.argv[2][0] != '/':
        location = '/%s' % sys.argv[2]
    else:
        location = sys.argv[2]

print 'searching at %s.' % location

if search_for_this:
    _command = 'grep -r "%s" %s | ' \
        'grep -v /.svn | ' \
        'grep -v .pyc | ' \
        'grep -v .py~ | ' \
        'grep -v .pl | ' \
        'grep -v .pm | ' \
        'grep -v /perl | ' \
        'grep -v /test | ' \
        'grep -v /# ' % ( search_for_this, location )
    
    if _command:
        os.system( _command )
