try:
    import sys
    from flask import Flask, render_template, request, redirect, flash
    import csv
    import json
    import numpy as np
    import pandas as pd
    from app_code.additional_functions_for_server import allowed_image_size, allowed_file, save_file, make_prediction
    from flask_pymongo import PyMongo
    import pymongo
except ValueError:
    print("Modules loading failed in " + sys.argv[0])


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/ECG_Datasets"
app.config['MAX_FILE_SIZE'] = 1 * 1024 * 1024
app.config['ALLOWED_FILE'] = ['csv']
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
mongo = PyMongo(app)


@app.route('/')
def start_page():
    return render_template('/index.html')


@app.route('/about')
def about_page():
    return render_template('/about.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        if request.files:
            if not allowed_image_size(request.cookies.get('filesize'), app.config['MAX_FILE_SIZE']):
                print('Prekročená maximálna veľkosť súboru!')
                flash('Prekročená maximálna veľkosť súboru! (MAX 100 KB)')
                return redirect(request.url)

            file = request.files["csv_file"]

            if not allowed_file(file.filename, app.config['ALLOWED_FILE']):
                print('Nepodporovaný typ súboru!')
                flash('Nepodporovaný typ súboru!')
                return redirect(request.url)

            else:
                reader = pd.read_csv(file)
                number_columns = len(reader.columns)

                if number_columns not in [1, 2]:
                    print('Neplatný .csv súbor!')
                    flash('Neplatný .csv súbor!')
                    return redirect(request.url)

                is_prediction_made, err, data, result, bad_signal = make_prediction(reader, number_columns)
                if not is_prediction_made:
                    print('Nepodarilo sa analyzovať súbor! ' + str(err))
                    flash('Nepodarilo sa analyzovať súbor! ' + 'Chyba: ' + str(err))
                    return redirect(request.url)

                is_file_saved = save_file(reader, mongo)
                if not is_file_saved:
                    print('Súbor sa nepodarilo uložiť!')
                    flash('Súbor sa nepodarilo uložiť!')
                    return redirect(request.url)

                return render_template('/predict.html', values=data, output=result, bad=bad_signal)

    return render_template('/index.html')


if __name__ == '__main__':
    app.run(debug=False, port=8000, threaded=False)
