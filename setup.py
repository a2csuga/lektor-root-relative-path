from setuptools import setup

setup(
    name='lektor-root-relative-path',
    author=u'Atsushi Suga',
    author_email='a2csuga@users.noreply.github.com',
    version='0.1',
    url='http://github.com/a2csuga/lektor-root-relative-path',
    license='MIT',
    packages=['lektor_root_relative_path'],
    description='Root relative path plugin for Lektor',
    entry_points={
        'lektor.plugins': [
            'root-relative-path = lektor_root_relative_path:RootRelativePathPlugin',
        ]
    }
)
