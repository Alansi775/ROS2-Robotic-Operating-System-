from setuptools import setup

package_name = 'midterm_app'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='safamoqbel',
    maintainer_email='mohamedalezzi6@gmail.com',
    description='Robot status info publisher and subscriber in ROS 2 Humble',
    license='MIT',
    entry_points={
        'console_scripts': [
            'status_publisher = midterm_app.scripts.status_publisher_node:main',
            'status_subscriber = midterm_app.scripts.status_subscriber_node:main',
        ],
    },
)
