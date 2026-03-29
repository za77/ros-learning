from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'smart_school'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # Include all launch files
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),

        # Include all config files
        (os.path.join('share', package_name, 'config'),
            glob('config/*.yaml'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='z',
    maintainer_email='z@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
             'attendance_server = smart_school.attendance_server:main',
             'attendance_client = smart_school.attendance_client:main',
             'bell_scheduler = smart_school.bell_scheduler:main',
             'school_monitor = smart_school.school_monitor:main'
        ],
    },
)
