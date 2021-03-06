# Pypi practice

[![Build Status](https://travis-ci.org/hyunyoung2/Hyunyoung2_Pypi_Python_package_index_for_practice.svg?branch=master)](https://travis-ci.org/hyunyoung2/Hyunyoung2_Pypi_Python_package_index_for_practice)

 When you normally distribute Python package, you have to use PyPi(Python Package Index).

 I mean when you install python package, you used to use pip install package name. 

 From now on, I will explain how to upload to pypi.org to manage python package. 

 Normally, before uploading PyPi, You have to sign up [PyPi](https://pypi.org). 

 In my case, I used setuptools. 

```python
from setuptools import setup, find_package

setup(
    name="your package name",
    version="your package version number",
    ... 
)
```

 So you have to pass arguements to setup to Python package index. 

 If the arguements is set up,  Let's see Requirements for packageing and distributing

 1. First, Make sure you have already fulfilled the [requirements for installing packages](https://packaging.python.org/tutorials/installing-packages/#installing-requirements).

 2. Install "twine":

> pip install twine  

 You will need this to upload your project distribution to PyPI.

 Then you have to select whether you want to distribute Source or just built package as wheel. 

 - Source Distributions

> python setup.py sdist  

 - Wheels

> python setup.py bdist_wheel

 After making the distribuing files. enter the following:

> twine upload dist/\*  

 **BUT**, after you release your python package, you cannot fix it. 

 You have to be careful of uploading your package, check your package. 

 So before releasing on main PyPI repo, I recommend you to use [PyPi test site](https://test.pypi.org/)

 - Upload as follows:

> twine upload --repository-url https://test.pypi.org/legacy/ dist/\*

 - install it 

> pip install --index-url https://test.pypi.org/simple/ your-package

But Ther are comfortable way to upload with **$HOME/.pypirc**

Create or modify **$HOME/.pypirc** with the following

```
[distutils]
index-servers=
    pypi
    testpypi

[pypi]
repository: https://pypi.python.org/pypi
username:your_username
password:your_password

[testpypi]
repository: https://test.pypi.org/legacy/
username: your testpypi username
password: your testpypi password
```

When you are with **$HOME/.pypirc** and twine, type in like this: 

> twine upload --repository testpypi dist/\*


OR


type in like this : 

The following is in Makefile

```
##################################################################
#                                                                #
#                            testpypi                            #
#                                                                #
##################################################################

# If you want to use another way, use the command below
# Reference : https://packaging.python.org/guides/using-testpypi/#using-test-pypi
#           : https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi
# python setup.py bdist_wheel
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*

testpypi:
	python setup.py register -r testpypi
	#python setup.py sdist --format=gztar upload -r testpypi
	python setup.py bdist_wheel upload -r testpypi
	# Execute manually below 
	# If you don't have the virtualenv, pip install virtualenv
	# cd /tmp
	# virtualenv venv
	# source venv/bin/activate
	# pip install --index-url https://test.pypi.org/simple/ konlp
	# deactivate 
	# virtualenv-3.5 venv3
	# source venv3/bin/activate
	# pip3 install --index-url https://test.pypi.org/simple/ konlp


##################################################################
#                                                                #
#                              pypi                              #
#                                                                #
##################################################################

# If you want to use another way, use the command below
# Reference : https://packaging.python.org/guides/using-testpypi/#using-test-pypi
#           : https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi
# python setup.py bdist_wheel
# twine upload dist/*

pypi:
	python setup.py register -r pypi
	#python setup.py sdist --format=gztar upload -r pypi
	python setup.py bdist_wheel upload -r pypi
```


# Reference 

 - [Example github](https://github.com/pypa/sampleproject)
 - [Tutorial of distributing package](https://packaging.python.org/tutorials/distributing-packages/#uploading-your-project-to-pypi)
 - [Using test pypi](https://packaging.python.org/guides/using-testpypi/#using-test-pypi)
 - [migrating to PyPi org](https://packaging.python.org/guides/migrating-to-pypi-org/)
 - [how to sumbit to PyPi](http://peterdowns.com/posts/first-time-with-pypi.html)
 - [example github](https://github.com/konltk/konlp)
 - [test pypi](https://test.pypi.org/)
 - [pypi org](https://pypi.org/)
 - [How to Publish Your Package on PyPI](https://blog.jetbrains.com/pycharm/2017/05/how-to-publish-your-package-on-pypi/)
 
 travis
  - [travis's example](https://github.com/travis-ci-examples)
  - [travis's python](https://docs.travis-ci.com/user/languages/python)
  - [traive with wordpress-plugin-travis](https://deliciousbrains.com/deploying-wordpress-plugins-travis/) 
