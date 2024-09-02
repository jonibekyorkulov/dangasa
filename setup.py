from setuptools import setup, find_packages

# Read the contents of your text file

with open('README.rst', 'r', encoding='utf-8') as f:
    long_description = f.read()
# List of template files
template_files = [
    'ListCreateApiView.py-tpl',
    'RetrieveAPIView.py-tpl',
    'serializers_class.py-tpl',
    'serializers.py-tpl',
    'urls.py-tpl',
    'views.py-tpl'
]

setup(
    name='Dangasa',
    version='0.2.8',
    author='Jonibek Yorkulov',
    author_email='jonibekyorkulov@gmail.com',
    description='Everything is very fast with Dangasa',
    long_description= long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/jonibekyorkulov/dangasa',
    packages=find_packages(),
    install_requires=[
        'djangorestframework>=3.14.0',
        'drf-yasg>=1.21.6',
    ],
    include_package_data=True,
    package_data={'': template_files},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    extras_require={
      
    },
    entry_points={
        'console_scripts': [
            'Dangasa = dangasa:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/jonibekyorkulov/dangasa/issues',
        'Source': 'https://github.com/jonibekyorkulov/dangasa',
    },
)
