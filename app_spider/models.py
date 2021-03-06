import time
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import VARCHAR, INTEGER, TEXT
db = SQLAlchemy()

class company_info(db.Model):
    __tablename__ = "company_info"

    id = db.Column("id", INTEGER, primary_key=True, nullable=False, autoincrement=True)
    web_id = db.Column("web_id", VARCHAR(length=100))
    name = db.Column("name", VARCHAR(length=255))
    boss = db.Column("boss", VARCHAR(length=255))
    category = db.Column("category", VARCHAR(length=255))
    level = db.Column("level", VARCHAR(length=255))
    people_number = db.Column("people_number", VARCHAR(length=255))
    location = db.Column("location", VARCHAR(length=255))
    description = db.Column("description", TEXT)
    web_url = db.Column("web_url", VARCHAR(length=255))
    company_url = db.Column("company_url", VARCHAR(length=255))
    rate = db.Column("rate", VARCHAR(length=100))
    from_web = db.Column("from_web", VARCHAR(length=255))
    create_time = db.Column("create_time", INTEGER)
    status = db.Column("status", INTEGER)
    uid = db.Column("uid", INTEGER)
    create_day = db.Column("create_day", INTEGER)

    def __init__(self, dic):
        self.web_id = dic["web_id"]
        self.name=dic["name"]
        self.boss=dic["boss"]
        self.category=dic["category"]
        self.level=dic["level"]
        self.people_number=dic["people_number"]
        self.location=dic["location"]
        self.description=dic["description"]
        self.web_url=dic["web_url"]
        self.company_url=dic["company_url"]
        self.rate=dic["rate"]
        self.from_web=dic["from_web"]
        self.status=dic["status"]
        self.create_time = int(time.time())
        self.uid = dic["uid"]
        day_str = time.strftime("%Y-%m-%d",time.localtime(self.create_time))
        self.create_day = int(time.mktime(time.strptime(day_str,"%Y-%m-%d")))

    def get_key_list():
        return ["web_id", "name", "boss", "category", "level", "people_number",\
                "location", "description", "web_url", "company_url", "rate",\
                "from_web", "status", "uid"]


class job_info(db.Model):
    __tablename__ = "job_info"

    id = db.Column("id", INTEGER, primary_key=True, nullable=False, autoincrement=True)
    web_id = db.Column("web_id", VARCHAR(length=100))
    company_id = db.Column("company_id", INTEGER)
    name = db.Column("name", VARCHAR(length=255))
    salary = db.Column("salary", VARCHAR(length=255))
    job_year = db.Column("job_year", VARCHAR(length=255))
    education = db.Column("education", VARCHAR(length=255))
    employee_type = db.Column("type", VARCHAR(length=100))
    web_url = db.Column("web_url", VARCHAR(length=255))
    create_time = db.Column("create_time", INTEGER)
    status = db.Column("status", INTEGER)
    from_web = db.Column("from_web", VARCHAR(length=255))
    uid = db.Column("uid", INTEGER)
    create_day = db.Column("create_day", INTEGER)
    location = db.Column("location", VARCHAR(length=255))




    def __init__(self, dic):
        self.web_id=dic["web_id"]
        self.company_id=dic["company_id"]
        self.name=dic["name"]
        self.salary=dic["salary"]
        self.job_year=dic["job_year"]
        self.education=dic["education"]
        self.employee_type=dic["employee_type"]
        self.web_url=dic["web_url"]
        self.status=dic["status"]
        self.create_time = int(time.time())
        self.from_web=dic["from_web"]
        self.uid = dic["uid"]
        day_str = time.strftime("%Y-%m-%d",time.localtime(self.create_time))
        self.create_day = int(time.mktime(time.strptime(day_str,"%Y-%m-%d")))
        self.location=dic["location"]


    def get_key_list():
        return ["web_id", "company_id", "name", "salary", "job_year", "education",\
                "employee_type", "web_url", "status", "from_web", "uid", "location"]

class spider_user(db.Model):
    __tablename__ = "spider_user"

    uid = db.Column("uid", INTEGER, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column("name", VARCHAR(length=255))
    token = db.Column("token", VARCHAR(length=255))
    create_time = db.Column("create_time", INTEGER)
    status = db.Column("status", INTEGER)
    password = db.Column("password", VARCHAR(length=255), nullable=False)
    level = db.Column("level", VARCHAR(length=50), nullable=False)


    def __init__(self, dic):
        self.name = dic["name"]
        self.token = dic["token"]
        self.create_time = int(time.time())
        self.status = 1
        self.password = dic["password"]
        self.level = dic["level"]

class url_table(db.Model):
    __tablename__ = "url_table"

    id = db.Column("id", INTEGER, primary_key=True, nullable=False, autoincrement=True)
    url = db.Column("url", VARCHAR(length=255))
    from_web = db.Column("from_web", VARCHAR(length=255))
    status = db.Column("status", INTEGER)
    classify = db.Column("classify", VARCHAR(length=45))
    uid = db.Column("uid", INTEGER)
    create_time = db.Column("create_time", INTEGER)

    def __init__(self, dic):
        url = dic["url"]
        from_web = dic["from_web"]
        status = 0
        classify = dic["classify"]
        uid = dic["uid"]
        create_time = int(time.time())

class company_info_ex(db.Model):
    __tablename__ = "company_info_ex"
    id = db.Column("id", INTEGER, primary_key=True, nullable=False, autoincrement=True)
    company_info_id = db.Column("company_info_id", INTEGER)
    meta_key = db.Column("meta_key", VARCHAR(length=255))
    meta_value = db.Column("meta_value", TEXT)

    def __init__(self, company_info_id, meta_key, meta_value):
        self.company_info_id = company_info_id
        self.meta_key = meta_key
        self.meta_value = meta_value


class job_info_ex(db.Model):
    __tablename__ = "job_info_ex"
    id = db.Column("id", INTEGER, primary_key=True, nullable=False, autoincrement=True)
    job_info_id = db.Column("job_info_id", INTEGER)
    meta_key = db.Column("meta_key", VARCHAR(length=255))
    meta_value = db.Column("meta_value", TEXT)
    def __init__(self, job_info_id, meta_key, meta_value):
        self.job_info_id = job_info_id
        self.meta_key = meta_key
        self.meta_value = meta_value
