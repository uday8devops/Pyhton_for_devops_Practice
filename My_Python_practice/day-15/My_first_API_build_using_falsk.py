from flask import Flask

# Creating a flask Application instance
app = Flask(__name__)


# Write a Decorator for API URL PATH, 
# So, that it will be verified before executing the hello function
@app.route("/uday")

# write hello-world function definition
def hello():
    return "Hello World...!!!!!"

# To run with built-in development server provided by falsk

# To run with default port=5000
# app.run('0.0.0.0')

# To run with custom port
app.run('0.0.0.0', port=1122) 