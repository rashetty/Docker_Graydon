# flask web api for company move probability

from flask import Flask, request 

#create the Flask app
app = Flask(__name__) 

#allow both GET and POST requests
@app.route('/', methods=['GET', 'POST']) 
def csvexample():
    import pandas as pd
    import numpy as np
    import pickle

# this block is only entered when the form is submitted
    if request.method == 'POST':  
        features = request.form.get('features').split(",")
        features_formatted = []

        for i in features:
            if i == 'True':
                i_val = True
            elif i == 'False':
                i_val = False
            else:
                i_val = float(i)
            features_formatted.append(i_val)

        df_columns = ["has_name_change",
                      "delta_qty_issued_credit_reports",
                      "delta_score_payment_assessment",
                      "code_legal_form_has_changed",
                      "SBI_has_changed",
                      "company_age",
                      "qty_green_flags",
                      "qty_orange_flags",
                      "qty_red_flags",
                      "A",
                      "AA",
                      "AAA",
                      "B",
                      "BB",
                      "BBB",
                      "C",
                      "CC",
                      "CCC",
                      "D",
                      "NR",
                      "code_legal_form_group_1",
                      "code_legal_form_group_2",
                      "SBI_group_1",
                      "SBI_group_2",
                      "is_discontinued_any",
                      "has_financial_calamity",
                      "mean_qty_issued_credit_reports",
                      "mean_score_payment_assessment",
                      "qty_address_mutations_year",
                      "qty_started_names_year",
                      "qty_stopped_names_year",
                      "qty_board_changes_year",
                      "variance_qty_issued_credit_reports",
                      "variance_score_payment_assessment"]
 
        df = pd.DataFrame(data=[features_formatted], columns=df_columns)

        clf = pickle.load(open("model.sav", 'rb'))
        probability_of_move = clf.predict_proba(df)[:, 1]

        return '''<h1>The probability of moving is {}</h1>'''.format(probability_of_move[0])

    return '''<form method="POST">
                  company features: <input type="list" name="features"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
