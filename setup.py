from setuptools import setup, find_packages

setup(
    name="service_collection",
    version="0.1.0",
    author="Alec Meyer",
    author_email="11meyal@gmail.com",
    description="ASP.NET Core-style dependency injection service collection for Python",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ameyer117/service_collection",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "Framework :: FastAPI",
        "Programming Language :: C#",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9,<=3.12",
    project_urls={
        "Homepage": "https://github.com/ameyer117/service_collection",
        "Documentation": "https://github.com/ameyer117/service_collection",
        "Source": "https://github.com/ameyer117/service_collection",
    },
)
