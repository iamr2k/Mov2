from flask import Flask,render_template,url_for,request
import pandas as pd
from sklearn.feature_extraction.text import movieVectorizer
from sklearn.metrics.pairwise import cosine_similarity
df = pd.read_csv('dataset.csv')


originalTitlelist = df.originalTitle.values.tolist()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    
   
    if request.method == 'POST':

        message = request.form.get('message')
        message = message.replace(",",' ')
        print(message)
        movie_vectorizer = movieVectorizer()
        df.content = df.content.str.replace('[','')
        df.content = df.content.str.replace(']','')
        df.content = df.content.str.replace("'",'')

        moviematrix = movie_vectorizer.fit_transform(tuple(df.content.astype(str)))
        question = message
        q_vect = movie_vectorizer.transform([question])
            
        similarity = cosine_similarity(q_vect, moviematrix)
        top_5_simmi = similarity[0].argsort()[-8:][::-1]

        result = []
        result1 = []
        for i in top_5_simmi:
            result.append(df.iloc[i]['originalTitle'])      
            #print("top questions", processed[processed.asin == asindf.iloc[i]['asin'] ].question)
            result1.append(similarity[0, i])
        print(result) 
        message = result[0]
                
        ###### helper functions. Use them when needed #######


        def get_similar_from_originalTitle(originalTitle):
            try :
                a = df[df.originalTitle == originalTitle]["similar"].values[0]
            except :
                a = 'not found'
            return a


        def get_poster_from_index(index):
            try :
                a=df[df.originalTitle == index]["poster"].values[0]
            except :
                a = 'not found'
            return a
        
        def get_url_from_index(index):
            try :
                a=df[df.originalTitle == index]["URL"].values[0]
            except :
                a = 'not found'
            return a
        
        def get_ytb_from_index(index):
            try :
                a=df[df.originalTitle == index]["youtube"].values[0]
            except :
                a = 'not found'
            return a

        def get_year_from_index(index):
            try :
                a=df[df.originalTitle == index]["startYear"].values[0]
            except :
                a = 'not found'
            return a
        
        def get_runtime_from_index(index):
            try :
                a=df[df.originalTitle == index]["runtimeMinutes"].values[0]
            except :
                a = 'not found'
            return a
        def get_gen_from_index(index):
            try :
                a=df[df.originalTitle == index]["genres"].values[0]
            except :
                a = 'not found'
            return a
        
        def get_ar_from_index(index):
            try :
                a=df[df.originalTitle == index]["averageRating"].values[0]
            except :
                a = 'not found'
            return a
        
        def get_nv_from_index(index):
            try :
                a=df[df.originalTitle == index]["numVotes"].values[0]
            except :
                a = 'not found'
            return a
        
        def get_content_from_index(index):
            try :
                a=df[df.originalTitle == index]["content"].values[0]
            except :
                a = 'not found'
            return a




        movie_user_likes = message

        ## Step 6: Get index of this movie from its originalTitle
        movie = get_similar_from_originalTitle(movie_user_likes)

        movie = movie.replace('[','')
        movie = movie.replace(']','')
        movie = movie.replace("'",'')
        #movie0 = movie0.replace(",",'')
        movie0 = [x.strip() for x in movie.split(',')]
       
        movie0 = result[0:8]
        
        movie1 = []
        movie2 = []
        movie3 = []
        movie4 = []
        movie5 = []
        movie6 = []
        movie7 = []
        movie8 = []
        movie9 = []
        
        for element in movie0:
            print(element)            
            movie1.append(get_url_from_index(element))
            movie2.append(get_poster_from_index(element))
            movie3.append(get_ytb_from_index(element))
            movie4.append(get_year_from_index(element))
            movie5.append(get_gen_from_index(element))
            movie6.append(get_ar_from_index(element))
            movie7.append(get_nv_from_index(element))
            movie8.append(get_runtime_from_index(element))
            movie9.append(get_content_from_index(element))

        

    return render_template('result.html',movie0=movie0,movie1=movie1,movie2=movie2,movie3=movie3,movie4=movie4,movie5 = movie5,movie6=movie6,movie7=movie7,movie8 = movie8,movie9 = movie9)




if __name__ == '__main__':
    app.run(debug=True)