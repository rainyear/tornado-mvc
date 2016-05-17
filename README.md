Tornado x MVC
---

### Structure

```
.
├── LICENSE
├── README.md
├── app.py
├── config
│   └── __init__.py
├── controller
│   ├── HomeHandler.py
│   └── __init__.py
├── model
│   └── __init__.py
├── requirements.txt
├── static
│   ├── css
│   ├── images
│   └── js
└── view
    └── 404.html
```

### Usage

```
git clone https://github.com/rainyear/tornado-mvc.git
cd tornado-mvc/
python3 -m venv venv3
source venv3/bin/activate
pip install -r requirements.txt

python app.py --env=dev
```
