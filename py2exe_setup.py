from distutils.core import setup  
import py2exe  

setup(
	console=['LEPortableHelper.py'],
	zipfile = None,
	options = {'py2exe': {'bundle_files': 1}}
	)
