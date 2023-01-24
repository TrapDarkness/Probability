import math
def  dreamland(deck_size,  hand_size, desired_card_amount, copies_of_desired_cards):
    sample_space = math.comb(deck_size, hand_size)
    sample_space_mulligan = math.comb(deck_size, hand_size-1)
    leftover_choices = math.comb(deck_size - desired_card_amount, hand_size - desired_card_amount)
    leftover_choices_mulligan = math.comb(deck_size - desired_card_amount, hand_size - 1- desired_card_amount)
    if 0 == 1:
        first_hand = leftover_choices / sample_space
        second_hand = (1 - first_hand) * first_hand
        third_hand = (1- second_hand) * (leftover_choices_mulligan / sample_space_mulligan)
        total_probability = first_hand + second_hand + third_hand
        return first_hand, second_hand, third_hand, total_probability*100
    else:
        copies_combinations = 1
        for i in copies_of_desired_cards:
            copies_combinations *= math.comb(int(i.split("th")[1]), copies_of_desired_cards[i])
            #print("n: " + str(i.split("th")[1]) +  " r: " + str(copies_of_desired_cards[i]) + " This Combination: " + str(math.comb(int(i.split("th")[1]), copies_of_desired_cards[i])) +  " Total So Far: " + str(copies_combinations))
        #print("Desired Cards: " + str(desired_card_amount) + " Leftover Choices: " + str(leftover_choices) + " Sample Space:  " + str(sample_space))
        first_hand = (copies_combinations * leftover_choices) / sample_space
        second_hand = (1 - first_hand) * first_hand
        third_hand = (1- second_hand) * (copies_combinations * leftover_choices_mulligan / sample_space_mulligan)
        total_probability = first_hand + second_hand + third_hand
        return "Odds on first draw: " + str(first_hand*100) + "%", "Odds for two draws: " + str(second_hand*100) + "%", "Odds for third draw: " + str(third_hand*100) + "%", "Overall Odds with Mulligan " + str(total_probability*100) + "%"
        

print("Input Deck Size")
n = int(input())
print("Input Starting Hand Size")
h = int(input())
print("Input # of Desired Cards")
d = int(input())
c = {}
for i in range(d):
    print("Input #Copies of Card in Deck, #Copies of Card in Hand")
    answer = input()
    answer = answer.split(",")
    c[str(i) + "th" + answer[0]] = int(answer[1])
   # print(answer)
   # print(c)
print(str(dreamland(n,h,d,c)) + "%")