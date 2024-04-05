from flask import Flask, request

from translator.translate import translate_en_zh as en_zh, translate_zh_en as zh_en

app = Flask(__name__)

@app.route('/')
def index():
  return 'Index Page'
  
@app.route('/translation/en-zh', methods=['GET'])
def translation_en_zh():
  text_for_translation = request.args.get('text')
  return en_zh(text_for_translation)

@app.route('/translation/zh-en', methods=['GET'])
def translation_zh_en():
  text_for_translation = request.args.get('text')
  return zh_en(text_for_translation)

if __name__ == '__main__':
    app.run()