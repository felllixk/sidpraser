from setuptools import setup, find_packages

setup(
    name='SidParser',
    version='0.1.0',
    author='felllixk',
    author_email='felllixk@gmail.com',
    description='Parse sid & and associate with logs',
    packages=find_packages(),
    install_requires=[
        'requests',
        'bs4',
        'PyQt6',
        'pyqt-tools',
        'pyinstaller'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.10',
)
