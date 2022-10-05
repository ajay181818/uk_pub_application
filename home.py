#import requirements
import streamlit as st
import pandas as pd
import numpy as np

#reading dataset
df=pd.read_csv('open_pubs.csv')
#assigning column names to the dataset
df.columns=['fsa_id','name','address','postcode','easting','northing','lat','lon','local_authority']
#replacing '\N' with null value
df=df.replace('\\N',np.NaN)
#removing null value rows
df=df.dropna()

#finding unique local_authority 
data_selection =df.local_authority.unique()
#displaying details
pub="Total no of PUBS: "+str(df.shape[0])
auth="Total no of PUB's Local Authority: "+str(data_selection.shape[0])
lat_range= "Latitude Range: "+str(df['lat'].min())+" to "+str(df['lat'].max())
lon_range= "Longitude Range: "+str(df['lon'].min())+" to "+str(df['lon'].max())

st.title("OPEN PUB APPLICATION ")
st.subheader("Time for some drinks")


st.subheader(pub)
st.subheader(auth)
st.subheader(lat_range)
st.subheader(lon_range)
st.sidebar.success("Select your required page")
information = st.sidebar.selectbox(
    "Statistical Data",
    ('Number of Pub\'s','Data_shape','Head', 'Tail', 'Unique Area\'s', 'Null values', 'Describe'))

if information=='Number of Pub\'s':
    st.markdown(f'**{df.shape[0]}**  Pubs  in  **UK**')

elif information == 'Data_shape':
    st.text('Number of rows: {}'.format(df.shape[0]))
    st.text('Number of columns: {}'.format(df.shape[1]))

elif information == 'Head':
    st.dataframe(df.head())

elif information == 'Tail':
    st.dataframe(df.tail())

elif information=='Unique Area\'s':
    st.markdown(f'Total no of unique locations where pubs are present in UK is **{len(df["local_authority"].unique())}** ')

elif information == 'Null values':
    st.markdown('**We can see that there are no null values in the data**')
    st.table(df.isna().sum())

elif information == 'Describe':
    st.table(df.describe())