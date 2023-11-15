import random
from django.core.management import BaseCommand
from faker import Faker
from django.contrib.auth.models import User
from app.models import Question, Profile, Like_question, Like_answer, Answer, Tag

fake = Faker()

class Command(BaseCommand):
    help = "Fills database with fake data"

    def add_arguments(self, parser):
        parser.add_argument("num", type=int)

    def handle(self, *args, **kwargs):
        num = kwargs['num']
        # # Создайте пользователей
        users = [
            User(
                username=str(fake.user_name()+str(i)),
                email=fake.email(),
                password=fake.password(),
            ) for i in range(num)
        ]
        User.objects.bulk_create(users)



        # Создайте профили для каждого пользователя
        profiles = [
            Profile(
                email=fake.email(),
                nickname=fake.user_name(),
                user=user,
            ) for user in users
        ]
        Profile.objects.bulk_create(profiles)

        # Создайте теги
        tags = [
            Tag(
                title=fake.word(),
            ) for _ in range(num)
        ]
        Tag.objects.bulk_create(tags)



        questions = [
            Question(
                title=fake.sentence(),
                content=fake.text(),
                author=profiles[fake.random_int(min=0, max=len(profiles) - 1)],
                tag=tags[fake.random_int(min=0, max=len(tags) - 1)],
                date=fake.date_between(start_date='-10y', end_date='today')
            )for _ in range(num*10)
        ]
        Question.objects.bulk_create(questions)

        answers = [
            Answer(
                content=fake.text(),
                author=profiles[fake.random_int(min=0, max=len(profiles) - 1)],
                status='s' if fake.random_int(min=0, max=1) == 0 else 'n',
                date=fake.date_between(start_date='-10y', end_date='today'),
                question=questions[fake.random_int(min=0, max=len(questions) - 1)]
            ) for _ in range(num * 100)
        ]
        Answer.objects.bulk_create(answers)

        likes_question = [
            Like_question(
                type='l' if fake.random_int(min=0, max=1) == 0 else 'd',
                user=profiles[fake.random_int(min=0, max=len(profiles) - 1)],
                question = questions[fake.random_int(min=0, max=len(questions) - 1)]
            ) for _ in range(num * 200)
        ]
        Like_question.objects.bulk_create(likes_question)

        likes_answer = [
            Like_answer(
                type='l' if fake.random_int(min=0, max=1) == 0 else 'd',
                user=profiles[fake.random_int(min=0, max=len(profiles) - 1)],
                question=questions[fake.random_int(min=0, max=len(questions) - 1)]
            ) for _ in range(num * 200)
        ]
        Like_answer.objects.bulk_create(likes_answer)
