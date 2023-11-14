# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# student_grades = {}
# for key in student_scores:
#     if student_scores[key] >= 90:
#         student_grades[key] = "outstanding"
#     elif student_scores[key] >= 80:
#         student_grades[key] = "accepted"
#     elif student_scores[key] >= 70:
#         student_grades[key] = "nice"
#     elif student_scores[key] < 70:
#         student_grades[key] = "fail"
# print(student_grades)

## =====================================================================================

# country = input()  # Add country name
# visits = int(input())  # Number of visits
# list_of_cities = eval(input())  # create list from formatted string

# travel_log = [
#     {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
#     {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
# ]


# # Write the function that will allow new countries to be added to the travel_log.
# def add_new_country(country, visits, list_of_cities):
#     travel_log.append(
#         {
#             "country": country,
#             "visits": visits,
#             "cities": list_of_cities,
#         }
#     )


# # Do not change the code below 👇
# add_new_country(country, visits, list_of_cities)
# print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
# print(f"My favourite city was {travel_log[2]['cities'][0]}.")

## =====================================================================================

## blind bid
# import os

# clear = lambda: os.system("cls")
# list_of_bids = []
# add_more_bids = True


# def biding(name, bid):
#     list_of_bids.append({"name": name, "bid": int(bid)})


# def winner_bid(list_of_bids):
#     the_winner = {"bid": 0}
#     for i in list_of_bids:
#         if i["bid"] > the_winner["bid"]:
#             the_winner = i
#     return f"the winner is {the_winner['name']} with a bit of ${the_winner['bid']}"


# while add_more_bids:
#     name = input("what is your name?: ")
#     bid = input("what is your bid?: ")
#     biding(name, bid)
#     mor_bidders = input("are there any more bidders?: Type 'YES' or 'NO' ").lower()
#     if mor_bidders == "yes":
#         clear()
#     else:
#         add_more_bids = False

# res = winner_bid(list_of_bids)
# print(res)
