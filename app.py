from json import dumps
from flask import Flask, request

from translator.translate import translate_en_zh as en_zh, translate_zh_en as zh_en

app = Flask(__name__)

@app.route('/')
def index():
  	return 'Index Page'
  
@app.route('/translation/en-zh', methods=['GET'])
def translation_en_zh_api():
	text_for_translation = request.args.get('text')
	try:
		return dumps({
			'translation': en_zh(text_for_translation)
		}, ensure_ascii=False)
	except:
		return dumps({'error': 'Error occurred during translation'})

@app.route('/translation/zh-en', methods=['GET'])
def translation_zh_en_api():
	text_for_translation = request.args.get('text')
	try:
		return dumps({
			'translation': zh_en(text_for_translation)
		}, ensure_ascii=False)
	except:
		return dumps({'error': 'Error occurred during translation'})

if __name__ == '__main__':
    app.run()