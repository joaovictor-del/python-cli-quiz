"""Quiz interativo de conhecimentos básicos de Python."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    prompt: str
    choices: tuple[str, ...]
    answer: str


QUESTIONS = (
    Question(
        "Qual palavra-chave define uma função em Python?",
        ("a) func", "b) def", "c) function"),
        "b",
    ),
    Question(
        "Qual tipo é usado para uma sequência mutável?",
        ("a) list", "b) tuple", "c) str"),
        "a",
    ),
    Question(
        "Qual símbolo inicia um comentário de uma linha?",
        ("a) //", "b) <!--", "c) #"),
        "c",
    ),
)


def calculate_score(answers: list[str], questions: tuple[Question, ...] = QUESTIONS) -> int:
    """Conta respostas corretas, ignorando diferenças de maiúsculas e espaços."""
    return sum(
        answer.strip().lower() == question.answer
        for answer, question in zip(answers, questions)
    )


def run_quiz(
    input_fn=input,
    output_fn=print,
    questions: tuple[Question, ...] = QUESTIONS,
) -> int:
    answers = []
    for number, question in enumerate(questions, start=1):
        output_fn(f"\n{number}. {question.prompt}")
        for choice in question.choices:
            output_fn(choice)
        answers.append(input_fn("Sua resposta (a/b/c): "))

    score = calculate_score(answers, questions)
    output_fn(f"\nVocê acertou {score} de {len(questions)} perguntas.")
    return score


if __name__ == "__main__":
    run_quiz()
