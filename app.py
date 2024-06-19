from flask import Flask, render_template, request
from stop_words import get_stop_words
from wordcloud import WordCloud, ImageColorGenerator 
import numpy as np
from PIL import Image
import os
import nltk
import matplotlib.pyplot as plt

app = Flask(__name__)

nltk.data.path.append('./nltk_data/')
nltk.download('stopwords', download_dir='./nltk_data/')

def calculate_frequencies(texto):
    punctuations = '''!()-[];:'"\\,<>./?@#$%^&*_~'''
    uninteresting_words = set(["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", 
                               "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", 
                               "its", "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", 
                               "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", 
                               "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", "all", 
                               "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", 
                               "can", "will", "just"])
    
    cleaned_text = ''.join([char.lower() for char in texto if char not in punctuations])
    filtered_words = [word for word in cleaned_text.split() if word.lower() not in uninteresting_words]

    word_freq = {}
    for word in filtered_words:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1
    
    return word_freq

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_wordcloud', methods=['POST'])
def generate_wordcloud():
    if request.method == 'POST':
        text_file = request.files['text_file']
        image_file = request.files['image_file']
        shape_file = request.files['shape_file']  

        text_file.save(os.path.join(app.root_path, 'static', 'uploaded', text_file.filename))
        image_file.save(os.path.join(app.root_path, 'static', 'uploaded', image_file.filename))
        shape_file.save(os.path.join(app.root_path, 'static', 'uploaded', shape_file.filename))  

        with open(os.path.join(app.root_path, 'static', 'uploaded', text_file.filename), 'r', encoding='utf-8') as f:
            texto = f.read()

        word_freq = calculate_frequencies(texto)

        stop_words = get_stop_words('english')

        shape_img = np.array(Image.open(os.path.join(app.root_path, 'static', 'uploaded', shape_file.filename)))
        mask = np.array(Image.open(os.path.join(app.root_path, 'static', 'uploaded', shape_file.filename)))
        
        img_for_color = np.array(Image.open(os.path.join(app.root_path, 'static', 'uploaded', image_file.filename)))
        image_colors = ImageColorGenerator(img_for_color)
        wc = WordCloud(background_color="white", width=800, height=600, stopwords=stop_words, mask=mask).generate_from_frequencies(word_freq)
        wc.recolor(color_func=image_colors)

        wc_image_path = os.path.join(app.root_path, 'static', 'wordcloud.png')
        wc.to_file(wc_image_path)

        return render_template('result.html', wc_image=wc_image_path)

if __name__ == '__main__':
    app.run(debug=True)
