#!/usr/bin/env python
# coding: utf-8

# In[30]:


from flask import Flask


# In[31]:


app = Flask(__name__)


# In[32]:


from flask import render_template,request

from keras.models import load_model
@app.route("/", methods = ["GET","POST"])

def index():
    if request.method =="POST":
        NPTL = request.form.get("NPTL")
        
        TLTA = request.form.get("TLTA")
        
        WCTA = request.form.get("WCTA")
        print(NPTL,TLTA,WCTA)
        model = load_model("BKR")
        pred = model.predict([[float(NPTL),float(TLTA),float(WCTA)]])
        print(pred)
        pred = pred[0][0]
        s = "The predicted bankrucptcy score is :" + str(pred)
        return(render_template("index.html",results=s))
    else:
        return(render_template("index.html",results="2"))
    


# In[33]:


if __name__ =="__main__":
    app.run()


# In[ ]:




