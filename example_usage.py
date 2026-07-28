from client import PdfDataExtractorClient

def main():
    client = PdfDataExtractorClient()
    res = client.extract_pdf_tables(pdf_name='quarterly_report.pdf')
    print(f"Result for extracted_tables: {res['extracted_tables']}")

if __name__ == "__main__":
    main()
