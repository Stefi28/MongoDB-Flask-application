import pandas as pd
import re
from cleanco import basename
from config import connect_to_sqldb, connect_to_mongodb
import json
from bson import json_util


def clean_company_names(company_name):
    company_name = re.sub(r'[,\(\)\"]', '', company_name)
    company_name = re.sub(r'\s-.*', '', company_name)
    company_name = basename(company_name).title()
    company_name = re.sub(r'\b(Ltd|Limited)\b', '', company_name).strip()
    company_name = re.sub(r'([A-Z]+)\s([A-Z]+)', lambda m: m.group(1) + ' & ' + m.group(2), company_name)
    return company_name


def update_db():
    conn = connect_to_sqldb()
    c = conn.cursor()

    chunk_size = 1000
    offset = 0
    while True:
        companies = pd.read_sql_query("SELECT * FROM companies LIMIT %d OFFSET %d" % (chunk_size, offset), conn)
        if companies.empty:
            break

        companies = companies.apply(clean_company_names, axis=1)
        companies.to_sql("companies", conn, if_exists="replace", index=False)

        offset += chunk_size

    conn.commit()
    c.close()
    conn.close()


def write_to_mongodb():
    conn = connect_to_mongodb()
    companies_collection = conn["companies"]

    companies = pd.read_sql_query("SELECT * FROM companies", connect_to_sqldb())
    companies = companies.apply(clean_company_names, axis=1)

    for index, row in companies.iterrows():
        company_dict = row.to_dict()
        companies_collection.update_one({"_id": company_dict["id"]}, {"$set": company_dict}, upsert=True)


def mongodb_to_html():
    conn = connect_to_mongodb()
    companies_collection = conn["companies"]

    companies = list(companies_collection.find().limit(20))
    return json.dumps(companies, default=json_util.default)

