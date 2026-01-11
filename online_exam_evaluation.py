# online_exam_system.py

class Exam:
    def evaluate(self):
        raise NotImplementedError


class MCQExam(Exam):
    def __init__(self, score):
        self.score = score

    def evaluate(self):
        return f"MCQ Exam Score: {self.score}"


class CodingExam(Exam):
    def __init__(self, passed_testcases, total_testcases):
        self.passed = passed_testcases
        self.total = total_testcases

    def evaluate(self):
        return f"Coding Score: {self.passed}/{self.total} test cases passed"


class DescriptiveExam(Exam):
    def evaluate(self):
        return "Descriptive exam needs manual evaluation"


# Main
print("---- Online Exam Evaluation ----")
print("1. MCQ Exam")
print("2. Coding Exam")
print("3. Descriptive Exam")

choice = input("Choose exam type: ")

if choice == "1":
    score = int(input("Enter MCQ score: "))
    exam = MCQExam(score)
elif choice == "2":
    passed = int(input("Passed test cases: "))
    total = int(input("Total test cases: "))
    exam = CodingExam(passed, total)
elif choice == "3":
    exam = DescriptiveExam()
else:
    print("Invalid choice")
    exit()

print(exam.evaluate())
