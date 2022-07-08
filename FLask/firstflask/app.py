from flask import Flask, url_for

app = Flask(__name__)

# topics={
#     {'id':1, 'title': 'html', 'body': "html is ..."},
#     {'id':2, 'title': 'css', 'body': "css is ..."},
#     {'id':3, 'title': 'javascript', 'body': "javascript is ..."}
# }

# def template(title, body):
#     f'''
#     <!doctype html>
#     <html>
#         <body>
#             <h1><a href='/'>HOME</h1>
#             <h2>{title}</h2> 
#             <p>{body}</p>
#         </body> 
#     </html>
#     '''

# 초기화면
@app.route('/')
def Index():
	return 'Main Page'

@app.route('/create/', methods=['GET','POST'])
def create():
	return f'''
    <form action="/create/" method="POST">
        <p><input type="text" name="title" placeholder="title"></p>
        <p><textarea type="body" name="body" placeholder="body"></textarea></p>
        <p><input type="submit" value="create"></p>
    </form>
    '''

# 변수 사용
@app.route('/read/<int:read_id>/')
def read(read_id):
    return 'read'
        
# url 구축
with app.test_request_context():
    print(url_for('Index'))
    print(url_for('create'))
    print(url_for('create', next='/'))
    print(url_for('read', read_id=1000))
