from distutils.core import setup

setup(
    name='phiggs',
    version='0.0.1',
    description='(P)ython (Hi)erarchical (G)raph (G)enerating (S)ystem',
    long_description="Python framework for generating directed acyclic graphs with a hierarchical tree structure.",
    url='https://github.com/meyersbs/PHiGGS/',
    author='Benjamin S. Meyers',
    author_email='admin@lionlogic.org',
    license='MIT',
    scripts=['phiggs/phiggs'],
    keywords=['tree', 'visualization', 'graph', 'hierarchy', 'graphviz'],
    package_data={},
    packages=[
        'phiggs',
    ],
    download_url='https://github.com/meyersbs/PHiGGS/archive/v0.0.1.tar.gz',
    requires=[],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
