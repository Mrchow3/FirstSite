#./manage.py shell < myscript.py


from polls.models import Question, Choice
from django.utils import timezone

for i in range(1,21):
    q = Question(title = f"Filler Title #{i}", question_text = f"Filler Text #{i}", date = timezone.now())
    q.save()

    c1 = Choice(question = q, choice_text = "Yes")
    c2 = Choice(question = q, choice_text = "No")

    c1.save()
    c2.save()