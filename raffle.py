# mainly written by Github Copilot

from dataclasses import dataclass
from typing import List
import csv
import random
import sys

@dataclass
class RaffleEntry:
    name: str
    orig_tickets: int
    curr_tickets: int
    orig_win_chance: float = 0.0
    curr_win_chance: float = 0.0

def read_raffle_data(filename: str) -> tuple[List[RaffleEntry], int, int]:
    entries = []
    all_tickets = 0
    longest_name_length = 0
    with open(filename, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, ['tickets','name'])
        for row in reader:
            entry = RaffleEntry(
                name    = row['name'],
                orig_tickets = int(row['tickets']),
                curr_tickets = int(row['tickets'])
            )
            entries.append(entry)
            all_tickets += entry.orig_tickets
            if len(entry.name) > longest_name_length:
                longest_name_length = len(entry.name)
    return entries, all_tickets, longest_name_length

def print_raffle_entries(entries: List[RaffleEntry], longest_name_length: int):
    print(f"{'Name':<{longest_name_length}} {'Current':>11} {'Original':>11}")
    print("-" * longest_name_length, end=' ')
    print('-' * 11, end=' ')
    print('-' * 11)
    for entry in entries:
        if entry.curr_tickets > 0:
            print("\033[92m", end="")
        else:
            print("\033[90m", end="")
        trend = ""
        if entry.curr_tickets == 0:
            trend = "\033[90m✗\033[0m"
        else:
            if entry.curr_win_chance > entry.orig_win_chance:
                trend = "\033[92m↑\033[0m"
            elif entry.curr_win_chance < entry.orig_win_chance:
                trend = "\033[91m↓\033[0m"
            else:
                trend = "="
        print(f"{entry.name:<{longest_name_length}} {entry.curr_tickets:>3} {entry.curr_win_chance:>7.2%} {entry.orig_tickets:>3} {entry.orig_win_chance:>7.2%} {trend}")
    print("\033[0m", end="")

if len(sys.argv) != 2:
    print("Usage: python raffle.py <raffle_data_file>")
    sys.exit(1)

entries, all_tickets, longest_name_length = read_raffle_data(sys.argv[1])

for entry in entries:
    entry.orig_win_chance = entry.orig_tickets / all_tickets
    entry.curr_win_chance = entry.orig_win_chance

sorted_entries = sorted(entries, key=lambda e: e.curr_win_chance, reverse=True)
print('The raffle has started!')
print()
print(f'Tickets remaining: {all_tickets}')
print()
print_raffle_entries(sorted_entries, longest_name_length)
print("\nPress Enter to eliminate the next ticket...")
input()

ticket_pool = []
for entry in entries:
    ticket_pool.extend([entry] * entry.curr_tickets)
random.shuffle(ticket_pool)

# import pprint
# pprint.pprint(ticket_pool[0])

while all_tickets > 1:
    removed_entry = ticket_pool.pop()
    all_tickets -= 1
    print()
    print(f'Tickets remaining: {all_tickets}')
    print()
    find_index = None
    for i, entry in enumerate(entries):
        if entry.name == removed_entry.name:
            find_index = i
            break
    if find_index is not None:
        entries[find_index].curr_tickets -= 1
        if entries[find_index].curr_tickets < 0:
            entries[find_index].curr_tickets = 0
        for entry in entries:
            entry.curr_win_chance = entry.curr_tickets / all_tickets
    
    sorted_entries = sorted(entries, key=lambda e: e.curr_win_chance, reverse=True)
    print_raffle_entries(sorted_entries, longest_name_length)
    # TODO when only one entry has more than 0 tickets, end the raffle
    remaining_entries = sum(1 for entry in entries if entry.curr_tickets > 0)
    if remaining_entries <= 1:
        break
    print()
    print("Press Enter to eliminate the next ticket...")
    input()

print()
print('The winner is:', end=' ')
print("\033[92m", end='')
print(ticket_pool[0].name,end='')
print("\033[0m", end='')
print('!')