from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import os
from app.gemini_generator import generate_diet_plan, generate_workout_plan

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html><body style="font-family:Arial; padding:20px;">
    <h1>Fit Buddy 💪</h1>
    <h2>Diet Plan</h2>
    <form action="/generate-diet" method="post">
      Age: <input name="age" value="22"><br><br>
      Weight: <input name="weight" value="70"><br><br>
      Height: <input name="height" value="170"><br><br>
      Goal: <input name="goal" value="weight loss"><br><br>
      Veg: <input name="veg" value="veg"><br><br>
      <button type="submit">Generate Diet</button>
    </form>
    <h2>Workout Plan</h2>
    <form action="/generate-workout" method="post">
      Age: <input name="age" value="22"><br><br>
      Weight: <input name="weight" value="70"><br><br>
      Height: <input name="height" value="170"><br><br>
      Goal: <input name="goal" value="muscle gain"><br><br>
      Level: <input name="level" value="beginner"><br><br>
      <button type="submit">Generate Workout</button>
    </form>
    </body></html>
    """

@app.post("/generate-diet", response_class=HTMLResponse)
async def gen_diet(age: int = Form(22), weight: float = Form(70), height: float = Form(170), goal: str = Form("weight loss"), veg: str = Form("veg")):
    plan = generate_diet_plan(age, weight, height, goal, veg)
    return f"<html><body style='font-family:Arial; padding:20px;'><h1>Diet Plan</h1><pre>{plan}</pre><br><a href='/'>Back</a></body></html>"

@app.post("/generate-workout", response_class=HTMLResponse)
async def gen_workout(age: int = Form(22), weight: float = Form(70), height: float = Form(170), goal: str = Form("muscle gain"), level: str = Form("beginner")):
    plan = generate_workout_plan(age, weight, height, goal, level)
    return f"<html><body style='font-family:Arial; padding:20px;'><h1>Workout Plan</h1><pre>{plan}</pre><br><a href='/'>Back</a></body></html>"