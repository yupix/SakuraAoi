import asyncio
import http.server

from mi import Note
from sakuraAoi.models.git_webhook import GitWebHook
import socketserver
import json


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)

        self.end_headers()
        content_len = int(self.headers.get('content-length'))
        requestBody = self.rfile.read(content_len).decode('UTF-8')
        json_data = json.loads(requestBody)
        recv = GitWebHook(**json_data)
        if recv.pusher:
            list_text = ''
            for commit in recv.commits:
                list_text += f'・?[{commit.id[0:7]}]({commit.url}) {commit.message}\n'
            text = f'≪{recv.repository.name}≫ 🌠 Pushを{recv.pusher.name}が ?[{len(recv.commits)}]({recv.compare}) 件行いました\n{list_text}'
        elif recv.repository.has_issues:
            if recv.action == 'closed':
                if recv.pull_request:
                    if recv.pull_request.merged:
                        is_merge = 'がMergeされました'
                    else:
                        is_merge = 'がMergeされず、閉じられました'
                    text = f'≪{recv.repository.name}≫ 🌈 PullRequest番号 <{recv.pull_request.number}> {is_merge} \nTitle: 「{recv.pull_request.title}」\nEvent Author: {recv.sender.login}\n{recv.pull_request.html_url}'
                else:
                    text = f'≪{recv.repository.name}≫ 🌈 Issue番号 <{recv.issue.number}> が解決しました \nTitle: 「{recv.issue.title}」\nEvent Author: {recv.issue.user.login}\nTimeStamp: {recv.issue.created_at}\n{recv.issue.html_url}'
            elif recv.action == 'opened':
                text = f'≪{recv.repository.name}≫ 🔥 Issue番号 <{recv.issue.number}> が発生しました\nTitle: 「{recv.issue.title}」\nEvent Author: {recv.issue.user.login}\nTimeStamp: {recv.issue.created_at}\n{recv.issue.html_url}'
            elif recv.action == 'created' and recv.comment:
                text = f'≪{recv.repository.name}≫ 💬 Issue番号 <{recv.issue.number}> にコメントが追加されました\nContent:「{recv.comment.body}」\nEvent Author: {recv.issue.user.login}\nTimeStamp: {recv.issue.created_at}\n{recv.issue.html_url}'
            elif recv.action == 'labeled':
                text = f'≪{recv.repository.name}≫ 🎨 Issue番号 <{recv.issue.number}> にラベルが追加されました\nContent:{[i.name for i in recv.issue.labels]}\nEvent Author: {recv.issue.user.login}\nTimeStamp: {recv.issue.created_at}\n{recv.issue.html_url}'
        asyncio.run(Note(text=text).send())


def run_webhook():
    with socketserver.TCPServer(("", 80), MyHandler) as httpd:
        httpd.serve_forever()


if __name__ == '__main__':
    run_webhook()
