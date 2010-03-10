from setuptools import setup, find_packages
setup(
    name = "Slidescript",
    version = "1.0dev",
    packages = ['slidescript', 'slidescript.antlr3'],
    scripts = ['slidec'],
    # metadata for upload to PyPI
    author = "Maximillian Dornseif",
    author_email = "md@hudora.de",
    description = "Programming language for people who hate Excel",
    license = "BSD",
    url = "http://github.com/mdornseif/Slidescript",
    zip_safe=False,
    # could also include long_description, download_url, classifiers, etc.
    install_requires = ['argparse', 'xlwt', 'odict'],
)