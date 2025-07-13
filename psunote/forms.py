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
            # ตรวจสอบว่า self.data เป็น Tag object หรือไม่
            return ", ".join(str(tag) if isinstance(tag, str) else tag.name for tag in self.data)
        else:
            return ""


    def populate_obj(self, obj, name):
        tag_instances = []
        for tag_name in self.data:
            # ค้นหา tag จากฐานข้อมูล
            tag = Tag.query.filter_by(name=tag_name).first()

            if not tag:  # ถ้าไม่พบแท็กในฐานข้อมูล
                # สร้างแท็กใหม่เป็น Tag object และเพิ่มเข้าไปในฐานข้อมูล
                tag = Tag(name=tag_name)
                models.db.session.add(tag)
            # เพิ่ม Tag object (หรือชื่อถ้าไม่พบ Tag ในฐานข้อมูล) เข้าไปใน tag_instances
            tag_instances.append(tag)

        # ตั้งค่าให้กับฟิลด์ในโมเดล
        setattr(obj, name, tag_instances)



# BaseNoteForm = model_form(
#     models.Note, 
#     base_class=FlaskForm, 
#     exclude=["created_date", "updated_date"],
#     db_session=models.db.session,
# )
BaseNoteForm = model_form(

    models.Note, base_class=FlaskForm, exclude=["created_date", "updated_date"], db_session=models.db.session

)

class NoteForm(BaseNoteForm):
    tags = TagListField("Tag")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ตรวจสอบว่า obj ถูกกำหนดหรือไม่ก่อนเข้าถึง
        if hasattr(self, 'obj') and self.obj and self.obj.tags:
            self.tags.data = [tag.name for tag in self.obj.tags]  # ให้แท็กที่มีอยู่มาแสดงในฟอร์ม
