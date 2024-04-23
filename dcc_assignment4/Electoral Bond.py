import fitz
import csv
import pandas as pd

# def pdf_to_csv(pdf_file, csv_file):
#     # Open the PDF file
#     doc = fitz.open(pdf_file)
    
#     # Create a CSV file and initialize a CSV writer
#     with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.writer(csvfile)
        
#         # Iterate through each page in the PDF
#         for page in doc:
#             # Extract text from the page
#             text = page.get_text()
            
#             # Split the text into lines
#             lines = text.split('\n')
            
#             # Write each line to the CSV file
#             for line in lines:
#                 # Split the line by spaces or other delimiters based on your PDF's structure
#                 # Adjust this based on how your text is structured in the PDF
#                 row = line.split(' ')
                
#                 # Write the row to the CSV file
#                 writer.writerow(row)
# pdf_file = 'LAfUoSGjIp.pdf'
# csv_file = 'Electoral Bonds 1.csv'
# pdf_to_csv(pdf_file, csv_file)

# pdf_1 = 'oN2CT46X0E.pdf'
# csv_1 = 'Electoral Bonds 2 .csv'
# pdf_to_csv(pdf_1, csv_1)

def pdf_to_csv(pdf_file, csv_file):
    doc = fitz.open(pdf_file)
    data=[]
    for page in doc:
        Tabs =page.find_tables()
        if Tabs.tables:
            TABS=Tabs[0].extract()
        data.extend(TABS[1:])
    headings=[i.replace('\n',' ') for i in TABS[0]]
    ds=pd.DataFrame(data,columns=headings)
    ds["Denominations"]=ds["Denominations"]
    ds.to_csv(csv_file, index =False)
pdf_to_csv(r'"C:\Users\acer\OneDrive\Desktop\Flask_App_Demo-main\dcc_assignment4\LAfUoSGjIp.pdf"',r'EB Redemption Details.csv')
pdf_to_csv(r'"C:\Users\acer\OneDrive\Desktop\Flask_App_Demo-main\dcc_assignment4\oN2CT46X0E.pdf"', r'EB Purchase Details.csv')