from setuptools import setup

setup(
    name='rpicarserver',
    version='0.1',
    description='',
    url='https://github.com/krixian/rpi-car-server',
    author='krixian',
    author_email='1101758+krixian@users.noreply.github.com',
    license='MIT',
    packages=['rpicarserver'],
    zip_safe=False,
    entry_points={
        'rpicarserver.ext': [
            'backlight = rpicarserver.backlight:Extension',
        ]
    }
)