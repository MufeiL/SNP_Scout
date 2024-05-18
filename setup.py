import os
from setuptools import setup, find_packages

# Version keeping code
curdir = os.path.abspath(os.path.dirname(__file__))
version_file = os.path.join(curdir, 'snp_scout/version.py')

MAJ = 0
MIN = 0
REV = 0
VERSION = f'{MAJ}.{MIN}.{REV}'

with open(version_file, 'w') as fout:
    fout.write(
        f"""
        # THIS FILE IS GENERATED FROM SETUP.PY
        version = '{VERSION}'
        __version__ = version
        """
    )

setup(
    name='snp_scout',
    version=VERSION,
    description='CSE185 Project',
    author='Mufei Li, Sally Ha, Margaret Jones',
    author_email='mul009@ucsd.edu, s1ha@ucsd.edu, mwjones@ucsd.edu',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snp_scout=snp_scout.snp_scout:main"
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
