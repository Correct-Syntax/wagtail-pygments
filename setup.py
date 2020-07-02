import setuptools


with open('README.rst', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='wagtail-pygments',
    version='0.1.1',
    description='A block render syntax highlighter for Wagtail CMS.',
    long_description=long_description,
    url='https://github.com/truongvan/wagtail-pygments.git',
    author='Truong Van',
    author_email='truongvan@live.com',
    license='BSD-3-Clause',
    py_modules=['wagtail_pygments'],
    packages=setuptools.find_packages(),
    install_requires=[
        'pygments>=2.6',
        'wagtail>=2',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ]
)
