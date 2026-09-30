def generate_diet_plan(age, weight, height, goal, veg):
    return f"""
    <h2>💪 Fit Buddy - Diet Plan</h2>
    <p><b>Profile:</b> {age} yrs, {weight}kg, {height}cm | Goal: {goal} | Type: {veg}</p>
    <hr>
    <p><b>🌅 Morning 7 AM:</b> Warm water + 5 almonds</p>
    <p><b>🍳 Breakfast 8:30 AM:</b> Oats + Banana / Idly + Sambar</p>
    <p><b>☀️ Lunch 1 PM:</b> Brown Rice + {veg} curry + Curd</p>
    <p><b>🍎 Snack 4:30 PM:</b> Green tea + Fruits</p>
    <p><b>🌙 Dinner 8 PM:</b> 2 Chapati + Veg curry + Salad</p>
    <p><b>🥛 Before Sleep:</b> 1 glass milk</p>
    <br><p>✅ Daily 3L water kudikanum da!</p>
    """

def generate_workout_plan(age, weight, height, goal, level):
    return f"""
    <h2>🔥 Fit Buddy - Workout Plan</h2>
    <p><b>Profile:</b> {age} yrs, {weight}kg, {height}cm | Goal: {goal} | Level: {level}</p>
    <hr>
    <p><b>Monday - Chest:</b> Pushups 3x15, Bench Press 3x10</p>
    <p><b>Tuesday - Back:</b> Pullups 3x8, Bent Row 3x12</p>
    <p><b>Wednesday - Legs:</b> Squats 3x15, Lunges 3x12</p>
    <p><b>Thursday - Arms:</b> Bicep Curl 3x12, Triceps Dip 3x12</p>
    <p><b>Friday - Shoulder + Cardio:</b> Shoulder Press 3x10, Running 20 min</p>
    <p><b>Saturday - Full Body HIIT</b></p>
    <p><b>Sunday - Full Rest da!</b></p>
    <br><p>✅ Dhinam 30 min workout pothum da!</p>
    """