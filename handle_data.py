import json
f1 = open('novel.json','r',encoding='utf8')
res1 = f1.read()
#print(res1)
res2 = json.loads(res1)
#print(res2)
with open('novel.txt','a',encoding='utf8') as f2:
    for item in res2:
        title = item['title']
        content = item['content']
        content = content.replace("“","\n“")
        f2.write(title)
        f2.write('\n')
        f2.write(content)
        f2.write('\n')
    f2.close()
f1.close
