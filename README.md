﻿# 🚀 CareerCraft: ATS Resume Tracker App

![Banner](images/banner.png) <!-- Optional: add a banner image if available -->

**CareerCraft** is a smart, AI-integrated Streamlit web application that analyzes resumes against job descriptions using OpenRouter's DeepSeek model. The platform offers job seekers personalized feedback, keyword alignment, and ATS readiness—all in a clean, interactive UI.

🔗 **Live Demo**: [Click here to try it](https://careercraft-ats-resume-tracker.streamlit.app/)

---

### 📽️ Demo Video
👇🎥 **CareerCraft - ATS Resume Tracker in Action**.<br>
Check out the [project walkthrough video here](https://www.awesomescreenshot.com/video/40983217?key=b2313d15dc25897bcde292f4442dd9d9) 

---

## 🧠 Key Features

- 📄 **Resume Parser**: Upload your PDF resume and extract meaningful content.
- 📝 **JD Analysis**: Paste job descriptions for real-time matching.
- 🤖 **AI Feedback**: Integrates with `deepseek-r1-0528:free` via OpenRouter API to provide intelligent resume insights.
- 📊 **ATS Compatibility**: Evaluates keyword relevance and structure.
- 💬 **Interactive FAQ**: Clarifies how the system works for beginners and professionals.
- 🖼️ **Beautiful UI**: Clean and modern layout using Streamlit columns and visual aids.

---

## 🛠️ Tech Stack

| Technology        | Purpose                        |
|-------------------|--------------------------------|
| Python            | Core backend logic             |
| Streamlit         | UI and frontend                |
| OpenRouter (OpenAI SDK) | LLM API integration           |
| PIL (Pillow)      | Image rendering                |
| PDFMiner / PyMuPDF (if used) | Resume text extraction   |

---

## 📁 Folder Structure

```bash
CareerCraft/
├── app.py                 # Main Streamlit app
├── requirements.txt       # Dependencies
├── .streamlit/
│   └── secrets.toml       # Secure API keys (not in repo)
├── images/
│   ├── upload.png.png
│   ├── output.png
│   ├── images.png
│   └── banner.png
└── README.md              # You're here!
````

---

## 🔐 Secrets Management

Using `st.secrets` in `.streamlit/secrets.toml` to securely store your OpenRouter API key:

```toml
OPENROUTER_API_KEY = "your_openrouter_api_key_here"
```

Access it in code:

```python
api_key = st.secrets["OPENROUTER_API_KEY"]
```

---

## 💻 How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Saket22-CS/CareerCraft-ATS.git
cd CareerCraft-ATS

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create a .streamlit/secrets.toml file
mkdir .streamlit
echo 'OPENROUTER_API_KEY = "your-key-here"' > .streamlit/secrets.toml

# 4. Run the app
streamlit run app.py
```

---

## 🌐 Deployment

* **Platform**: Streamlit Community Cloud
* **URL**: [https://saket22-cs-careercraft-ats-resume-tracker-app-1ae4mk.streamlit.app/](https://saket22-cs-careercraft-ats-resume-tracker-app-1ae4mk.streamlit.app/)
* API Integration via OpenRouter using `deepseek-r1-0528:free` model.

---

## 📸 Screenshots

| UI Section     | Preview                     |
| -------------- | --------------------------- |
| Resume Upload  | ![upload](images/upload.png) |
| Output Display | ![result](images/output.png) |
| FAQ Section    | ![FAQ](images/FAQ.png  )    |

---

## 💡 Future Improvements

* 🔍 Add advanced keyword density visualizations.
* 📤 Allow export of feedback as PDF.
* 🧾 History/logs for users' previous analyses.
* 🌍 Multilingual support for global applications.

---

## 🙌 Acknowledgments

* [OpenRouter](https://openrouter.ai) for free API access.
* [Streamlit](https://streamlit.io) for the amazing open-source framework.
* Inspired by real-world HR screening tools and ATS logic.

---

## 📬 Contact

**Saket Chaudhary**
📧 [saketrishu64821@gmail.com](mailto:saketrishu64821@gmail.com)
🔗 [LinkedIn](https://linkedin.com/in/saket-chaudhary22)
💻 [GitHub](https://github.com/Saket22-CS)

---

## 📜 License

MIT License. Feel free to use and modify for educational or personal purposes.
