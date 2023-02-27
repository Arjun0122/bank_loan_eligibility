
from flask import *
from flask import request, render_template
import json
import pickle
import pandas as pd

app = Flask(__name__)

model=pickle.load(open('model.pk1','rb'))

def predict(value):
  
   sample=pd.DataFrame({'Current Loan Amount':[value["Current Loan Amount"]],'Term':[value["Term"]],'Credit Score':[value["Credit Score"]], 'Annual Income':[value['Annual Income']], 'Years in current job':[value['Years in current job']]
                    , 'Home Ownership':[value['Home Ownership']], 'Purpose':[value['Purpose']], 'Monthly Debt':[value['Monthly Debt']],'Years of Credit History':[value['Years of Credit History']], 
                     'Number of Open Accounts':[value['Number of Open Accounts']]
                    , 'Number of Credit Problems':[value['Number of Credit Problems']], 'Current Credit Balance':[value['Current Credit Balance']], 'Maximum Open Credit':[value['Maximum Open Credit']], 'Bankruptcies':[value['Bankruptcies']],
                     'Tax Liens':[value['Tax Liens']] })
   a=model.predict(sample)
   if a[0] == 0.0 :
        return "You are not eligible for loan"
   else:
       return "You are eligible"

   


@app.route("/", methods=["GET", "POST"])


def home():
    if request.method == "POST":
        data=request.form.to_dict()
        json_data_dump=json.dumps(data)
        json_data=json.loads(json_data_dump)
        print(json_data)
        output = predict(json_data)
        print(output)
        if output:
              return render_template("home.html",index=output)
        
    return render_template("home.html")
            
    

if __name__ == "__main__":
    app.debug= True
    app.run('0.0.0.0',port=5000)