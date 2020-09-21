import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="cwapi3d",
  version="0.10",
  author="Cadwork Montreal",
  author_email="it@cadwork.ca",
  description="Python bindings for CwAPI3D",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/CadworkMontreal/cwapi3d",
  packages=setuptools.find_packages(),
  classifiers=[
    "Development Status :: 3 - Alpha",
    "Environment :: Win32 (MS Windows)",
    "Intended Audience :: Developers",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python :: 3",
    "Topic :: Software Development :: Libraries",
    "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
  ],
  python_requires=">=3.7",
  package_data={
    '': ['*.pyi'],
  },
  include_package_data=True,
)
