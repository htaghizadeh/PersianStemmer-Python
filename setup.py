from setuptools import setup

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE', encoding='utf-8') as f:
    license = f.read()

setup(
        name='PersianStemmer',
        version='1.0.0',
        description='Persian Stemmer for Python',
        author='Hossein Taghi-Zadeh',
        author_email='h.t.azeri@gmail.com',
        url='https://github.com/MrHTZ/PersianStemmer-Python',
        license=license,
        package_data={'': ['data/*']},
        classifiers=[
            'Topic :: Text Processing',
            'Natural Language :: Persian',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
        ],
        install_requires=['patricia-trie']
)
