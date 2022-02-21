import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder


def ipc_prediction(text):
    #Data Analysis

    train_data=pd.read_excel("trainv1.xlsx")

    train_section = train_data["Section"].to_numpy()
    

    train_offence = train_data["Offence"].to_numpy()
    

    Label_Encoder = LabelEncoder()
    train_ipc_labels_encoder = Label_Encoder.fit_transform(train_section.reshape(-1, 1))
    


    # Create tokenization and modelling pipeline
    model_0 = Pipeline([
                        ("tfidf", TfidfVectorizer()), # convert words to numbers using tfidf
                        ("clf", MultinomialNB()) # model the text
    ])

    # Fit the pipeline to the training data
    model_0.fit(train_offence, train_ipc_labels_encoder)
    
    text = np.array([text])
   

    ipc_preds = model_0.predict(text)
    ipc_preds = Label_Encoder.inverse_transform(ipc_preds)

    return ipc_preds


def data_retrival(code):

  data={"ipc:354":["354. Assault or criminal force to woman with intent to outrage her modesty.",
                   "Whoever assaults or uses criminal force to any woman, intending to outrage or knowing it to be likely that he will thereby outrage her modesty, shall be punished with impris­onment of either description for a term which may extend to two years, or with fine, or with both."],
        "ipc:498":["498. Enticing or taking away or detaining with criminal intent a married woman",
                   "Whoever takes or entices away any woman who is and whom he knows or has reason to believe to be the wife of any other man, from that man, or from any person having the care of her on behalf of that man, with intent that she may have illicit intercourse with any person, or conceals or detains with that intent any such woman, shall be punished with imprisonment of either description for a term which may extend to two years, or with fine, or with both."]}
  
  detail = data[code][0]
  punishment = data[code][1]

  return detail,punishment




def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele  
    
    # return string  
    return str1 


