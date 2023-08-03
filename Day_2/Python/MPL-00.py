import matplotlib as mp
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"text.usetex": True, 
                     'text.latex.preamble': r'\usepackage{siunitx}', 
                     'pgf.preamble': r'\usepackage{siunitx}', 
                     'pgf.texsystem': 'lualatex',
                     'font.family':'serif',
                     'font.serif' : 'cm'})

plt.rcParams["text.latex.preamble"].join([
        r"\usepackage{siunitx}\usepackage{sansmath}",              
        r"\setmainfont{Audiowide}",
])

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
#plt.savefig("myImagePDF.pdf", format="pdf", bbox_inches="tight")
plt.savefig('figure.pdf', backend='pgf')
#plt.show()
