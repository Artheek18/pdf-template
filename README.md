# 📄 PDF Notes Generator

A full-stack web application that generates structured PDF lesson notes from a simple CSV file. 
Users upload a `topics.csv` file, and the app dynamically creates a downloadable PDF with a table of contents and lined note pages for each topic.

---

## 🌐 Live Demo

You can try the app live here:

* **Web App (Frontend – Vercel):** [https://pdf-template-woad.vercel.app](https://pdf-template-woad.vercel.app)
* **Backend API (FastAPI – Render):** [https://pdf-template.onrender.com](https://pdf-template.onrender.com)
* **API Docs:** [https://pdf-template.onrender.com/docs](https://pdf-template.onrender.com/docs)

> ⚠️ **Note:** The backend is hosted on Render’s free tier, so the first request may take a few seconds if the server is waking up.

---

## ✨ Features

* **CSV Upload:** Upload a structured file to define your lesson plan.
* **Automatic Generation:** * Professional Table of Contents.
    * One or more lined note pages per topic.
* **Instant Delivery:** Returns the PDF as a direct browser download.
* **Validation:** Server-side validation for CSV structure and data types.
* **Privacy-Focused:** Temporary file handling (no files are stored permanently).
* **Modern UI:** Clean, responsive React interface.

---

## 📁 CSV Format

The uploaded CSV must contain the following columns:

| Column | Description |
| :--- | :--- |
| **Order** | Numerical order of the lesson |
| **Topic** | The title of the lesson/section |
| **Pages** | Number of lined note pages to generate for this topic |

### Example `topics.csv`
csv
Order,Topic,Pages
1,Introduction to AI,3
2,Search Algorithms,5
3,Machine Learning Basics,4
---

# 🛠 Tech Stack
Backend
Language: Python

Framework: FastAPI

PDF Engine: FPDF (1.7.2)

Data Handling: Pandas

Deployment: Hosted on Render

Frontend
Framework: React

Build Tool: Vite

Deployment: Hosted on Vercel

#🧠 Architecture Overview
Interaction: User interacts with the React (Vite) Frontend.

Request: Frontend sends a multipart/form-data (CSV upload) to the FastAPI Backend.

Validation: Backend performs CSV structure and data validation.

Generation: PDF Generation (FPDF) creates the document in memory or temporary storage.

Storage: A temporary PDF file is created and served via the API.

Delivery: The user receives a Direct Download Response.

# 🧑‍💻 Local Development
**Backend**
Bash

cd backend

python -m venv venv

source venv/bin/activate 
# Windows: venv\Scripts\activate

pip install -r requirements.txt

uvicorn app.main:app --reload

**Frontend**
Bash

cd frontend

npm install

npm run dev

# 📈 Future Improvements
Customization: Add page styles such as grid, dotted, or blank pages.

UX: In-browser PDF preview before downloading.

Security: User authentication and private saved templates.

Export: Support for multiple formats (e.g., DOCX).

# 🏁 Summary
This project demonstrates a full-stack approach to file processing, including robust API design, seamless frontend-backend integration, and automated cloud deployment.
