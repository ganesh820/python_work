import time

questions_list = [["What does API stand for?", "Application Programming Interface", "Advanced Programming Interface",
                   "Automated Program Integration", "Application Programming Interface"],
                  ["Which programming language is known for its simplicity and readability?", "Java", "Python", "C++",
                   "Python"],
                  ["What is the purpose of version control systems like Git?",
                   "To manage different versions of source code", "To optimize database queries",
                   "To develop graphical user interfaces", "To manage different versions of source code"],
                  ["Which technology is used for virtualization in IT infrastructure?", "VMware", "Microsoft Excel",
                   "Adobe Photoshop", "VMware"],
                  ["What is the role of a cybersecurity analyst?", "To protect computer systems from threats",
                   "To design user interfaces", "To manage corporate finances",
                   "To protect computer systems from threats"],
                  ["Which cloud computing service is known for its serverless computing platform?",
                   "Google Cloud Platform", "Amazon Web Services", "Microsoft Azure", "Amazon Web Services"],
                  ["What does SQL stand for in the context of databases?", "Structured Query Language",
                   "Sequential Query Language", "System Query Language", "Structured Query Language"],
                  [
                      "Which programming paradigm focuses on treating computation as the evaluation of mathematical functions?",
                      "Object-oriented programming", "Functional programming", "Procedural programming",
                      "Functional programming"],
                  ["What is the purpose of a VPN?", "To establish a secure connection over a public network",
                   "To organize data in relational databases", "To develop virtual reality applications",
                   "To establish a secure connection over a public network"],
                  ["Which technology is used for containerization of applications?", "Docker", "WordPress", "Magento",
                   "Docker"]]

Rewards = [1000, 10000, 100000, 200000, 500000, 1000000, 2000000, 5000000, 9000000, 10000000]

number_of_questions = len(questions_list)
take_home_money = 0


def user_selection(user_input):
    try:

        if user_input == "A":
            return 1

        if user_input == "B":
            return 2

        if user_input == "C":
            return 3

    except Exception as e:
        print(f"issue is been occured in user_selection, issue is : {e}")


def game_start():
    global take_home_money
    for i in range(number_of_questions):
        print(f"for {Rewards[i]} rupees, Here is {i + 1}st question on your screen :\n")
        time.sleep(1)
        Question = f"{questions_list[i][0]}\n A. {questions_list[i][1]} \n B. {questions_list[i][2]} \n C. {questions_list[i][3]}"
        print(Question)
        time.sleep(1)
        user_answer = input("Provide your answer here :")

        user_answer = user_selection(user_answer)
        print(questions_list[i][user_answer])
        print(questions_list[i][4])
        if questions_list[i][user_answer] == questions_list[i][4]:
            print("you have given the correct answer")
            print(f"\nYou have earn the reward of amount {Rewards[i]}\n")

        elif questions_list[i][user_answer] != questions_list[i][4] and 3 < i < 8:
            print("Hello")
            print(f"unfortunately your answer is wrong.\n correct answer is : {questions_list[i][4]}")
            print(f"you are exiting game with amount : 100000\n")
            break

        else:
            if 3 < i < 7 :
                print(f"you are exiting game with amount : 100000\n")
                take_home_money = 10000

            if 7 < i < 9:
                print(f"you are exiting game with amount : 100000\n")
                take_home_money = 500000
            else :
                print(f"unfortunately your answer is wrong.\n correct answer is : {questions_list[i][4]}")
                print(f"i is {i}")
                break


print("Welcome to the Kaun Banega Crorepati\n")
time.sleep(1)

game_start()

print("game is over for you")
print(take_home_money)
