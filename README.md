1. python3 -m venv venv
2. source venv/bin/activate
3. touch requirements.txt
3.1. add requirements to file
4. pip install -r requirements.txt
5. Создаем структуру проекта
6. export FLASK_APP=wsgi.py
7. echo ".idea" >> .gitignore
7.1 echo "venv" >> .gitignore
7.2 echo "*__pycache__*" >> .gitignore
8. echo "FLASK_APP=wsgi.py" >> .flaskenv


REST API
1. Client-server
2. Stateless
3. Cache 