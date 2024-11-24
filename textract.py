import boto3
import json

from pdf2image import convert_from_path
from PIL import Image

pdfFilePath = 'files/extrato.pdf'
tiffFilePath = 'files/extrato.tiff'

# Converter PDF para imagens
# pages = convert_from_path(pdfFilePath, dpi=300)

# Salvar como um único TIFF
# pages[0].save(tiffFilePath, save_all=True, append_images=pages[1:])

# Cliente AWS Textract
textract = boto3.client('textract')


# Carregar o documento
with open(pdfFilePath, "rb") as document:
    print(document)
    response = textract.analyze_document(
        Document={'Bytes': document.read()},
        FeatureTypes=["TABLES"]
    )

# Imprimir a resposta para debug
print(json.dumps(response, indent=2))
