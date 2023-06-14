import xmlrpc.client as xmlrpclib

pypi = xmlrpclib.ServerProxy('https://pypi.org/pypi', allow_none=True)

def allPackages():
	"""return a list of all server packages"""
	return pypi.list_packages()

def userPackages(user):
	"""return a list of user packages"""
	return pypi.user_packages(user)

def releaseUrls(name, version):
	"""return a list of release urls"""
	return pypi.release_urls(name, version)

def packageRoles(name):
	"""return a list of package roles"""
	return pypi.package_roles(name)

def packageReleases(name, show_hidden=True):
	"""return a list of package releases"""
	return pypi.package_releases(name, show_hidden)

def releaseData(name, version):
	"""return dictionary with release data"""
	return pypi.release_data(name, version)
