import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import json
from recommendation_engine import CareerRecommendationEngine

# Page configuration
st.set_page_config(
    page_title="AI Career Path Recommender",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {}

# Load logo
logo_path = Path("assets/logo.png")
if logo_path.exists():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(str(logo_path), width=150, use_column_width=False)

st.markdown("<h1 style='text-align: center; color: #00D9FF;'>🚀 AI Career Path Recommender</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #888;'>Discover Your Perfect Career Path with AI</p>", unsafe_allow_html=True)
st.divider()

# Initialize recommendation engine
engine = CareerRecommendationEngine()

# Sidebar for user inputs
with st.sidebar:
    st.markdown("### 📋 Tell Us About Yourself")
    
    # User inputs
    name = st.text_input("Your Name", placeholder="Enter your name")
    
    st.markdown("**Skills & Interests**")
    skills = st.multiselect(
        "Select your top skills",
        options=engine.get_available_skills(),
        max_selections=5,
        help="Choose up to 5 skills you're proficient in"
    )
    
    interests = st.multiselect(
        "Select your interests",
        options=engine.get_available_interests(),
        max_selections=5,
        help="Choose up to 5 areas that interest you"
    )
    
    st.markdown("**Experience Level**")
    experience = st.select_slider(
        "Years of experience",
        options=["0-1", "1-3", "3-5", "5-10", "10+"],
        value="0-1"
    )
    
    st.markdown("**Preferences**")
    work_style = st.selectbox(
        "Preferred work style",
        options=["Remote", "Hybrid", "On-site"],
        help="Choose your preferred working arrangement"
    )
    
    salary_range = st.select_slider(
        "Expected salary range (USD)",
        options=["$30K-$50K", "$50K-$80K", "$80K-$120K", "$120K-$150K", "$150K+"],
        value="$50K-$80K"
    )
    
    st.divider()
    
    # Recommendation button
    if st.button("🎯 Get Recommendations", use_container_width=True, type="primary"):
        if not skills or not interests:
            st.warning("Please select at least one skill and one interest!")
        else:
            # Store user profile
            st.session_state.user_profile = {
                "name": name,
                "skills": skills,
                "interests": interests,
                "experience": experience,
                "work_style": work_style,
                "salary_range": salary_range
            }

# Main content area
if st.session_state.user_profile:
    user_data = st.session_state.user_profile
    
    st.markdown(f"### Hello, {user_data['name'] or 'Career Seeker'}! 👋")
    
    # Get recommendations
    recommendations = engine.get_recommendations(
        skills=user_data['skills'],
        interests=user_data['interests'],
        experience=user_data['experience'],
        work_style=user_data['work_style'],
        salary_range=user_data['salary_range']
    )
    
    # Display recommendations
    st.markdown("### 🎯 Top Career Paths for You")
    
    for idx, (career, details) in enumerate(recommendations.items(), 1):
        st.markdown(f"---")
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.markdown(f"**#{idx} {career}**")
            st.markdown(f"Match Score: {details['match_score']:.0f}%")
            st.markdown(f"**Description:** {details['description']}")
            
            # Skills required
            st.markdown("**Skills to Develop:**")
            skill_cols = st.columns(len(details['required_skills']))
            for col, skill in zip(skill_cols, details['required_skills']):
                with col:
                    st.info(skill)
            
            # Growth potential
            st.markdown(f"**Growth Potential:** {details['growth_potential']}")
            st.markdown(f"**Average Salary:** {details['avg_salary']}")
            
        with col2:
            st.metric("Growth Potential", f"{details['growth_potential'][:10]}")
    
    # Additional insights
    st.divider()
    st.markdown("### 📊 Your Profile Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Skills Selected", len(user_data['skills']))
    with col2:
        st.metric("Interests", len(user_data['interests']))
    with col3:
        st.metric("Experience Level", user_data['experience'])
    with col4:
        st.metric("Work Style", user_data['work_style'])
    
    # Recommendations
    st.divider()
    st.markdown("### 💡 Next Steps")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("📚 **Learn New Skills**\nTake online courses to bridge skill gaps")
    
    with col2:
        st.info("🤝 **Network**\nConnect with professionals in your target fields")
    
    with col3:
        st.info("🏆 **Build Portfolio**\nCreate projects showcasing your abilities")
    
    # Reset button
    if st.button("🔄 Start Over", use_container_width=True):
        st.session_state.user_profile = {}
        st.rerun()

else:
    st.info("👈 Fill out the form on the left to get started with personalized career recommendations!")
    
    # Show some general information
    st.markdown("### About This Tool")
    st.markdown("""
    This AI-powered career recommender helps you discover career paths based on:
    - **Your Skills**: Select technical and soft skills you already have
    - **Your Interests**: Choose areas that excite you professionally
    - **Your Experience**: Let us know your career stage
    - **Your Preferences**: Set your work style and salary expectations
    
    Get personalized recommendations that match your profile!
    """)
