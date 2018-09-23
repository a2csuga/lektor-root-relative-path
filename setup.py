import io
from setuptools import setup

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

setup(
    name='lektor-root-relative-path',
    author=u'Atsushi Suga',
    author_email='a2csuga@users.noreply.github.com',
    version='0.2.0',
    classifiers=[
        'Framework :: Lektor',
        'Environment :: Plugins',
    ],
    url='http://github.com/a2csuga/lektor-root-relative-path',
    license='MIT',
    install_requires=open('requirements.txt').read(),
    packages=['lektor_root_relative_path'],
    description='Root relative path plugin for Lektor',
    long_description=readme,
    long_description_content_type='text/markdown',
    entry_points={
        'lektor.plugins': [
            'root-relative-path = lektor_root_relative_path:RootRelativePathPlugin',
        ]
    }
)
