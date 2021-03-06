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
                list_text += f'ã»?[{commit.id[0:7]}]({commit.url}) {commit.message}\n'
            text = f'âª{recv.repository.name}â« ð  Pushã{recv.pusher.name}ã ?[{len(recv.commits)}]({recv.compare}) ä»¶è¡ãã¾ãã\n{list_text}'
        elif recv.repository.has_issues:
            if recv.action == 'closed':
                if recv.pull_request:
                    if recv.pull_request.merged:
                        is_merge = 'ãMergeããã¾ãã'
                    else:
                        is_merge = 'ãMergeããããéãããã¾ãã'
                    text = f'âª{recv.repository.name}â« ð PullRequestçªå· <{recv.pull_request.number}> {is_merge} \nTitle: ã{recv.pull_request.title}ã\nEvent Author: {recv.sender.login}\n{recv.pull_request.html_url}'
                else:
                    text = f'âª{recv.repository.name}â« ð Issueçªå· <{recv.issue.number}> ãè§£æ±ºãã¾ãã \nTitle: ã{recv.issue.title}ã\nEvent Author: {recv.issue.user.login}\nTimeStamp: {recv.issue.created_at}\n{recv.issue.html_url}'
            elif recv.action == 'opened':
                text = f'âª{recv.repository.name}â« ð¥ Issueçªå· <{recv.issue.number}> ãçºçãã¾ãã\nTitle: ã{recv.issue.title}ã\nEvent Author: {recv.issue.user.login}\nTimeStamp: {recv.issue.created_at}\n{recv.issue.html_url}'
            elif recv.action == 'created' and recv.comment:
                text = f'âª{recv.repository.name}â« ð¬ Issueçªå· <{recv.issue.number}> ã«ã³ã¡ã³ããè¿½å ããã¾ãã\nContent:ã{recv.comment.body}ã\nEvent Author: {recv.issue.user.login}\nTimeStamp: {recv.issue.created_at}\n{recv.issue.html_url}'
            elif recv.action == 'labeled':
                text = f'âª{recv.repository.name}â« ð¨ Issueçªå· <{recv.issue.number}> ã«ã©ãã«ãè¿½å ããã¾ãã\nContent:{[i.name for i in recv.issue.labels]}\nEvent Author: {recv.issue.user.login}\nTimeStamp: {recv.issue.created_at}\n{recv.issue.html_url}'
        asyncio.run(Note(text=text).send())


def run_webhook():
    with socketserver.TCPServer(("", 80), MyHandler) as httpd:
        httpd.serve_forever()


if __name__ == '__main__':
    run_webhook()
