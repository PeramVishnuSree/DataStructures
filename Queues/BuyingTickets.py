# You are given a 0-indexed integer array tickets of length n where the number of tickets that
# the ith person would like to buy is tickets[i].
# Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and
# has to go back to the end of the line (which happens instantaneously) in order to buy more tickets.
# If a person does not have any tickets left to buy, the person will leave the line.
# Return the time taken for the person at position k (0-indexed) to finish buying tickets.

def BuyingTickets(tickets, k):
    t = tickets[k]
    n = 0
    while tickets[k] != 0:
        for i in range(len(tickets)):
            if tickets[i] == 0:
                continue
            tickets[i] = tickets[i] - 1
            n += 1
            if tickets[k] == 0:
                break
    return n