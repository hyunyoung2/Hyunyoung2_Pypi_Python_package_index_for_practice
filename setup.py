from setuptools import setup, find_packages

# Setuptools
setup(
    name="nlppypitest",
    description="pypi-test practice",
    version=0.0.1, # We are dealing with as variable by reading VERSION file under konlp directory 
    url="https://hyunyoung2.github.io",
    long_description="""\
KoNLP is Natural Language Processing Toolkit and Python package for
Korean natural Language precessing. KoNLP currently requires Python 3.5.""",
    license="", # later on, We select it
    keywords=['NLP', 'KoNLTK', 'NLPK',
              'koNLP', 'konltk', 'nlpk', 'konlp',
              'korean natural langugae processing', 'natural language processing',
              'parsing', 'tagging', 'tokenizing',
              'morpheme anaylisis', 'chunk',
              'natural language', 'text anayltics'],
    author="Hyunyoung Lee, GyuHyeon Nam", # Later on, maintainer
    author_email="hyun02.engineer@gmail.com, ngh3053@gmail.com",
    classifiers=[
        # How mature is this project? common value are
        #    3 - Alpha
        #    4 - Beta
        #    5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is inteded for
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        #'License :: ',
        #'Operating System :: OS Dependent', # Later on, we change it into OS Independent
        #'Programming Language :: Python :: 2.7', # Later on, we support it
        'Programming Language :: Python :: 3.5',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic',
    ],
    package_data={'nlppypitest':['lib/*', 'VERSION']}, # Later on we have to change it
    install_requires=[], # Later on, we have to select
    packages=find_packages(), # later on, with exclude setting
    extras_require={}, # Later on, refer to k-NLTK resource
    python_requires='>=3', # Later on, we change this to classifier above
    zip_safe=False, # Later on, we look for exact reason
    # Later on, We have to search for additional condition from Python
    )
