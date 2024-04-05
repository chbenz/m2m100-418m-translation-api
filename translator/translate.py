from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

model = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
tokenizer = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")

def translate_zh_en(text: str):
    tokenizer.src_lang = "zh"
    encoded_zh = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(**encoded_zh, forced_bos_token_id=tokenizer.get_lang_id("en"))
    text_decoded = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return text_decoded[0]

def translate_en_zh(text: str):
    tokenizer.src_lang = "en"
    encoded_en = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(**encoded_en, forced_bos_token_id=tokenizer.get_lang_id("zh"))
    text_decoded = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
    return text_decoded[0]