
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>FitBuddy - AI Fitness Planner</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #101827;
            color: white;
            margin: 0;
            padding: 30px 15px;
        }
        .container {
            max-width: 480px;
            margin: 30px auto;
            padding: 28px;
            background: #1e293b;
            border-radius: 16px;
        }
        h1 { color: #4ade80; text-align: center; }
        label { display: block; margin-top: 15px; }
        input, select, button {
            box-sizing: border-box;
            width: 100%;
            padding: 12px;
            margin-top: 7px;
            border-radius: 8px;
            border: 1px solid #475569;
        }
        button {
            background: #22c55e;
            color: #102018;
            font-weight: bold;
            cursor: pointer;
            margin-top: 22px;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>FitBuddy AI</h1>
    <p>Create your personalized 7-day fitness plan.</p>

    <form action="/generate-workout" method="post">
        <label>Name</label>
        <input type="text" name="username" required maxlength="100">

        <label>Age</label>
        <input type="number" name="age" min="13" max="100" required>

        <label>Weight (kg)</label>
        <input type="number" name="weight" min="20" max="350" required>

        <label>Fitness Goal</label>
        <select name="goal" required>
            <option value="Weight loss">Weight loss</option>
            <option value="Muscle gain">Muscle gain</option>
            <option value="General fitness">General fitness</option>
            <option value="Flexibility">Flexibility</option>
        </select>

        <label>Workout Intensity</label>
        <select name="intensity" required>
            <option value="Low">Low</option>
            <option value="Medium">Medium</option>
            <option value="High">High</option>
        </select>

        <button type="submit">Generate My Plan</button>
    </form>
</div>
</body>
</html>