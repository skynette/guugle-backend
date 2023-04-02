## Guugle Backend
This is the backend for Guugle, a search engine API clone of Google Search. It is built with FastAPI and provides endpoints for searching, as well as indexing pages for searching.

![image](https://user-images.githubusercontent.com/29153968/229352678-4ec37ecf-7cf1-4c8b-b374-e1e8cee2b927.png)
sample request

![image](https://user-images.githubusercontent.com/29153968/229352701-f068e2fe-510c-4a88-a4a0-47904668310e.png)
sample response


### Features
Search engine API

### Installation
To get started, you need to have Python 3.x and pip installed on your machine. Then, follow these steps:

- Clone the repository: `git clone https://github.com/skynette/guugle-backend.git`
- Change to the project directory: `cd guugle-backend`
- Create a virtual environment using: `python3 -m venv env`
- Activate the virtual environment using: `source env/bin/activate`
- Install the required dependencies: `pip install -r requirements.txt`
- Start the server: `uvicorn main:app --reload`

The server should now be running at `http://localhost:5000`.

### Endpoints

### GET /search
This endpoint allows you to search pages. The query string should include the search query

### Contributing
Contributions are always welcome! Feel free to submit issues and pull requests.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Acknowledgments
This project was inspired by Google Search and built with FastAPI.
