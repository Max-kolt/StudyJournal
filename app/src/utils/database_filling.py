import datetime

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncConnection

from config import ADMIN_MANAGER_USERNAME, ADMIN_MANAGER_PASSWORD
from src.entities.Teachers.schema import TeacherSchema
from datetime import time
from . import password_generator
from src.entities.Auth.schema import bcrypt_context
from uuid import uuid4

weekdays = {
    0: 'Понедельник',
    1: "Вторник",
    2: "Среда",
    3: "Четверг",
    4: "Пятница",
    5: "Суббота",
    6: "Воскресенье"
}

async def database_filling(con: AsyncConnection):
    await con.execute(text(
        f"insert into specializations (name, qualification) values" +
        f"( 'Информационные системы и программирование', 'Администратор баз данных'),"
        f"( 'Информационные системы и программирование', 'Программист')," 
        f"( 'Сетевое и системное администрирование', null);"
    ))
    await con.execute(text(
        f"insert into groups (id, specialization, course) values" +
        f"('404', 1, 4)," +
        f"('405', 2, 4)," +
        f"('402', 3, 4)," +
        f"('314', 1, 3)," +
        f"('312', 3, 3)," +
        f"('225', 2, 2);"
    ))
    await con.execute(text(
        f"insert into standard_class_schedule (lesson_number, time_start, time_end) values " +
        f"(1,'{time(hour=9)}', '{time(hour=9, minute=45)}')," +
        f"(2,'{time(hour=9, minute=50)}', '{time(hour=10, minute=35)}')," +
        f"(3,'{time(hour=11, minute=5)}', '{time(hour=11, minute=50)}')," +
        f"(4,'{time(hour=11, minute=55)}', '{time(hour=12, minute=40)}')," +
        f"(5,'{time(hour=13, minute=10)}', '{time(hour=13, minute=55)}')," +
        f"(6,'{time(hour=14)}', '{time(hour=14, minute=45)}');"
    ))

    await con.execute(text(
        f"insert into educational_cycle (name, curriculum_index) values" +
        f"('Разработка, администрирование и защита баз данных', 'ПМ.11')," +
        f"('Разработка модулей программного обеспечения для компьютерных систем', 'ПМ.01'),"
        f"('Соадминистрирование баз данных и серверов', 'ПМ.07');"
    ))
    await con.execute(text(
        f"insert into disciplines (name, curriculum_index, course_of_study_max) values" 
        f"('Управление и автоматизация баз данных', 'МДК.07.01', 4)," 
        f"('Сертификация информационных систем', 'МДК.07.02', 4),"
        f"('Разработка программных модулей', 'МДК.01.01', 3),"
        f"('Разработка мобильных приложений', 'МДК.01.03', 3),"
        f"('Технология разработки и защиты баз данных', 'МДК.11.01', 4);"
    ))
    await con.execute(text(
        f"insert into cycle_desciplines(education_cycle, discipline, course_of_study, academic_hours) values"
        f"(1, 'Технология разработки и защиты баз данных', 4, 370),"
        f"(3, 'Сертификация информационных систем', 3, 148),"
        f"(3, 'Управление и автоматизация баз данных', 3, 204),"
        f"(2, 'Разработка мобильных приложений', 2, 42),"
        f"(2, 'Разработка программных модулей', 2, 108),"
        f"(3, 'Управление и автоматизация баз данных', 4, 98);"
    ))
    await con.execute(text(
        f"insert into educational_cycle_specializations(specialization, ed_cycle) values"
        f"(1, 1),"
        f"(1, 3),"
        f"(2, 2),"
        f"(2, 3),"
        f"(3, 2);"
    ))

    await con.execute(text(
        f"insert into users (id, lname, fname, mail, with_account) values"
        f"('{uuid4()}', 'Романовская', 'Наталья', 'teacher@mail.ru', true),"
        f"('{uuid4()}', 'Парфенов', 'Артемий', 'teacherman@mail.ru', true),"
        f"('{uuid4()}', 'Иванова', 'Валерия', 'teachergirl@mail.ru', true),"
        f"('{uuid4()}', 'Колосов', 'Максим', 'kolosov@mail.ru', true),"
        f"('{uuid4()}', 'Крестьянов', 'Валерий', 'kres_val@mail.ru', true),"
        f"('{uuid4()}', 'Некрасова', 'Вероника', 'nek_ver@mail.ru', true),"
        f"('{uuid4()}', 'Прекрасная', 'Малина', 'valina@mail.ru', true),"
        f"('{uuid4()}', 'Иванов', 'Владимир', 'vladcher@mail.ru', true),"
        f"('{uuid4()}', 'Петрова', 'Марина', 'petrova@mail.ru', true),"
        f"('{uuid4()}', 'Салихова', 'Софья', 'ss@mail.ru', true),"
        f"('{uuid4()}', 'Кольцов', 'Максим', 'km@mail.ru', true),"
        f"('{uuid4()}', 'Терентьева', 'Наталья', 'tn@mail.ru', true),"
        f"('{uuid4()}', 'Иванова', 'Дарья', 'ivda@mail.ru', true),"
        f"('{uuid4()}', 'Всеволодовна', 'Романовская', 'vsero@mail.ru', true),"
        f"('{uuid4()}', 'Родова', 'Александра', 'roal@mail.ru', true);"
    ))

    await con.execute(text(
        f"insert into teachers (user_id, specialization, education, category)"
        f"select id, ROW_NUMBER() OVER (ORDER BY created_at), 'ВУЗ Информационных Технологий', 'Высшая' from users where (lower(mail) like 'teacher%');"
    ))

    await con.execute(text(
        f"insert into students (user_id, group_id, course)"
        f"select id, '404', 4 from users where (lower(mail) not like 'teacher%');"
    ))

    await con.execute(text(
        f"insert into subjects (discipline_id, teacher_id, default_cabinet) values"
        f"('Управление и автоматизация баз данных', 1, 402),"
        f"('Сертификация информационных систем', 3, 411),"
        f"('Разработка программных модулей', 2, 212),"
        f"('Разработка мобильных приложений', 2, 212),"
        f"('Технология разработки и защиты баз данных', 1, 402);"
    ))

    await con.execute(text(
        f"insert into classes_timetable (subject_id, lesson_number, group_id, week_day) values"
        f"(1, 1, '404', 'Понедельник'),"
        f"(1, 2, '404', 'Понедельник'),"
        f"(4, 3, '404', 'Понедельник'),"
        f"(4, 4, '404', 'Понедельник'),"
        
        f"(1, 1, '404', 'Вторник'),"
        f"(1, 2, '404', 'Вторник'),"
        f"(5, 3, '404', 'Вторник'),"
        f"(5, 4, '404', 'Вторник'),"
        f"(4, 5, '404', 'Вторник'),"
        f"(4, 6, '404', 'Вторник'),"
        
        f"(4, 3, '404', 'Среда'),"
        f"(4, 4, '404', 'Среда'),"
        f"(5, 5, '404', 'Среда'),"
        f"(5, 6, '404', 'Среда'),"
        
        f"(1, 5, '404', 'Четверг'),"
        f"(1, 6, '404', 'Четверг'),"
        
        f"(3, 1, '404', 'Пятница'),"
        f"(3, 2, '404', 'Пятница'),"
        f"(1, 3, '404', 'Пятница'),"
        f"(1, 4, '404', 'Пятница'),"
        
        f"(2, 3, '404', 'Суббота'),"
        f"(2, 4, '404', 'Суббота'),"
        f"(5, 5, '404', 'Суббота'),"
        f"(5, 6, '404', 'Суббота');"
    ))

    await con.execute(text(
        f"insert into classes_timetable (subject_id, lesson_number, group_id, week_day) values"
        f"(3, 1, '405', 'Понедельник'),"
        f"(3, 2, '405', 'Понедельник'),"
        f"(2, 3, '405', 'Понедельник'),"
        f"(2, 4, '405', 'Понедельник'),"
        f"(4, 1, '405', 'Вторник'),"
        f"(4, 2, '405', 'Вторник'),"
        f"(2, 3, '405', 'Вторник'),"
        f"(2, 4, '405', 'Вторник'),"
        f"(1, 5, '405', 'Вторник'),"
        f"(1, 6, '405', 'Вторник'),"
        f"(2, 3, '405', 'Среда'),"
        f"(2, 4, '405', 'Среда'),"
        f"(3, 5, '405', 'Среда'),"
        f"(3, 6, '405', 'Среда'),"
        f"(2, 5, '405', 'Четверг'),"
        f"(2, 6, '405', 'Четверг'),"
        f"(5, 5, '405', 'Пятница'),"
        f"(5, 6, '405', 'Пятница'),"
        f"(2, 3, '405', 'Пятница'),"
        f"(2, 4, '405', 'Пятница');"
    ))

    await con.execute(text(
        f"insert into classes_timetable (subject_id, lesson_number, group_id, week_day) values"
        f"(2, 1, '312', 'Понедельник'),"
        f"(2, 2, '312', 'Понедельник'),"
        f"(5, 3, '312', 'Понедельник'),"
        f"(5, 4, '312', 'Понедельник'),"
        f"(2, 3, '312', 'Вторник'),"
        f"(2, 4, '312', 'Вторник'),"
        f"(4, 5, '312', 'Вторник'),"
        f"(4, 6, '312', 'Вторник'),"
        f"(2, 3, '312', 'Среда'),"
        f"(2, 4, '312', 'Среда'),"
        f"(1, 3, '312', 'Четверг'),"
        f"(1, 4, '312', 'Четверг'),"
        f"(5, 1, '312', 'Пятница'),"
        f"(5, 2, '312', 'Пятница'),"
        f"(2, 3, '312', 'Пятница'),"
        f"(2, 4, '312', 'Пятница');"
    ))

    start = datetime.datetime.strptime("11-01-2024", "%d-%m-%Y")
    end = datetime.datetime.strptime("25-06-2024", "%d-%m-%Y")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

    for date in date_generated:
        await con.execute(text(
            f"insert into current_class_schedule (default_class, date_of)"
            f"select id, '{date.date()}' from classes_timetable where week_day='{weekdays[date.weekday()]}';"
        ))



    start = datetime.datetime.strptime("11-01-2024", "%d-%m-%Y")
    end = datetime.datetime.strptime("20-07-2024", "%d-%m-%Y")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end - start).days)]

    for date in date_generated:
        await con.execute(text(
            f"insert into completed_lessons (lesson_id) "
            f"select id from current_class_schedule where date_of='{date.date()}';"
        ))


    # await con.execute(text(
    #     f"insert into student_evaluation (student_id, lesson_id, mark) values"
    #     f"(8, 17, 5),"
    #     f"(8, 15, 5),"
    #     f"(8, 19, 4);"
    # ))

    await con.execute(text(
        f"insert into users_accounts (id, password)"
        f"select id, '{bcrypt_context.hash('qwerty')}' from users;"
    ))


    await con.execute(text(
        f"insert into head_of_department (name, password) values " +
        f"('{ADMIN_MANAGER_USERNAME}', '{bcrypt_context.hash(ADMIN_MANAGER_PASSWORD)}');"
    ))


