from PyPDF2 import PdfReader
import docx
from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from flask_cors import CORS  # Import the CORS extension

app = Flask(__name__)
# disable cors
# CORS(app)
CORS(app, resources={r"/upload": {"origins": "http://localhost:8000"}})


def vectorize(Text): return TfidfVectorizer().fit_transform(Text).toarray()
def similarity(doc1, doc2): return cosine_similarity([doc1, doc2])

class FileWrapper:
    def __init__(self, file_name):
        self.name = file_name
        self.text = ""
        self.read()
    def read(self):
        raise NotImplementedError()
class DocxFileWrapper(FileWrapper):
    def read(self):
        doc = docx.Document(self.name)
        for paragraph in doc.paragraphs:
            self.text = self.text + "\n" + paragraph.text
        return self.text
class PDFWrapper(FileWrapper):
    def read(self):
        reader = PdfReader(self.name)
        for page_number in range(len(reader.pages)):
            page = reader.pages[page_number]
            text = page.extract_text()
            self.text = self.text + "\n" + text
        return self.text

def file_factory(file_name):
    if file_name.filename.endswith(".pdf"):
        return PDFWrapper(file_name)
    elif file_name.filename.endswith(".docx"):
        return DocxFileWrapper(file_name)
    else:
        raise NotImplementedError()
def text_to_dictionary(text):
    dictionary = {}
    for word in text.split():
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    return dictionary
def check_plagiarism(first_file_name, second_file_name):
    first = file_factory(first_file_name)
    second = file_factory(second_file_name)

    data1=text_to_dictionary(first.text)
    data2=text_to_dictionary(second.text)
    common = {word: min(data1[word], data2[word]) for word in data1 if word in data2 and len(word) > 4}
    most_frequent = sorted(common.items(), key=lambda x: x[1], reverse=True)[:10]
    print([{word: freq} for word, freq in most_frequent])
    vectors = vectorize([first.text, second.text])
    sim_score = similarity(vectors[0], vectors[1])[0][1]
    return sim_score*100,[{word: freq} for word, freq in most_frequent]


    # data1=text_to_dictionary(first.text)
    # data2=text_to_dictionary(second.text)
    # common = {word: min(data1[word], data2[word]) for word in data1 if word in data2 and len(word) > 4}
    # most_frequent = sorted(common.items(), key=lambda x: x[1], reverse=True)[:10]
    # print([{word: freq} for word, freq in most_frequent])

@app.route('/')
def index():
    return render_template('./index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file_data_1' not in request.files or 'file_data_2' not in request.files:
        return "Missing PDF files", 400

    file_data_1 = request.files['file_data_1']
    file_data_2 = request.files['file_data_2']
    # print(file_data_1.filename)
    # print(file_data_2.filename)
    ret_val = check_plagiarism(file_data_1, file_data_2)
    print(ret_val)
    return jsonify(ret_val)


if __name__ == '__main__':
    app.run(debug=True)

# print(check_plagiarism("1706.03762.pdf", "1706.03762.pdf"))
