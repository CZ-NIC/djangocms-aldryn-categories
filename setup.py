from setuptools import setup, find_packages
from aldryn_categories import __version__

setup(
    name='djangocms-aldryn-categories',
    version=__version__,
    url='https://github.com/CZ-NIC/djangocms-aldryn-categories',
    license='BSD License',
    description='Hierarchical categories/taxonomies for your Django project.',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    author='Divio AG',
    author_email='info@divio.ch',
    packages=find_packages(),
    platforms=['OS Independent'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires=[
        'djangocms-aldryn-translation-tools',
    ],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.7'
)
