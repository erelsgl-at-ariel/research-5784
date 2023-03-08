import setuptools, pathlib

NAME = "example_pypi_package_5782"
URL = "https://github.com/tomchen/example_pypi_package/"
HERE = pathlib.Path(__file__).parent
print(f"\nHERE = {HERE.absolute()}\n")
README = (HERE / "README.md").read_text()
REQUIRES = (HERE / "requirements.txt").read_text().strip().split("\n")
REQUIRES = [lin.strip() for lin in REQUIRES]
print(f'\nVERSION = {(HERE / "examplepy" / "VERSION").absolute()}\n')
VERSION = (HERE / "examplepy" / "VERSION").read_text().strip()
# See https://packaging.python.org/en/latest/guides/single-sourcing-package-version/

setuptools.setup(
    name=NAME,
    version=VERSION,

    packages=setuptools.find_packages(),
    install_requires=REQUIRES,

    author='Tom Chen',
    author_email='tomchen.org@gmail.com',
    description='Example PyPI Package',
    keywords='example, pypi, package',
    license="MIT",

    long_description=README,
    long_description_content_type='text/markdown',

    url=URL,
    project_urls={
        'Documentation': URL,
        'Bug Reports': URL+'/issues',
        'Source Code': URL,
    },

    python_requires='>=3.8',
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 7 - Inactive',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

    include_package_data= True,
)

# Build:
#   Delete old folders: build, dist, *.egg_info, .venv_test.
#   Then run:
#        build
#   Or (old version):
#        python setup.py sdist bdist_wheel


# Publish to test PyPI:
#   twine upload --repository testpypi dist/*

# Publish to real PyPI:
#   twine upload --repository pypi dist/*


# Test in a virtual environment:
#    cd ..
#    virtualenv test_env
#    test_env\Scripts\activate
#    pip install numpy
#    pip install -i https://test.pypi.org/simple/ example-pypi-package-5782
#    pytest test_env\Lib\site-packages\examplepy
