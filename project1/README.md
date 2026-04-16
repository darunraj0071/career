# AI Career Path Recommendation System

A modern Python web application that uses AI to recommend personalized career paths based on user skills, interests, and experience level.

## Features

🎯 **Intelligent Recommendations** - AI-powered engine that matches your profile with the best career paths
🎨 **Dark Theme UI** - Sleek, modern black-themed interface with cyan accents
📊 **Profile Analysis** - Comprehensive user profiling based on multiple factors
🚀 **10+ Career Paths** - Recommendations across various AI and tech careers
📈 **Growth Insights** - View salary ranges, growth potential, and skill requirements

## Supported Career Paths

- Machine Learning Engineer
- Data Scientist
- AI Research Scientist
- Data Engineer
- Full Stack Developer
- Cloud Architect
- AI Product Manager
- Computer Vision Engineer
- Natural Language Processing Engineer
- DevOps Engineer
- Robotics Engineer

## Installation

1. **Clone or download this project**

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open in browser:**
   The app will automatically open at `http://localhost:8501`

## Project Structure

```
project1/
├── app.py                          # Main Streamlit application
├── recommendation_engine.py        # AI recommendation logic
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── .streamlit/
│   └── config.toml                # Streamlit theme configuration
└── assets/
    └── logo.png                   # Application logo (add your own)
```

## How It Works

1. **Input Your Profile:**
   - Enter your name
   - Select up to 5 skills you have
   - Select up to 5 interests
   - Specify your experience level
   - Choose work style preference (Remote/Hybrid/On-site)
   - Set your salary expectations

2. **Get AI Recommendations:**
   - The recommendation engine analyzes your profile
   - Matches it against 10+ career paths
   - Calculates compatibility scores
   - Returns top 5 personalized recommendations

3. **View Detailed Information:**
   - Career descriptions
   - Required skills to develop
   - Average salary ranges
   - Growth potential
   - Related interests

## Customization

### Add Your Logo
Replace the placeholder in `assets/logo.png` with your own logo file (PNG format recommended, 200x200px minimum).

### Customize Careers Database
Edit `recommendation_engine.py` and modify the `_load_careers_database()` method to add or update career information.

### Change Theme Colors
Edit `.streamlit/config.toml`:
- `primaryColor`: Primary accent color
- `backgroundColor`: Main background
- `secondaryBackgroundColor`: Secondary background
- `textColor`: Text color

## Requirements

- Python 3.8+
- Streamlit 1.28.1
- pandas 2.1.1
- numpy 1.24.3
- scikit-learn 1.3.2
- Pillow 10.1.0

## Technologies Used

- **Streamlit**: Interactive web framework
- **Python**: Core programming language
- **scikit-learn**: Machine learning utilities
- **pandas & numpy**: Data processing
- **CSS/HTML**: Custom styling

## Future Enhancements

- [ ] Integration with actual job market data APIs
- [ ] User authentication and profile saving
- [ ] Machine learning model training on real salary data
- [ ] Integration with LinkedIn or job boards
- [ ] Skill roadmap generation
- [ ] Resume analyzer
- [ ] Job market statistics visualization

## License

This project is open source and available under the MIT License.

## Support

For issues or suggestions, please create an issue in the project repository.

---

**Happy career path exploring! 🚀**
