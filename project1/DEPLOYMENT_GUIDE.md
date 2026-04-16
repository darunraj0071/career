# Streamlit Cloud Deployment Guide

## Step-by-Step Instructions to Deploy Your AI Career Recommender

### Prerequisites
- GitHub account (create at https://github.com if you don't have one)
- Streamlit account (create at https://share.streamlit.io)

---

## Step 1: Prepare Your Project (✅ Already Done)

Your project structure is ready:
```
project1/
├── app.py                      # Main application
├── recommendation_engine.py    # AI recommendation logic
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore file
├── README.md                   # Documentation
├── generate_logo.py            # Logo generator
├── .streamlit/
│   └── config.toml            # Theme configuration
└── assets/
    └── logo.png               # AI Career logo
```

---

## Step 2: Create a GitHub Repository

1. **Go to GitHub** → https://github.com/new
2. **Create new repository** with name: `ai-career-recommender`
3. **Add description:** "AI-powered Career Path Recommendation System"
4. **Make it Public** (required for free Streamlit Cloud)
5. **Click "Create repository"**

---

## Step 3: Upload Your Project to GitHub

### Option A: Using GitHub Web Interface (Easiest - No Git Required)

1. **Open your new repository** on GitHub
2. **Click "Add file" → "Upload files"**
3. **Drag and drop** all project files from:
   ```
   c:\Users\darun\Downloads\projects\project1\
   ```
4. **Add commit message:** "Initial commit: AI Career Path Recommendation System"
5. **Click "Commit changes"**

### Option B: Using Git Command Line (If Git is Installed)

```bash
cd c:\Users\darun\Downloads\projects\project1
git init
git add .
git commit -m "Initial commit: AI Career Path Recommendation System"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ai-career-recommender.git
git push -u origin main
```

---

## Step 4: Deploy to Streamlit Cloud

1. **Go to** https://share.streamlit.io
2. **Click "New app"**
3. **Fill in the deployment form:**
   - **GitHub repository:** YOUR_USERNAME/ai-career-recommender
   - **Branch:** main
   - **Main file path:** app.py
4. **Click "Deploy!"**

**Your app will be live at:**
```
https://ai-career-recommender.streamlit.app
```

---

## Step 5: Monitor Your Deployment

After clicking Deploy:
- ✅ Streamlit will build your app
- ✅ Dependencies will be installed from requirements.txt
- ✅ Your app will be accessible online
- ✅ You can share the URL with anyone

---

## Troubleshooting

### "requirements.txt not found"
- ✅ We have this file in the project

### "Module not found" errors
- Ensure all imports in app.py match requirements.txt:
  - streamlit
  - pandas
  - numpy
  - scikit-learn
  - Pillow

### App crashes on deploy
- Check Streamlit Cloud logs for error details
- Ensure app.py runs locally without errors

---

## What Happens After Deployment

✅ **Your app is live!**
- Share the URL: `https://ai-career-recommender.streamlit.app`
- Anyone can access it from any device
- No installation needed
- Runs in the cloud 24/7

---

## Next Steps

1. **Upload to GitHub** (Step 2-3)
2. **Deploy to Streamlit Cloud** (Step 4)
3. **Share your URL** with friends/colleagues
4. **Monitor analytics** in Streamlit Cloud dashboard

---

**Need help?**
- Streamlit Cloud Docs: https://docs.streamlit.io/streamlit-cloud
- GitHub Help: https://docs.github.com
- Contact support at both platforms if you encounter issues

🚀 **Happy deploying!**
