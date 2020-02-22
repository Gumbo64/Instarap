import pyautogui
import time
import collections
import requests
import pytesseract
a = 'samuel morgan'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
messages = collections.deque([a, a, a, a, a], 5)

def makelink(messages):
    link = 'http://deepbeat.org/deepbeat.fcgi?l=en&r=true&nn=true&k=&q='
    for forma in messages:
        forma = forma.replace(' ', r'%20')
        forma = forma.replace("'", r'%27')
        forma = forma + '&q='
        link = link + forma
    link = link[:-3:]
    return link

        

def makelist(link):
    listanswers =[]
    json = requests.get(link).text
    answers = json
    while answers.find('"line"') != -1:
        textpos = answers.find('"line"')
        answers = answers[textpos+9::]
        endtextpos = answers.find('"')
        textpos = answers.find('"line"')
        itemtext = answers[:endtextpos:]
        scorepos = answers.find('"score"')+9
        endscorepos = answers.find(',', scorepos+1, -1)
        itemscore = answers[scorepos:endscorepos:]
        listanswers.append([itemtext, float(itemscore)])
    return listanswers

time.sleep(5)
while True:
    screenshot = pyautogui.screenshot(region=(90, 740, 460,185))
    newestmsg = pytesseract.image_to_string(screenshot)
    newestmsg.replace('this_might_be_my_usernamo', '')
    newestmsg.replace('hipstawhale_', '')
    newestmsg.replace('_tiahoare', '')
    newestmsg.replace(r'\n', ' ')
    newestmsg.replace('|', 'I')
    if newestmsg != messages[-1] and newestmsg != '' and newestmsg.find('Typing...') ==-1 and newestmsg.find('yping...'):
        messages.append(newestmsg)
        print(newestmsg)
        link = makelink(messages)
        listanswers = makelist(link)
        best = listanswers[0]
        #for entry in listanswers:
        #    if entry[1] > best[1]:
        #        best = entry
        besttext = best[0]
        pyautogui.click(400,968)
        pyautogui.typewrite(besttext)
        pyautogui.click(1824,968)
        pyautogui.click(400,968)
        pyautogui.moveTo(500,500)
        pyautogui.scroll(-10)
        print(messages)
    pyautogui.moveTo(500,500)
    pyautogui.scroll(-1000)