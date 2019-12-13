from aip import AipSpeech

APP_ID = '14542628'
API_KEY = 'MYCbeYzTbqG6U5EeQRsYtvSm'
SECRET_KEY = '3oFuFdG0V8EOF6H77qLe1KGT3k0xfI3a'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
result = client.synthesis('空山新雨后，天气晚来秋！', 'zh', 1, {
    'vol': 7,
    'spd': 5,
    'pit': 8,
    'per': 3,

})
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('audio.mp3', 'wb') as f:
        f.write(result)