import os
from docling.document_converter import DocumentConverter

input_folder = "resumes"
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)

converter = DocumentConverter()

for filename in os.listdir(input_folder):
    if filename.endswith((".pdf", ".docx")):
        filepath = os.path.join(input_folder, filename)
        print(f"▶ Processing: {filepath}")

        try:
            result = converter.convert(filepath)
            doc_text = result.document.export_to_text()

            txt_name = os.path.splitext(filename)[0] + ".txt"
            out_path = os.path.join(output_folder, txt_name)

            with open(out_path, "w", encoding="utf-8") as f:
                f.write(doc_text)

            print(f"✅ Saved to {out_path}")

        except Exception as e:
            print(f"❌ Error: {filename}: {e}")
