from wtforms_sqlalchemy.orm import model_form
from flask_wtf import FlaskForm
from wtforms import Field, widgets
from models import Tag  # นำเข้า Tag จาก models.py

import models


class TagListField(Field):
    widget = widgets.TextInput()

    def __init__(self, label="", validators=None, remove_duplicates=True, **kwargs):
        super().__init__(label, validators, **kwargs)
        self.remove_duplicates = remove_duplicates
        self.data = []

    def process_formdata(self, valuelist):
        data = []
        if valuelist:
            data = [x.strip() for x in valuelist[0].split(",")]

        if not self.remove_duplicates:
            self.data = data
            return

        self.data = []
        for d in data:
            if d not in self.data:
                self.data.append(d)

    def _value(self):
        if self.data:
            # แปลงข้อมูลใน self.data ให้เป็น string ก่อนที่จะใช้ join
            return ", ".join(str(tag) for tag in self.data)  # แปลงทุกๆ tag ให้เป็น string
        else:
            return ""


    def populate_obj(self, obj, name):
        tag_instances = []
        for tag_name in self.data:
            tag = Tag.query.filter_by(name=tag_name).first()  # ค้นหา tag จากฐานข้อมูล
            if tag:  # ถ้าพบ tag ในฐานข้อมูล
                tag_instances.append(tag)
        setattr(obj, name, tag_instances)  # ตั้งค่าให้กับฟิลด์ในโมเดล



BaseNoteForm = model_form(
    models.Note, 
    base_class=FlaskForm, 
    exclude=["created_date", "updated_date"],
    db_session=models.db.session,
)


class NoteForm(BaseNoteForm):
    tags = TagListField("Tag")
