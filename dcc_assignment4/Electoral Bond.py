import fitz
import csv
import pandas as pd
def convert(pdf_file, csv_file):
    doc = fitz.open(pdf_file)
    data=[]
    for i in doc:
        tables =i.find_tables()
        if tables.tables:
            TABS=tables[0].extract()
        data.extend(TABS[1:])
    headings=[i.replace('\n',' ') for i in TABS[0]]
    df=pd.DataFrame(data,columns=headings)
    df["Denominations"]=df["Denominations"]
    df.to_csv(csv_file, index =False)
convert(r'"C:\Users\acer\OneDrive\Desktop\Flask_App_Demo-main\dcc_assignment4\LAfUoSGjIp.pdf"',r'EB Redemption Details.csv')
convert(r'"C:\Users\acer\OneDrive\Desktop\Flask_App_Demo-main\dcc_assignment4\oN2CT46X0E.pdf"', r'EB Purchase Details.csv')
