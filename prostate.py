import pandas as pd

# todo: change this to use urllib2, instead of local file
# info... http://stackoverflow.com/questions/1393324/in-python-given-a-url-to-a-text-file-what-is-the-simplest-way-to-read-the-cont

df = pd.read_csv('prostate.data',sep='\t',index_col=0)

df['Intercept'] = 1

print df.head()
