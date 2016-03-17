from setuptools import setup

setup(
    name='lektor-root-relative-path',
    version='0.1',
    author=u'Atsushi Suga',
    author_email='',
    license='MIT',
    py_modules=['lektor_root_relative_path'],
    entry_points={
        'lektor.plugins': [
            'root-relative-path = lektor_root_relative_path:RootRelativePathPlugin',
        ]
    }
)
