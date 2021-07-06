import setuptools
import subprocess

with open("README.md", "r") as fh:
    long_description = fh.read()

version = subprocess.run(['git', 'rev-list', '--all', '--count'], stdout=subprocess.PIPE)
version = version.stdout.decode('utf-8').replace('\n', '').replace('\r', '')

req = []
with open('requirements.txt', 'r') as file:
    for line in file:
        if line != '' or line != '\n':
            req.append(line)

setuptools.setup(
    name="pibot",
    version=version,
    author="TUC-RoboSchool",
    author_email="felix.kettner@informatik.tu-chemnitz.de",
    description="Library for controlling the PiBot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.hrz.tu-chemnitz.de/ketf--tu-chemnitz.de/hufa-pibot",
    packages=setuptools.find_packages(),
    package_dir={'pibot': 'pibot'},
    install_requires=req,
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3.0 (gpl-3.0)",
        "Operating System :: OS Independent",
    ],
)
