# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yaskour <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/18 17:45:57 by yaskour           #+#    #+#              #
#    Updated: 2022/02/18 19:29:10 by yaskour          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #
import gspread
from flask import Flask ,render_template,request
app = Flask(__name__)

gc = gspread.service_account(filename='flask-profile.json')
sh = gc.open('flask-profile')

shProfile = sh.get_worksheet(0)
shContacts = sh.get_worksheet(1)
@app.route('/',methods=['POST','GET'])
def home():
    if request.method == 'POST':
        shContacts.append_row([request.form['name'],request.form['email'],request.form['message']])
    profile = {
            'about':shProfile.acell('B1').value,
            'interests':shProfile.acell('B2').value,
            'experience':shProfile.acell('B3').value,
            'education':shProfile.acell('B4').value,
        }
    return render_template('index.html',profile=profile)
@app.route('/contact')
def contact():
    return render_template('contact.html')

if ( __name__ == '__main__'):
    app.run(debug=True)
