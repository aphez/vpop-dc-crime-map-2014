import pandas as pd
import pyproj
df = pd.read_csv("20160212_CrimeLocation2014_V2.csv")
out = [pyproj.transform(pyproj.Proj(init='EPSG:26985'),pyproj.Proj(init='EPSG:4326'),x,y) for i,x,y in df[['BLOCKXCOORD','BLOCKYCOORD']].itertuples()]
outdf = pd.DataFrame(out)
outdf.columns = ['Long','Lat']
outdf.to_csv("outcrime.csv",index=False)