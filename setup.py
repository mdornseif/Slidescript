from setuptools import setup, find_packages
setup(
    name = "Slidescript",
    version = "1.0dev",
    packages = find_packages(),
    scripts = ['slidec'],
    install_requires = ['argparse', 'xlwt'],

    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.slide'],
    },

    # metadata for upload to PyPI
    author = "Maximillian Dornseif",
    author_email = "md@hudora.de",
    description = "Programming language for people who hate Excel",
    license = "BSD",
    url = "http://github.com/mdornseif/Slidescript",

    # could also include long_description, download_url, classifiers, etc.
)