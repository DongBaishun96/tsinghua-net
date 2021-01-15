from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="tsinghua_net_dongbaishun",
    version="1.0.0",
    description="Tsinghua network tools",
    long_description=long_description,
    license="Apache 2.0 Licence",

    url="https://github.com/DongBaishun96/tsinghua-net",
    author="dongbaishun",
    author_email="dbs18@mails.tsinghua.edu.cn",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['requests', 'schedule', 'chardet'],

    scripts=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'tsinghua_net=tsinghua_net_dongbaishun.tsinghua_net:main'
        ]
    }
)

