# 📄 CV-Ranking Pipeline

Pipeline này thực hiện việc:
1. Trích xuất văn bản từ file PDF/DOCX sử dụng **Docling**
2. Phân tích cú pháp văn bản bằng **ANTLR4**
3. Đánh giá nội dung văn bản bằng **GPT-4 (LLM)**
4. (Tùy chọn) Rerank theo bố cục thị giác bằng mô hình CV

---

## 🗂️ Cấu trúc thư mục

cv_ranking_pipeline/ ├── resumes/ # Thư mục chứa các CV gốc (.pdf, .docx) ├── outputs/ # Thư mục lưu file .txt sau khi convert ├── grammars/ # Chứa file grammar ANTLR (.g4) │ └── cv_scan.g4 ├── parse/ # Chứa các file lexer/parser/visitor do ANTLR sinh ra │ └── visitor.py # File visitor viết tay để xử lý cây cú pháp ├── process_docling.py # Trích xuất văn bản từ file gốc ├── parse_with_antlr.py # Duyệt file văn bản bằng ANTLR ├── llm_ranker.py # Đánh giá nội dung bằng GPT-4 ├── final_pipeline.py # Chạy toàn bộ pipeline └── README.md # Hướng dẫn này

yaml
Copy
Edit

---

## ✅ Cài đặt môi trường

```bash
pip install docling openai antlr4-python3-runtime
🛠️ Compile ANTLR cho Python
Tải ANTLR tại: https://www.antlr.org/download.html

Giả sử bạn đã tải antlr4-4.9.2-complete.jar và đặt tại C:/antlr4-4.9.2-complete.jar

Biên dịch file grammar cv_scan.g4:

bash
Copy
Edit
java -jar C:/antlr4-4.9.2-complete.jar -Dlanguage=Python3 -visitor -o parse grammars/cv_scan.g4
✅ Cờ -visitor sẽ tự động sinh file cv_scanVisitor.py.

▶️ Chạy pipeline
Chạy từng bước:

bash
Copy
Edit
python process_docling.py        # Bước 1: Trích văn bản từ PDF/DOCX
python parse_with_antlr.py       # Bước 2: Dùng ANTLR để phân tích văn bản
python llm_ranker.py             # Bước 3: Chấm điểm bằng GPT-4
Hoặc chạy tất cả bằng 1 lệnh:

bash
Copy
Edit
python final_pipeline.py