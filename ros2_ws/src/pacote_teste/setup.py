from setuptools import find_packages, setup

package_name = 'pacote_teste'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='heverton',
    maintainer_email='hevertonsilvadesouza@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "pub = pacote_teste.pub:main",
            "sub = pacote_teste.sub:main"
        ],
    },
)
