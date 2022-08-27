import sys, protbuilder as prot
from setuptools import setup, find_packages
exec(open('src/prot/__version__.py').read())
ver = prot.VersionString(__version__)
if '!upgrade' in sys.argv:
	sys.argv.remove('!upgrade')
	ver = ver.upgrade()
	f = open('src/prot/__version__.py', 'w')
	f.write('__version__ = '+repr(ver))
	f.flush()
	f.close()

setup(
	name="prot", version=ver, description='A Simple Tool That Contains Advance Functions.',
	long_description=open('README.md').read(), long_description_content_type='text/markdown',
	author="Alireza Poodineh", author_email='pa789892@gmail.com', url='https://www.pypi.org/user/Ali_p1986',
	packages=find_packages(where="src"), package_dir={"": "src"}, zip_safe=False,
	entry_points={"console_scripts": ["prot=prot:prot", "prot.pip=prot.pip:pip"]})