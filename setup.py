from distutils.core import setup


setup(
    name='gendisplay',
    py_modules=['gendisplay'],
    packages=['funniest'],
    version="1.0",
    description="Generic Display class for MicroPython.",
    long_description="""\
Generic Display class for MicroPython.""",
    author='Dave Amphlett',
    author_email='dave@davelopware.com',
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
