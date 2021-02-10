import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ChimuApi",
    version="0.1.5",
    author="Lenforiee",
    author_email="lenforiee@misumi.me",
    description="API Wrapper around Chimu.moe API for both synchronous and asynchronous purposes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lenforiee/ChimuApi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)