Guugle Backend
This is the backend for Guugle, a search engine API clone of Google Search. It is built with FastAPI and provides endpoints for searching, as well as indexing pages for searching.

Features
Search engine API
Page indexing API
Full-text search
Auto-suggestion
Pagination
Installation
To get started, you need to have Python 3.x and pip installed on your machine. Then, follow these steps:

Clone the repository: git clone https://github.com/skynette/guugle-backend.git
Change to the project directory: cd guugle-backend
Install the required dependencies: pip install -r requirements.txt
Start the server: uvicorn main:app --reload
The server should now be running at http://localhost:8000.

Endpoints
POST /index
This endpoint allows you to index a webpage for searching. The request body should include the URL of the page you want to index.

GET /search
This endpoint allows you to search the indexed pages. The query string should include the search terms, as well as the pagination parameters.

GET /suggest
This endpoint allows you to get auto-suggestions for a given search query.

Contributing
Contributions are always welcome! Feel free to submit issues and pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
This project was inspired by Google Search and built with FastAPI.