import json
from typing import Dict, List, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class CareerRecommendationEngine:
    """AI-powered career recommendation engine"""
    
    def __init__(self):
        self.careers_database = self._load_careers_database()
        self.vectorizer = TfidfVectorizer(lowercase=True, stop_words='english')
    
    def _load_careers_database(self) -> Dict:
        """Load the careers database with detailed information"""
        return {
            "Machine Learning Engineer": {
                "description": "Build and deploy machine learning models for real-world applications",
                "required_skills": ["Python", "ML Algorithms", "TensorFlow", "Statistics"],
                "growth_potential": "High (20% annually)",
                "avg_salary": "$120K-$180K",
                "related_interests": ["AI", "Data", "Technology"],
                "match_factors": {
                    "skills": ["Python", "statistics", "data analysis", "mathematics"],
                    "interests": ["AI", "machine learning", "data", "technology"]
                }
            },
            "Data Scientist": {
                "description": "Extract insights from data to drive business decisions",
                "required_skills": ["Python", "SQL", "Statistics", "Data Visualization"],
                "growth_potential": "High (18% annually)",
                "avg_salary": "$110K-$160K",
                "related_interests": ["Data", "Analytics", "Business"],
                "match_factors": {
                    "skills": ["Python", "SQL", "statistics", "data analysis"],
                    "interests": ["data", "analytics", "business", "insights"]
                }
            },
            "AI Research Scientist": {
                "description": "Develop cutting-edge AI algorithms and advance the field",
                "required_skills": ["Python", "Research", "Deep Learning", "Mathematics"],
                "growth_potential": "Very High (25% annually)",
                "avg_salary": "$130K-$200K",
                "related_interests": ["AI", "Research", "Innovation"],
                "match_factors": {
                    "skills": ["Python", "mathematics", "research", "deep learning"],
                    "interests": ["AI", "research", "innovation", "technology"]
                }
            },
            "Data Engineer": {
                "description": "Design and maintain data pipelines and infrastructure",
                "required_skills": ["Python", "SQL", "Spark", "Cloud Platforms"],
                "growth_potential": "High (19% annually)",
                "avg_salary": "$115K-$170K",
                "related_interests": ["Data", "Infrastructure", "Technology"],
                "match_factors": {
                    "skills": ["Python", "SQL", "database", "infrastructure"],
                    "interests": ["data", "technology", "systems"]
                }
            },
            "Full Stack Developer": {
                "description": "Build complete web applications from frontend to backend",
                "required_skills": ["JavaScript", "Python", "Databases", "API Design"],
                "growth_potential": "Medium-High (12% annually)",
                "avg_salary": "$90K-$140K",
                "related_interests": ["Web Development", "Technology", "Design"],
                "match_factors": {
                    "skills": ["JavaScript", "Python", "web development", "databases"],
                    "interests": ["web development", "technology", "design"]
                }
            },
            "Cloud Architect": {
                "description": "Design scalable cloud infrastructure and solutions",
                "required_skills": ["Cloud Platforms", "Architecture", "DevOps", "Security"],
                "growth_potential": "High (21% annually)",
                "avg_salary": "$130K-$190K",
                "related_interests": ["Infrastructure", "Security", "Technology"],
                "match_factors": {
                    "skills": ["cloud", "architecture", "devops", "infrastructure"],
                    "interests": ["infrastructure", "security", "technology"]
                }
            },
            "AI Product Manager": {
                "description": "Lead AI product development and strategy",
                "required_skills": ["Product Strategy", "Communication", "AI Understanding", "Analytics"],
                "growth_potential": "Medium-High (15% annually)",
                "avg_salary": "$100K-$150K",
                "related_interests": ["AI", "Product", "Business"],
                "match_factors": {
                    "skills": ["communication", "strategy", "analytics", "leadership"],
                    "interests": ["AI", "product", "business", "innovation"]
                }
            },
            "Computer Vision Engineer": {
                "description": "Develop computer vision systems for image and video analysis",
                "required_skills": ["Python", "OpenCV", "Deep Learning", "Image Processing"],
                "growth_potential": "Very High (22% annually)",
                "avg_salary": "$125K-$185K",
                "related_interests": ["AI", "Computer Vision", "Technology"],
                "match_factors": {
                    "skills": ["Python", "deep learning", "image processing", "mathematics"],
                    "interests": ["AI", "computer vision", "technology"]
                }
            },
            "Natural Language Processing Engineer": {
                "description": "Build NLP systems for text understanding and generation",
                "required_skills": ["Python", "NLP Libraries", "Deep Learning", "Linguistics"],
                "growth_potential": "Very High (23% annually)",
                "avg_salary": "$120K-$190K",
                "related_interests": ["AI", "NLP", "Language"],
                "match_factors": {
                    "skills": ["Python", "deep learning", "NLP", "linguistics"],
                    "interests": ["AI", "NLP", "language", "technology"]
                }
            },
            "DevOps Engineer": {
                "description": "Manage infrastructure, deployment, and operations",
                "required_skills": ["Linux", "Docker", "Kubernetes", "Scripting"],
                "growth_potential": "High (17% annually)",
                "avg_salary": "$105K-$160K",
                "related_interests": ["Infrastructure", "Automation", "Technology"],
                "match_factors": {
                    "skills": ["Linux", "docker", "automation", "infrastructure"],
                    "interests": ["infrastructure", "automation", "technology"]
                }
            },
            "Robotics Engineer": {
                "description": "Design and develop robotic systems and automation",
                "required_skills": ["C++", "ROS", "Control Systems", "Mechanical Design"],
                "growth_potential": "High (20% annually)",
                "avg_salary": "$110K-$170K",
                "related_interests": ["Robotics", "Automation", "Technology"],
                "match_factors": {
                    "skills": ["C++", "robotics", "control systems", "automation"],
                    "interests": ["robotics", "automation", "technology"]
                }
            }
        }
    
    def get_available_skills(self) -> List[str]:
        """Get list of available skills"""
        return [
            "Python", "JavaScript", "SQL", "Java", "C++",
            "Machine Learning", "Deep Learning", "Statistics", "Data Analysis",
            "Web Development", "Mobile Development", "Cloud Computing", "DevOps",
            "API Design", "Database Design", "System Design", "Leadership",
            "Communication", "Problem Solving", "Creativity", "Project Management"
        ]
    
    def get_available_interests(self) -> List[str]:
        """Get list of available interests"""
        return [
            "AI", "Machine Learning", "Data Science", "Web Development",
            "Mobile Apps", "Cloud Computing", "Infrastructure", "Security",
            "Computer Vision", "NLP", "Robotics", "Automation",
            "Product Management", "Startups", "Research", "Gaming",
            "Finance", "Healthcare", "Education", "E-commerce"
        ]
    
    def _calculate_match_score(self, user_skills: List[str], user_interests: List[str], career: Dict) -> float:
        """Calculate match score between user profile and career"""
        score = 0
        weight = 0
        
        # Match skills
        career_match_skills = career['match_factors']['skills']
        for skill in user_skills:
            for match_skill in career_match_skills:
                if skill.lower() in match_skill.lower() or match_skill.lower() in skill.lower():
                    score += 30
                    weight += 1
        
        # Match interests
        career_match_interests = career['match_factors']['interests']
        for interest in user_interests:
            for match_interest in career_match_interests:
                if interest.lower() in match_interest.lower() or match_interest.lower() in interest.lower():
                    score += 35
                    weight += 1
        
        # Base score
        if weight > 0:
            return min(100, 40 + (score / weight))
        return 40
    
    def get_recommendations(self, skills: List[str], interests: List[str], 
                           experience: str, work_style: str, salary_range: str) -> Dict:
        """Get career recommendations based on user profile"""
        recommendations = {}
        
        for career_name, career_info in self.careers_database.items():
            match_score = self._calculate_match_score(skills, interests, career_info)
            
            # Experience adjustment
            exp_multiplier = self._get_experience_multiplier(experience, career_name)
            match_score *= exp_multiplier
            
            recommendations[career_name] = {
                **career_info,
                "match_score": max(0, min(100, match_score))
            }
        
        # Sort by match score
        sorted_recommendations = dict(sorted(
            recommendations.items(),
            key=lambda x: x[1]['match_score'],
            reverse=True
        ))
        
        # Return top 5
        return {k: v for k, v in list(sorted_recommendations.items())[:5]}
    
    def _get_experience_multiplier(self, experience: str, career: str) -> float:
        """Get experience level multiplier"""
        multipliers = {
            "0-1": {"entry": 1.1, "mid": 0.8, "senior": 0.5},
            "1-3": {"entry": 1.0, "mid": 1.1, "senior": 0.7},
            "3-5": {"entry": 0.9, "mid": 1.15, "senior": 0.9},
            "5-10": {"entry": 0.8, "mid": 1.0, "senior": 1.15},
            "10+": {"entry": 0.7, "mid": 0.9, "senior": 1.2}
        }
        
        # Classify career level
        if "Research" in career or "Architect" in career:
            level = "senior"
        elif "Engineer" in career or "Scientist" in career:
            level = "mid"
        else:
            level = "entry"
        
        return multipliers.get(experience, {}).get(level, 1.0)
