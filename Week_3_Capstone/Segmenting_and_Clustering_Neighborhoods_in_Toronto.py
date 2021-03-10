##Segmenting and Clustering Neighborhoods in Toronto
#Import requests and Pandas
import requests
import pandas as pd

#Get the HTML of the Wiki page, convert into a table with help of read_html (read HTML tables into a list of DataFrame objects), remove cells with a borough that is Not assigned.
wiki = 'https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M'
wikipedia_page = requests.get(wiki)
df_raw = pd.read_html(wikipedia_page.content, header=0)[0]
df_new = df_raw[df_raw.Borough != 'Not assigned']

df_new.head()

df_new.loc[df_new.Neighbourhood == 'Not assigned']

df_new.Neighbourhood.replace('Not assigned',df_new.Borough,inplace=True)
df_new.head(8)


df_toronto = df_new.groupby(['Postcode', 'Borough'])['Neighbourhood'].apply(lambda x: ', '.join(x))
df_toronto = df_toronto.reset_index()
df_toronto.rename(columns = {'Postcode':'PostalCode'}, inplace = True)
df_toronto.rename(columns = {'Neighbourhood':'Neighborhood'}, inplace = True)
df_toronto.head()


df_toronto.shape
