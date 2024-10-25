from flask import Flask,render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def level1():

    return render_template('play.html')  # Return the string 'Hello World!' as a response

@app.route('/play/<number>')          # The "@" decorator associates this route with the function immediately following
def level2():
    return render_template('level2.html')  # Return the string 'Hello World!' as a response








if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

