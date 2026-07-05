playing = True

while True:    
    try: 
        questions = [
            ["What is the capital of France? ", "Paris", "Rome", "Berlin", "Madrid", 1],
            ["Which planet is known as the Red Planet? ", "Earth", "Mars", "Jupiter", "Saturn", 2],
            ["What is the largest ocean on Earth? ", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
            ["How many colors are there in a rainbow? ", "5", "6", "7", "8", 3],
            ["Which animal is known as the Ship of the Desert? ", "Horse", "Camel", "Elephant", "Lion", 2],
            ["What is the baby of a dog called? ", "Kitten", "Cub", "Puppy", "Calf", 3],
            ["Which is the tallest animal on Earth? ", "Giraffe", "Elephant", "Ostrich", "Dinosaur", 1],
            ["In which direction does the sun rise? ", "West", "East", "North", "South", 2],
            ["What is the name of the gas that humans breathe in to survive? ", "Carbon Dioxide", "Nitrogen", "Helium", "Oxygen", 4],
            ["How many days are there in a standard year? ", "360", "364", "365", "366", 3],
            ["Which is the largest country in the world by land area? ", "Canada", "China", "United States", "Russia", 4]
        ]
        
        prizes = ["₹100", "₹500", "₹1000", "₹5000", "₹10000", "₹50000", "₹100000", "₹500000", "₹1000000", "₹5000000", "₹10000000"]
        
        i = 0

        for question in questions:
            print(question[0])
            print(f"a. {question[1]}")
            print(f"b. {question[2]}")
            print(f"c. {question[3]}")
            print(f"d. {question[4]}")

            a = int(input("Enter Your answer:  1 For A, 2 For B, 3 For C, 4 For D \n "))

            if a == question[5]:
                print("Correct Answer \n")
            else: 
                print("Wrong Answer")
                print(f"The correct answer is {question[5]}")
                print("Better luck next time")
                
                playing = False
                break
            
            print(prizes[i])
            i += 1
            
        if playing:
            print("\nCongratulations! You answered all questions correctly!")
            playing = False

    except Exception as e:
        print("Enter the valid Input!") 