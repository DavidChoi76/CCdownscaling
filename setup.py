from setuptools import setup, find_packages


setup(name='CCdownscaling',
      description='A package providing several statistical climate downscaling tools and evaluation metrics',
      url='https://github.com/drewpolasky/CCdownscaling',
      author='Drew Polasky',
      author_email='drewpolasy@gmail.com',
      license='MIT',
      packages=find_packages(),
      include_package_data=True)