quiz_question = {

    "What is the capital of Nepal" : "c",

    "Who wrote the book Think and grow rich?" : "a",

    "What do you call a term 'Root under minus 1 in mathematics" : "b",

    "If (3x+2=11), what is the value of (x)?" : "a"                            


}
#c a b a
options = [
    ["a.Bhaktapur", "b.Pokhara", "c.Kathmandu","d.Kirtipur"],
    ["a.Napolean Hill","Napolean Bonapart","Elon Musk","Napolian Sharma"],
    ["a.Whole number", "b.Imaginary Number","Real Number","Integers"],
    ["3","1","4","9"]
    ]

score = 0
question_number = 0
for question,correct_answer in quiz_question.items():
    print("\n"+question)
    for option in options[question_number]:
        print(option)

    answer = input("Enter your answer (a/b/c/d): ").lower()
    if answer == "a" or "b" or "c" or "d":
        if answer == correct_answer:
            print("correct")
            score+=1

        else:
            print(f"Wrong the answer was {correct_answer} ")
        question_number+=1

    else:
        print("Try a b c or d only")

print(f"\n Quiz over! Your final score was {score}/{len(quiz_question)}")