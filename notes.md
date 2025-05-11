# Python Fast API installation guide

Link : [fastapi](https://fastapi.tiangolo.com/)

[thanks-to-bitfumes](https://youtu.be/7t2alSnE2-I?si=AUsK42UuB3HncRgD)

---

Make sure we have python version greater than 3.6 .

We can either install fastapi globally or in a virtual environment(venv).

python3 -m venv fastapi-example-env

Once created then,

fastapi-example-env\Scripts\activate.bat

---

pip install fastapi

pip install uvicorn

---

### Run the server with the command

uvicorn main:app --reload

---

All the data validation performed by fastapi is taken care of pydantic and also it is suggested to move all the static paths (/blog/unpublished) before the dynamic paths (/blog/{id}) to avoid conflicts

Swagger comes with fast api
http://127.0.0.1:8000/docs

So if we navigate to /docs we can see the Swagger documentation

If we want to run the main.py file inside the blog folder then we have to use the command

uvicorn blog.main:app --reload

---

pip install SQLAlchemy

[InstallationGuide](https://docs.sqlalchemy.org/en/20/intro.html#installation)

Download Tableplus app
