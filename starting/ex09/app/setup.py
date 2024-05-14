from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    description='1337 Package',
    url='#',
    author='asalek',
    author_email='ayoub.salek8599@gmail.com',
    license='MIT',
    # packages=['ft_package'],
    packages=find_packages(),
    zip_safe=False #The zip_safe argument defines whether the package is installed in compressed mode or regular mode.
)