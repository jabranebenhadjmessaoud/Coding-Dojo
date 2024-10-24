from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response




@app.route('/dojo')
def home():
    return "Dojo!"

@app.route('/say/<name>')
def saying(name):
    typeof=type(name)
    print (typeof)
    if typeof==str:
        return "Hi "+ name +"!"
    else :
        return " The given name is not a string"

@app.route('/repeat/<number>/<name>')
def repeating(number, name):
    return (name +" ") *(int (number))


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
