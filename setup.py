"""Setup configuration for Aim Trainer Plus."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [
        line.strip() for line in fh if line.strip() and not line.startswith("#")
    ]

setup(
    name="aim-trainer-plus",
    version="1.0.0",
    author="Aim Trainer Plus Contributors",
    description="A pygame-based aim trainer to improve mouse accuracy and speed",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sailboy42/aim-trainer-plus",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "aim-trainer=src.aim_trainer_game:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["assets/*"],
    },
)
