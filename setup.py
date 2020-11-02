import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name='cwapi3d',
  version='0.11',
  author='Cadwork Montreal',
  author_email='it@cadwork.ca',
  description='Python bindings for CwAPI3D',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/CadworkMontreal/cwapi3d',
  packages=[
    'attribute_controller',
    'bim_controller',
    'cadwork',
    'connector_axis_controller',
    'element_controller',
    'file_controller',
    'geometry_controller',
    'list_controller',
    'machine_controller',
    'material_controller',
    'menu_controller',
    'roof_controller',
    'scene_controller',
    'shop_drawing_controller',
    'utility_controller',
    'visualization_controller'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Environment :: Plugins',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries',
  ],
  python_requires='>=3.7',
  package_data={
    '': ['*.pyi'],
  },
  include_package_data=True,
)
