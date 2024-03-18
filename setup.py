from setuptools import setup, find_packages

# Read the contents of your text file
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Read the contents of README.md
readme_content = read_file('README.rst')

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
    version='0.2.3',
    author='Jonibek Yorkulov',
    author_email='jonibekyorkulov@gmail.com',
    description='Everything is very fast with Dangasa',
    long_description=readme_content,
    long_description_content_type='text/plain',
    url='https://github.com/jonibekyorkulov/dangasa',
    packages=find_packages(),
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
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
        # Define additional dependencies for extra features
    },
    entry_points={
        # Define console scripts or other entry points here
    },
    project_urls={
        'Bug Reports': 'https://github.com/jonibekyorkulov/dangasa/issues',
        'Source': 'https://github.com/jonibekyorkulov/dangasa',
    },
)
