from fabric.api import *

def update():
	local('git add .')
	comment=raw_input('key in comment:')
	local('git commit -m "%s"' % comment)
	local('git push origin master')
