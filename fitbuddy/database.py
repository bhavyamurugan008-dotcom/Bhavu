import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file!")

# client ah global ah define panrom
client = genai.Client(api_key=api_key)

def generate_workout_plan(user_data: dict):
    prompt = f"""
    Create a personalized 7-day workout plan for:
    Age: {user_data.get('age')}, Weight: {user_data.get('weight')}kg, 
    Height: {user_data.get('height')}cm, Goal: {user_data.get('goal')},
    Fitness Level: {user_data.get('fitness_level')}, 
    Days: {user_data.get('workout_days')}
    
    Return in clean HTML format with tables and sections. Make it motivating!
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )
    
    return response.text