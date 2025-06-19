# PlagueTale – Plagiarism Checker with Word-Count Graph

A lightweight web app that compares two documents (PDF or DOCX), computes a similarity score via TF-IDF + cosine similarity, and highlights the top overlapping words in an interactive D3.js bar chart.

## 🚀 Features

- **Multi-format support**: Upload and compare PDF and DOCX files.
- **Plagiarism scoring**: Uses TF-IDF vectorization and cosine similarity to compute a percentage match.
- **Word-count analysis**: Extracts and counts common words (length > 4), displays the top 10 overlaps.
- **Interactive visualization**: Renders an interactive bar chart of word frequencies using D3.js.
- **REST API**: Simple Flask backend with a `/upload` endpoint for file comparison.

## 🛠️ Tech Stack

- **Backend**: Python, Flask  
- **Text Extraction**: PyPDF2 (PDF), python-docx (DOCX)  
- **ML**: scikit-learn (`TfidfVectorizer`, `cosine_similarity`)  
- **Frontend**: HTML/CSS, Tailwind, D3.js  
- **Others**: Flask-CORS for cross-origin support

## 📁 Project Structure

.
├── static/
│ └── js/
│ └── d3.js
├── templates/
│ └── index.html
├── main.py # Flask app and plagiarism logic
├── test.py # Standalone text-to-dictionary & demo extractor
├── requirements.txt # Python dependencies
├── README.md # This file
└── .gitignore



## ⚙️ Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone https://github.com/pr0ximaCent/PlagueTale-Plagiarism-Checker-With-specific-word-and-count-by-graph.git
   cd PlagueTale-Plagiarism-Checker-With-specific-word-and-count-by-graph
Create & activate a virtualenv

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the server

bash
Copy
Edit
python main.py
The app will be accessible at http://127.0.0.1:5000.

🚀 Usage
Open the web interface (/) to upload two documents.

Click Convert to Text to trigger /upload.

View:

Similarity percentage printed in the output panel.

Top overlapping words bar chart rendered below via D3.js.

🔧 Endpoints
GET /
Serves the upload form (index.html).

POST /upload
Accepts file_data_1 and file_data_2 (PDF or DOCX), returns JSON

json
Copy
Edit
[
  82.3567,                        // similarity percentage
  [ {"disease": 5}, … {"health":3} ]  // top 10 common words & counts
]
📝 Testing
test.py: Demo script reading test_doc_2.docx, prints paragraphs and builds a word-frequency dict.

bash
Copy
Edit
python test.py
🤝 Contributing
Fork the repo

Create a feature branch: git checkout -b feature/YourFeature

Commit changes & push: git push origin feature/YourFeature

Open a Pull Request

📄 License
This project is MIT-licensed. See LICENSE for details.
