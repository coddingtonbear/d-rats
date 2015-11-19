from setuptools import setup, find_packages

from d_rats.version import DRATS_VERSION


base_setup = {
    'name': 'd-rats',
    'description': 'D-RATS',
    'long_description': 'A communications tool for D-STAR',
    'author': 'Dan Smith, KK7DS',
    'author_email': 'kk7ds@danplanet.com',
    'packages': find_packages(),
    'version': DRATS_VERSION,
    'entry_points': {
        'console_scripts': [
            'd-rats = d_rats.cmdline.main:main',
            'd-rats_repeater = d_rats.cmdline.repeater:main',
            'd-rats_mapdownloader = d_rats.cmdline.mapdownloader:main',
        ]
    }
}


def default_build():
    setup(
        **base_setup
    )


default_build()
