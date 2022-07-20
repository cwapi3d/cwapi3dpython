from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='cwapi3d',
    version='1.3.10',
    author='Cadwork',
    author_email='it@cadwork.ca',
    description='Python bindings for CwAPI3D',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cwapi3d/cwapi3dpython',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.9, <4',
    packages=[
        'attribute_controller',
        'bim_controller',
        'cadwork',
        'connector_axis_controller',
        'element_controller',
        'endtype_controller',
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
    package_dir={'': 'src'},
    package_data={
        '': ['*.pyi'],
    },
    include_package_data=True,
)
