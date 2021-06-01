import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pedestrian_movement",
    version="0.0.3",
    author="Michael Hartmann",
    author_email="michael.hartmann@v2c2.at",
    description="Human Locomotion Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "GitHub": "https://github.com/ga74kud/pedestrian_movement.git",
        "Bug Tracker": "https://github.com/ga74kud/pedestrian_movement.git",
    },
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    install_requires=["matplotlib"],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=2.7",
)