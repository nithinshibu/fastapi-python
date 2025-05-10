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
