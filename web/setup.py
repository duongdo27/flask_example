from setuptools import setup
from setuptools import find_packages

setup(name='thea-web',
      version='0.1',
      description='Thea',
      url='http://github.com/duongdo27/thea',
      author='Duong Do',
      author_email='duongdo@example.com',
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      install_requires=[
          'Flask',
          'Flask-Mail',
          'gunicorn',
          'pymysql',
      ],
      zip_safe=False)
