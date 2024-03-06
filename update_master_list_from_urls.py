# 文件名：update_master_list_from_urls.py
import requests

def fetch_list_content(url):
    response = requests.get(url)
    response.raise_for_status()  # 如果请求失败，抛出HTTPError异常
    return response.text

def update_master_list(urls, master_file_path):
    with open(master_file_path, 'w') as master_file:
        for url in urls:
            content = fetch_list_content(url)
            master_file.write(content + "\n\n")

if __name__ == "__main__":
    urls = [
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Claude/Claude.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Loon/Gemini/Gemini.list"
    ]
    master_file_path = "master.list"
    update_master_list(urls, master_file_path)