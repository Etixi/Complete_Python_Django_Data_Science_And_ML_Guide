import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents


@pytest.fixture
def empty_classroom():
    return Classroom(teacher=Teacher("Professor Dumbledore"), students=[], course_title="Defense Against the Dark Arts")


def test_add_students(empty_classroom):
    student1 = Student("Harry Potter")
    student2 = Student("Hermione Granger")

    empty_classroom.add_students(student1)
    assert len(empty_classroom.students) == 1
    assert empty_classroom.students[0].name == "Harry Potter"

    empty_classroom.add_students(student2)
    assert len(empty_classroom.students) == 2
    assert empty_classroom.students[1].name == "Hermione Granger"


def test_add_too_many_students(empty_classroom):
    students = [Student(f"Student{i}") for i in range(11)]

    for student in students[:10]:
        empty_classroom.add_students(student)

    try:
        empty_classroom.add_students(students[-1])
    except TooManyStudents as e:
        print(f"Caught TooManyStudents exception: {e}")
        raise e



def test_remove_student(empty_classroom):
    student1 = Student("Ron Weasley")
    student2 = Student("Luna Lovegood")

    empty_classroom.add_students(student1)
    empty_classroom.add_students(student2)

    empty_classroom.remove_student("Ron Weasley")
    assert len(empty_classroom.students) == 1
    assert empty_classroom.students[0].name == "Luna Lovegood"


def test_change_teacher(empty_classroom):
    new_teacher = Teacher("Professor McGonagall")

    empty_classroom.change_teacher(new_teacher)
    assert empty_classroom.teacher.name == "Professor McGonagall"


# Add more tests as needed based on the functionalities you want to test.
