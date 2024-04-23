### WEB DEVELOPMENT WITH FLASK
#### Task 1: Loading the PDF files and converting them to CSV using Fitz.
The given database consists of the data for electoral bonds of the 2024 elections.
It contains two files, namely:
1. Purchase Details: It contains information about when and by whom an electoral bond was purchased.
2. Redemption Details: This dataset consists of the details of the pay branch and the pay teller.

These datasets are in the form of PDFs.
To be able to perform data analysis on it, we need to convert it to .csv format. For this, I used the FITZ library.

![Code to convert PDF files to csv Format](https://github.com/Nirjara07/DCC_Assignment4_23110220/assets/143330260/b5041364-ffaf-4a88-b1b8-f52abfc2cc2a)

The Fitz library can be installed by giving the prompt 'pip install PyMuPDF' in the VSCODE terminal and then using the import fitz command in the Python file.

As we can see, two new CSV files with the desired names have been created in the required folder.

![csv output](https://github.com/Nirjara07/DCC_Assignment4_23110220/assets/143330260/dd40e439-67ec-48c9-92a6-29a69254d272)


#### Task 2: Uploading the CSV files on MySQL as a database
To upload the CSV files as tables to MySQL, we create a new schema and add the tables.
Following is the code to create a new schema electoral_  bonds and add the data from the CSV file redemption details.

![image](https://github.com/Nirjara07/DCC_Assignment4_23110220/assets/143330260/5a970f9b-4e44-4820-9abc-dc957fe94529)

Upload the second table in the same manner.

Now, right-click on the tables section in the navigation bar and click on the Table Data Import Wizard option.
The following window will appear.
Choose the desired file and click on next.
![image](https://github.com/Nirjara07/DCC_Assignment4_23110220/assets/143330260/20bd4370-81ed-4218-b448-0ca161cd7661)

Use the existing table to import the data.
![image](https://github.com/Nirjara07/DCC_Assignment4_23110220/assets/143330260/08246710-9b89-44ef-81d6-1f9991f0004f)

Verify the column mapping of the CSV file and the created table.
![image](https://github.com/Nirjara07/DCC_Assignment4_23110220/assets/143330260/e7d9f333-83d3-4c0f-b742-4a0584538557)

An import data window will appear as shown below:
![image](https://github.com/Nirjara07/DCC_Assignment4_23110220/assets/143330260/e1a5fccc-4b5e-4215-b482-2cb4911aebcf)

Now, we have two desired tables in the schema electoral_bonds.

#### Task 3: Connecting the backend to the front end using Flask.

To connect the SQL Backend to the front end, we use the following pyhton code, changing the host to local server(or whichever server may be used), and the password to the MySQL workbench password, otherwise, the  commands may not be executed.

![image](https://github.com/Nirjara07/DCC_Assignment4_23110220/assets/143330260/b2955fc2-cf8c-4933-9c82-fbcc4e837bf1)




