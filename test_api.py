from requests import get, post, delete

# print(get('http://localhost:5000/api/news').json())
#
# print(get('http://localhost:5000/api/news/3').json())
# print(get('http://localhost:5000/api/news/999').json())

# print(post('http://localhost:5000/api/news').json())
# print(post('http://localhost:5000/api/news',
#            json={'title': 'Заголовок'}).json())
print(post('http://localhost:5000/api/v2/news',
           json={'title': 'ttt',
                 'content': 'text',
                 'user_id': 1,
                 'is_private': False}).json())

# print(delete('http://localhost:5000/api/news/999').json())
# # новости с id = 999 нет в базе
#
# print(delete('http://localhost:5000/api/news/1').json())
