import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'python_hello',
    version = '0.0.1',
    author = 'wwzz3077',
    author_email = 'wtzhao@hotmail.com',
    description = 'A function that returns [hello, world]',
    long_description = long_description,
    url = 'https://github.com/wwzz3077/python_hello',
    packages= setuptools.find_packages(),
    keywords= ['python', 'wwzz3077'],
    install_requires = [
        'python_world@https://github.com/wwzz3077/python_world#egg=python_world-0.0.1',
    ]
)
