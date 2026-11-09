import unittest

from quiz import QUESTIONS, Question, calculate_score, run_quiz


class QuizTests(unittest.TestCase):
    def test_calculate_score_normalizes_answers(self):
        self.assertEqual(calculate_score([" B ", "a", "C"]), 3)

    def test_calculate_score_ignores_extra_answers(self):
        self.assertEqual(calculate_score(["b", "a", "c", "a"]), 3)

    def test_run_quiz_uses_injected_input_and_output(self):
        answers = iter(["b", "a", "c"])
        output = []

        score = run_quiz(input_fn=lambda _: next(answers), output_fn=output.append)

        self.assertEqual(score, len(QUESTIONS))
        self.assertIn("Você acertou 3 de 3 perguntas.", output[-1])

    def test_empty_quiz_has_zero_score(self):
        self.assertEqual(calculate_score([], ()), 0)
        self.assertEqual(run_quiz(input_fn=lambda _: "", output_fn=lambda _: "", questions=()), 0)

    def test_calculate_score_with_custom_question(self):
        question = Question("2 + 2?", ("a) 4", "b) 5"), "a")
        self.assertEqual(calculate_score(["a"], (question,)), 1)


if __name__ == "__main__":
    unittest.main()
