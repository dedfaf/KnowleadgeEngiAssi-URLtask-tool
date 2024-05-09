import webbrowser
import json
import time
import keyboard
import pyperclip
import urllib.parse
import re
import os

def SaveJson(data):
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def process_url(origin_url):
    url = urllib.parse.urlparse(origin_url)
    decoded_path = urllib.parse.unquote_plus(url.path)
    new_url = f'{url.scheme}://{url.netloc}{decoded_path}'
    return new_url

def process_content(content, entity):
    text = re.sub(r'/[a-zA-Z]+', '', content)
    text = re.sub(r'^\d+-\d+-\d+-\d+\s+', '', text)
    text = re.sub(r'[\s\#]', '', text)
    text = re.sub(r'\[|]nt', '', text)
    text = re.sub(r'\{.*?\}', '', text)

    red_entity = f"\033[31m{entity}\033[0m"
    highlighted_text = re.sub(re.escape(entity), red_entity, text)
    return highlighted_text

def Process():
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    total_task = len(data)
    task_count = 0
    for item in data:
        task_count += 1
        print('正在处理任务:', item['sentence_id'], "总进度:", f'{task_count}/{total_task}')
        print('实体名称:', item['entity'])
        print(process_content(item['content'], item['entity']))
        webbrowser.get('Browser').open('https://baike.baidu.com/search?enc=utf8&pn=0&rn=0&word=' + item['entity'], new=1, autoraise=0)

        last_clip = pyperclip.paste()
        SkipConut = 0

        print("正在监听剪贴板")
        while True:
            if keyboard.is_pressed('right shift'):
                SkipConut += 1
                if SkipConut < 5:
                    print("!RshiftPressed! : 确认None跳过:", f'{SkipConut}/{5}')
                else:
                    print("!RshiftPressed! : 确认None跳过:", f'{SkipConut}/{5}')
                    print("结束监听剪贴板")
                    print("\033[31m跳过该任务\033[0m")
                    break
            else:
                SkipConut = 0
            current_clip = pyperclip.paste()
            if current_clip != last_clip:
                print("检测到新的复制:", current_clip)
                print("URL解析结果:", process_url(current_clip))
                print("是否确认输入？[enter/n]")

                choice = input()
                if choice == '':
                    new_URL = process_url(current_clip)
                    item['url'] = new_URL
                    SaveJson(data)
                    print('写入新URL:', new_URL)
                    print("结束监听剪贴板")
                    break
                else:
                    print("继续监听剪贴板")
                last_clip = current_clip
            time.sleep(0.5)
        
        print("任务完成")


BrowserPath = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
json_file_path = 'annotation-task/你的学号.json'

webbrowser.register('Browser', None, webbrowser.BackgroundBrowser(BrowserPath))

# webbrowser.get('Browser').open('10.0.0.55', new = 0, autoraise = False)

Process()

print("JOB DONE")
