from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

with open('LICENSE', encoding='utf-8') as f:
    license = f.read()

setup(
        name='PersianStemmer',
        version='1.0.0',
        description='Persian Stemmer for Python',
        author='Hossein Taghi-Zadeh',
        author_email='h.t.azeri@gmail.com',
        url='https://github.com/htaghizadeh/PersianStemmer-Python',
        license=license,
        package_data={'': ['data/*']},
        keywords=['persian','information-retrieval','nlp','morphological analysis','stemming algorithms','stemmers'],
        packages=find_packages(),
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',            
            'Topic :: Text Processing',
            'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
            'Topic :: Text Processing :: Indexing',
            'Topic :: Text Processing :: Linguistic',
            'Natural Language :: Persian',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
        ],
        install_requires=['patricia-trie']
)
