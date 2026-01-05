# ATS Analyzer 📄✨

An intelligent **Applicant Tracking System (ATS) Resume Analyzer** powered by Google's Gemini AI and Flask. This tool helps job seekers optimize their resumes by analyzing them against job descriptions and providing actionable insights.

## 🌟 Features

- **AI-Powered Analysis**: Leverages Google Gemini 2.0 Flash model for intelligent resume evaluation
- **PDF Resume Upload**: Supports PDF format for resume parsing
- **Job Description Matching**: Compares your resume against specific job requirements
- **Comprehensive Scoring**: Provides detailed scores across multiple dimensions:
  - Keyword Matching Score
  - Impact Score (action verbs analysis)
  - Readability Score
  - Overall ATS Score (0-100)
- **Missing Keywords Detection**: Identifies important skills and terms missing from your resume
- **Strengths & Weaknesses**: Detailed feedback on what works and what needs improvement
- **Fallback Engine**: Smart local analysis engine when AI is unavailable
- **User-Friendly Interface**: Clean, responsive web interface

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **AI**: Google Gemini 2.0 Flash API
- **PDF Processing**: PyPDF2
- **Frontend**: HTML/CSS with modern UI
- **Environment Management**: python-dotenv

## 📋 Prerequisites

- Python 3.7 or higher
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- pip (Python package manager)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/murali-krishna-palla/ATS_Analyzer.git
   cd ATS_Analyzer
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask PyPDF2 python-dotenv google-genai
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
   
   ⚠️ **Important**: Never commit your `.env` file to version control!

## 💻 Usage

1. **Start the application**
   ```bash
   python main.py
   ```

2. **Open your browser**
   
   Navigate to: `http://localhost:8080`

3. **Analyze your resume**
   - Upload your resume (PDF format)
   - Paste the job description you're targeting
   - Click "Analyze Resume"
   - Review your ATS score and recommendations

## 📊 How It Works

### Analysis Process

1. **PDF Text Extraction**: The tool extracts text from your uploaded resume using PyPDF2
2. **AI Analysis**: Sends your resume and job description to Google Gemini for intelligent analysis
3. **Scoring Algorithm**: Evaluates your resume across three key dimensions:
   - **Keywords (50%)**: Matches technical skills and job-specific terms
   - **Impact (30%)**: Analyzes presence of strong action verbs
   - **Readability (20%)**: Assesses document structure and length
4. **Feedback Generation**: Provides detailed strengths, weaknesses, and missing keywords

### Fallback Mode

If the Gemini API is unavailable, the tool automatically switches to a local analysis engine that:
- Uses regex-based keyword extraction
- Filters out common stop words
- Provides basic scoring and recommendations

## 📁 Project Structure

```
ATS_Analyzer/
├── main.py              # Flask application & core logic
├── templates/
│   └── ATS.html        # Frontend interface
├── uploads/            # Temporary PDF storage
├── .env                # Environment variables (not tracked)
├── .gitignore         # Git ignore rules
├── LICENSE            # Project license
└── README.md          # This file
```

## 🔒 Security

- API keys are stored in `.env` file (excluded from version control)
- Uploaded resumes are processed in memory and not permanently stored
- No personal data is retained after analysis

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Known Issues / Limitations

- Only supports PDF format (Word documents not yet supported)
- AI analysis requires active internet connection
- Best results with English-language resumes

## 🔮 Future Enhancements

- [ ] Support for DOCX format
- [ ] Batch resume processing
- [ ] Historical analysis tracking
- [ ] Resume optimization suggestions
- [ ] Multi-language support
- [ ] Export analysis reports as PDF

## 👨‍💻 Author

**Murali Krishna Palla**
- GitHub: [@murali-krishna-palla](https://github.com/murali-krishna-palla)

## 🙏 Acknowledgments

- Google Gemini AI for powering the intelligent analysis
- Flask community for the excellent web framework
- All contributors and users of this tool

---

⭐ If you find this project helpful, please consider giving it a star on GitHub!