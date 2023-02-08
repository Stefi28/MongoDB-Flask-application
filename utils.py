import re
import pandas as pd
from cleanco import basename
from config import connect_to_sqldb, connect_to_mongodb
from bson import json_util


def clean_company_names(company_name):
    # Clean unwanted characters: commas and full text after commas, brackets and text in them, quotation marks, dashes when not part of the company name.
    company_name = re.sub(r'[,\(\)\[\]\"\']', '', company_name)
    # Clean legal entity: LIMITED, LTD., ltd. Limited, limited.
    company_name = re.sub(r'(LTD|Limited)', '', company_name).strip()
    # The name should only be with initial capital letters
    company_name = company_name.title()
    # If acronyms are used in the name, then the acronym should be in capital letters
    company_name = re.sub(r'([A-Z][a-z]+)', lambda x: x.group(0).upper(), company_name)
    return company_name

def update_db():
    conn = connect_to_sqldb()
    cursor = conn.cursor()

    # Read the data in chunks of 1000
    chunk_size = 1000
    chunk = pd.read_sql("SELECT * FROM companies", conn, chunksize=chunk_size)
    for i, df in enumerate(chunk):
        for index, row in df.iterrows():
            company_name = row['name']
            cleaned_name = clean_company_names(company_name)
            # Update the cleaned name in the database
            cursor.execute("UPDATE companies SET company_name_cleaned=? WHERE id=?", (cleaned_name, row['id']))
        # Commit changes after every chunk
        conn.commit()
    cursor.close()
    conn.close()

def write_to_mongodb():
    db = connect_to_mongodb()
    companies_collection = db.companies
    conn = connect_to_sqldb()
    df = pd.read_sql("SELECT * FROM companies", conn)
    for index, row in df.iterrows():
        company = {
            'name': row['company_name_cleaned'],
            'country_iso': row['country_iso'],
            'city': row['city'],
            'nace': row['nace'],
            'website': row['website']
        }
        # Insert the company into the MongoDB collection
        companies_collection.insert_one(company)
    conn.close()

def mongodb_to_html():
    db = connect_to_mongodb()
    companies_collection = db.companies
    companies = companies_collection.find().limit(20)
    return json.dumps(list(companies), default=json_util.default)


