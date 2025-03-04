from rest_framework import viewsets
from .models import Student, Test, TestResult, Question
from .serializers import StudentSerializer, TestSerializer, TestResultSerializer, QuestionSerializer
from rest_framework.response import Response



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer

class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer

    def create(self, request, *args, **kwargs):
        student_id = request.data.get('student')
        test_id = request.data.get('test')
        answers = request.data.get('answers', {})  # JSON formatda keladi: {"1": "A", "2": "B"}

        try:
            student = Student.objects.get(id=student_id)
            test = Test.objects.get(id=test_id)
        except (Student.DoesNotExist, Test.DoesNotExist):
            return Response({"error": "Student or Test not found"}, status=400)

        questions = Question.objects.filter(test=test)
        total_questions = questions.count()
        correct_answers = 0

        for question in questions:
            if str(question.id) in answers and answers[str(question.id)] == question.correct_answer:
                correct_answers += 1

        score = (correct_answers / total_questions) * test.max_score if total_questions > 0 else 0

        test_result = TestResult.objects.create(student=student, test=test, score=score)
        return Response({"message": "Test result saved", "score": score}, status=201)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
