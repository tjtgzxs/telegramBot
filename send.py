import telegram
import requests
def get_url():
    contents = requests.get('https://random.dog/woof.json').json()
    url = contents['url']
    return url
def main():
    bot=telegram.Bot(token="5134521680:AAHdEBWW_41Kkl6oj1UFRRKpbXFQYJXBbA8")
    textMSg="i1dadd313"
    bot.send_document(chat_id="-624460494",document="http://techslides.com/demos/sample-videos/small.mp4")
if __name__ == '__main__':
    main()
