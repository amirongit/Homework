from ..models import Student, Teacher, User


def create_user(user_type, username='dummyuser',
                email='dummyuser@email.com', password='dummypassword',
                first_name='Dummy', last_name='User'):
    return User.objects.create_user(username=username, email=email,
                                    password=password,
                                    first_name=first_name, last_name=last_name,
                                    user_type=user_type)


def create_student(username='dummystudent', email='dummystudent@email.com',
                   password='dummypassword', first_name='Dummy',
                   last_name='Student'):
    return Student.objects.create_user(username=username, email=email,
                                       password=password,
                                       first_name=first_name,
                                       last_name=last_name)


def create_teacher(username='dummyteacher', email='dummyteacher@email.com',
                   password='dummypassword', first_name='Dummy',
                   last_name='teacher'):
    return Teacher.objects.create_user(username=username, email=email,
                                       password=password,
                                       first_name=first_name,
                                       last_name=last_name)
