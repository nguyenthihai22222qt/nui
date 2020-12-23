from setuptools import setup, find_packages

setup(
	name='nui',
	version='g2.12-c3.1',  # <name (g/c)><newest 'folder' ver>-<same format, next part>
	url='https://github.com/TheNovi/Nui',
	license='MIT',
	author='TheNovi',
	author_email='jakub.novi.novacek@gmail.com',
	description='',
	packages=find_packages(),
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Topic :: Software Development :: Ui Tools',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3.9',
	],
)

# pip install .
