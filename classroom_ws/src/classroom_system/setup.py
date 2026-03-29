from setuptools import find_packages, setup

package_name = 'classroom_system'

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
    maintainer='z',
    maintainer_email='z@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            # ---------------------------------------------------------------------------
            # PUBLISHER NODES
            # Format: 'run_command = package.file:main'
            # ---------------------------------------------------------------------------

            # Registers tamil_publisher.py → run with:
            # ros2 run classroom_system tamil_publisher
            'tamil_publisher = classroom_system.tamil_publisher:main',

            # Registers english_publisher.py → run with:
            # ros2 run classroom_system english_publisher
            'english_publisher = classroom_system.english_publisher:main',

            # ---------------------------------------------------------------------------
            # SUBSCRIBER NODES
            # ---------------------------------------------------------------------------

            # Registers class_a_node.py → run with:
            # ros2 run classroom_system class_a
            'class_a = classroom_system.class_a_node:main',

            # Registers class_b_node.py → run with:
            # ros2 run classroom_system class_b
            'class_b = classroom_system.class_b_node:main',
        ],
    },
)
