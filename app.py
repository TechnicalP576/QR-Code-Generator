from flask import Flask, render_template, request
import qrcode
import os

#name of the app/website
app = Flask(__name__)

#The first route = telling python to go to the menu (HTML)
@app.route('/')
def index():
    return render_template('index.html')

#generating the qr code then returning back to html doc
@app.route('/generate', methods=['POST'])
def generate():
    user_url = request.form.get('url')  
    img = qrcode.make(user_url) #this makes the user send the url for the qr code to be created
    file_name = "qr_code.png"
    img.save(os.path.join('QR Code Generator', 'Static', 'images', file_name)) #saving the qr code image file in the hard drive of the system
    return render_template('index.html', qr_image=file_name)

#starting command for the qr code runner
if __name__ == "__main__":
    app.run(debug=False)