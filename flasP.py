from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods = ["GET", "POST"])
def search_books():
    api_key = "bb8ffc956a6f4204adccefef8f160195"
   
    query = request.form.get("query") if request.method == "POST" else None
    
    url = f" https://api.bigbookapi.com/search-books?api-key={api_key}&query={query}"
    response = requests.get(url)
    data = response.json()

    books_data = [book[0] for book in data.get("books", [])]

    return render_template('book.html', books_data= books_data, query=query)

if __name__ == '__main__':
    app.run(debug=True)