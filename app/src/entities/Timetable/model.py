from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Uuid, Time
from sqlalchemy.orm import relationship

from src.entities.Plan.model import Discipline
from src.entities.Teachers.model import Teacher
from src.entities.Groups.model import Group


class Subject(Base):
    __tablename__ = 'subjects'

    id = Column('id', Integer, primary_key=True)
    discipline_id = Column('discipline_id', String, ForeignKey(Discipline.name))
    teacher_id = Column('teacher_id', Integer, ForeignKey(Teacher.id))
    default_cabinet = Column('default_cabinet', Integer)

    teacher = relationship(Teacher, back_populates='subjects', lazy='selectin')
    class_timetable = relationship('ClassesTimetable', back_populates='subject', lazy='selectin')

class StandardClassSchedule(Base):
    __tablename__ = 'standard_class_schedule'

    lesson_number = Column('lesson_number', Integer, primary_key=True)
    time_start = Column('time_start', Time)
    time_end = Column('time_end', Time)


class ReplacementClasses(Base):
    __tablename__ = 'replacement_classes'

    id = Column('id', Integer, primary_key=True)
    new_subject = Column('new_subject', Integer, ForeignKey(Subject.id))
    new_cabinet = Column('new_cabinet', Integer)
    subject = relationship(Subject, lazy='selectin')

class ClassesTimetable(Base):
    __tablename__ = 'classes_timetable'

    id = Column('id', Integer, primary_key=True)
    subject_id = Column('subject_id', Integer, ForeignKey(Subject.id))
    lesson_number = Column('lesson_number', Integer, ForeignKey(StandardClassSchedule.lesson_number))
    cabinet = Column('cabinet', Integer)
    group_id = Column('group_id', String, ForeignKey(Group.id))
    week_day = Column('week_day', String)

    group = relationship(Group, back_populates='classes_timetable', lazy='selectin')
    subject = relationship(Subject, back_populates='class_timetable', lazy='selectin')


class CurrentClassSchedule(Base):
    __tablename__ = 'current_class_schedule'

    id = Column('id', Integer, primary_key=True)
    replacement_class_id = Column('replacement_class', Integer, ForeignKey(ReplacementClasses.id))
    default_class_id = Column('default_class', Integer, ForeignKey(ClassesTimetable.id))
    date_of = Column('date_of', Date, nullable=False)

    default_class = relationship(ClassesTimetable, lazy='selectin')
    replacement_class = relationship(ReplacementClasses, lazy='selectin')


class CompletedLesson(Base):
    __tablename__ = 'completed_lessons'

    lesson_id = Column('lesson_id', Integer, ForeignKey(CurrentClassSchedule.id), primary_key=True)
    lesson_topic = Column('lesson_topic', String)
    homework_text = Column('homework_text', String)

    schedule_lesson = relationship('CurrentClassSchedule', lazy='selectin')

