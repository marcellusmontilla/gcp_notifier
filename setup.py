from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="gcp_notifier",
    version="0.1.0",
    description="Notification microservice for Email and Google Chat, ready for Cloud Run.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="YOUR NAME",
    author_email="your@email.com",
    url="https://github.com/yourusername/gcp_notifier",
    packages=find_packages(),
    install_requires=[
        "requests",
        "google-cloud-secret-manager",
        "google-auth"
    ],
    python_requires=">=3.8",
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
