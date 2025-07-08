

# rate as a decimal (e.g., 0.01 for 1%)
# pulls is the number of attempts
# timestohit is the number of times you want to hit the target
# this is not including 50/50 chance
#every 90 pulls is guaranteed to hit the target
def calculate_probability(rate, pulls, timestohit):
    if pulls == 0:
        print("No pulls made, probability is 0.")
        return
    count = 0
    while pulls > 90:
        pulls -= 90
        count += 1
    probability = 1 - (1 - rate) ** pulls
    print(f"You are guaranteed {count} 5-Stars, Probability of getting another is {probability:.2%}. The goal is {timestohit}")
    return

def calculate_average_case(averagepulls, pulls):
    if pulls == 0:
        print("No pulls made, average case is 0.")
        return
    count = 0
    while pulls >= averagepulls:
        pulls -= averagepulls
        count += 1
    
    probability = 1 - (1 - 0.016) ** pulls

    print(f"You will pull: {count} 5-Stars when using the average case. {probability:.2%} chance of getting another 5-Star.")
    return

def WorstCase(pulls, guaranteed):
    if pulls == 0:
        print("No pulls made, worst case is 0.")
        return
    if guaranteed == False:
        count = pulls
        print(f"You will need: {count * 2} 5-Stars in the worst case with no guaranteed.")
    else:
        count = pulls
        print(f"You will need: {count * 2 - 1} 5-Stars in the worst case with guaranteed.")
    return

def main():
    # Example usage
    
    rate = 0.016  # 1.6% chance
    pulls = 66
    print(f"Rate: {rate*100}%, Pulls: {pulls}")
    timestohit = 1
    calculate_probability(rate, pulls, timestohit)
    averagepulls = 66  # Average pulls to get a 5-Star
    calculate_average_case(averagepulls, pulls)
    guaranteed = True  # Whether you have a guaranteed 5-Star
    WorstCase(timestohit, guaranteed)
    return
if __name__ == "__main__":
    main()
