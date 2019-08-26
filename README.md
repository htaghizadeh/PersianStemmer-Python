# PersianStemmer-Python

## Installation
```
  pip install PersianStemmer
  pip install https://github.com/htaghizadeh/PersianStemmer-Python/archive/master.zip --upgrade
```

## Code Example

```python
from PersianStemmer import PersianStemmer 

ps = PersianStemmer()
print(ps.run("زیباست"))

# or NLTK compatible form
print(ps.stem("زیباست"))
```

## Citation
To cite the paper/code, please use this BibTex:

```
@article{10.1093/llc/fqv053,
    author = {Taghi-Zadeh, Hossein and Sadreddini, Mohammad Hadi and Diyanati, Mohammad Hasan and Rasekh, Amir Hossein},
    title = "{A new hybrid stemming method for persian language}",
    journal = {Digital Scholarship in the Humanities},
    volume = {32},
    number = {1},
    pages = {209-221},
    year = {2015},
    month = {11},
    issn = {2055-7671},
    doi = {10.1093/llc/fqv053},
    url = {https://doi.org/10.1093/llc/fqv053},
    eprint = {http://oup.prod.sis.lan/dsh/article-pdf/32/1/209/11046608/fqv053.pdf},
}

```

Taghi-Zadeh, Hossein and Sadreddini, Mohammad Hadi and Diyanati, Mohammad Hasan and Rasekh, Amir Hossein. 2017. *A New Hybrid Stemming Method for Persian Language*. In *Digital Scholarship in the Humanities*. The Oxford University Press.
[DOI](https://doi.org/10.1093/llc/fqv053)
[Link](https://academic.oup.com/dsh/article-abstract/32/1/209/2957378)

H. Taghi-Zadeh and M. H. Sadreddini and M. H. Dianaty and A. H. Rasekh. 2013. *A New Rule-Based Persian Stemmer Using Regular Expression (In Persian)*. In *Iranian Conference on Intelligent Systems (ICIS 2013)*, pages 401–407.
[Link](http://www.civilica.com/Paper-ICS11-ICS11_109.html)


If you have questions, send me an email: h.t.azeri at gmail dot com
