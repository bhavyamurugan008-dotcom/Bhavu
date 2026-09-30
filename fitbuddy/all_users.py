
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>FitBuddy Admin</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; }
        h1 { color: #15803d; }
        .user {
            padding: 18px;
            margin: 15px 0;
            background: #f1f5f9;
            border-radius: 10px;
        }
        pre { white-space: pre-wrap; overflow-wrap: anywhere; }
    </style>
</head>
<body>
    <h1>FitBuddy - All Users</h1>

    {% for user in users %}
    <div class="user">
        <h2>{{ user.username }} (ID: {{ user.id }})</h2>
        <p>Age: {{ user.age }}</p>
        <p>Weight: {{ user.weight }} kg</p>
        <p>Goal: {{ user.goal }}</p>
        <p>Intensity: {{ user.intensity }}</p>

        <h3>Original Workout Plan</h3>
        <pre>{{ user.workout_plan }}</pre>

        {% if user.updated_plan %}
        <h3>Updated Workout Plan</h3>
        <pre>{{ user.updated_plan }}</pre>
        {% endif %}
    </div>
    {% else %}
    <p>No users registered yet.</p>
    {% endfor %}

    <a href="/">Back to Home</a>
</body>
</html>