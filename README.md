<div align="center">

# 🧭 Career Compass

**An AI-powered guidance app for skill evaluation, profile matching, and personalized career insights.**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Supabase](https://img.shields.io/badge/Supabase-Database-3ECF8E?style=flat-square&logo=supabase&logoColor=white)](https://supabase.com/)

---

</div>

### 💡 Overview

**Career Compass** was built to solve a simple problem: bridging the gap between a candidate's current skills and their target career path. Using interactive inputs and database-driven matching, it evaluates competencies and visualizes skill gaps in real time.

---

### ✨ Highlights

* **Interactive Assessment** — Step-by-step workflow for skills and job targets.
* **Real-time Analytics** — Visual match scoring and breakdown.
* **Secure Architecture** — Zero hardcoded credentials; fully managed via Streamlit Secrets and `.env` setups.

---

### 🛠️ Tech Stack

* **Frontend & UX:** Streamlit
* **Backend & Database:** Supabase
* **Data Processing:** Pandas, NumPy
* **Environment Management:** Python-dotenv

---

### 🔐 Security & Configuration

Secrets are kept strictly out of version control. For local deployment, create a `.env` file in the root directory:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key```

🚀 Quick Start
Clone the project:
Bash
```git clone [https://github.com/haykuhii2000-blip/career-compass-mini-project.git](https://github.com/haykuhii2000-blip/career-compass-mini-project.git)
cd career-compass-mini-project```

Install requirements:
Bash
```pip install -r requirements.txt```

Launch the app:
Bash
```streamlit run app.py```
Crafted with care by Haykuhi Ananyan
