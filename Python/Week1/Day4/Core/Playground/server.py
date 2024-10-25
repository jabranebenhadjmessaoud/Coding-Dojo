from flask import Flask,render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def level1():

    return render_template('play.html')  # Return the string 'Hello World!' as a response

@app.route('/play/<int:number>')          # The "@" decorator associates this route with the function immediately following
def level2(number):
    return render_template('level2.html',number=number)  # Return the string 'Hello World!' as a response

@app.route('/play/<int:number>/<thecol>')          # The "@" decorator associates this route with the function immediately following
def level3(number,thecol):
    return render_template('level3.html',number=number,thecol=thecol)  # Return the string 'Hello World!' as a response









if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

