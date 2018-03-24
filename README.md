# PersianStemmer-Python

## Installation
`pip install PersianStemmer`
`pip install https://github.com/htaghizadeh/PersianStemmer-Python/archive/master.zip --upgrade`

## Code Example

```python
from PersianStemmer import PersianStemmer 

ps = PersianStemmer()
print(ps.run("زیباست"))

# or NLTK compatible form
print(ps.stem("زیباست"))
```

## Citation
If you use this software please cite the followings:

Taghi-Zadeh, Hossein and Sadreddini, Mohammad Hadi and Diyanati, Mohammad Hasan and Rasekh, Amir Hossein. 2015. *A New Hybrid Stemming Method for Persian Language*. In *Digital Scholarship in the Humanities*. The Oxford University Press.
[DOI](http://dx.doi.org/10.1093/llc/fqv053)
[Link](http://dsh.oxfordjournals.org/content/early/2015/11/06/llc.fqv053.abstract)

H. Taghi-Zadeh and M. H. Sadreddini and M. H. Dianaty and A. H. Rasekh. 2013. *A New Rule-Based Persian Stemmer Using Regular Expression (In Persian)*. In *Iranian Conference on Intelligent Systems (ICIS 2013)*, pages 401–407.
[Link](http://www.civilica.com/Paper-ICS11-ICS11_109.html)
