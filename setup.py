import sys, prot
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
  classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12"
    ],
  long_description=open('README.md').read(), long_description_content_type='text/markdown',
  author="Alireza Poodineh", author_email='itsaeliux@gmail.com', url='https://github.com/SAPTeamDEV/prot',
  packages=find_packages(where="src"), license_files=('LICENSE',), package_dir={"": "src"}, license="MIT",
  entry_points={"console_scripts": ["prot=prot:prot", "prot.pip=prot.pip:pip"]}
)