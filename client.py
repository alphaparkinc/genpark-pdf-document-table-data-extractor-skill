class PdfDataExtractorClient:
    def extract_pdf_tables(self, pdf_name: str) -> dict:
        return {
            "extracted_tables": [['Q1', '$10M'], ['Q2', '$12M']]
        }
