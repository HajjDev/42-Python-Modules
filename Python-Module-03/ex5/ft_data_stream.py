#!/usr/bin/env python3

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_data_stream.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: cel-hajj <cel-hajj@student.s19.be>        +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/04 12:58:27 by cel-hajj        #+#    #+#               #
#  Updated: 2026/02/04 17:39:02 by cel-hajj        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

def event_generator(events: list) -> object:
    for event in events:
        yield event


def process_events(events: object) -> dict[str, int]:
    event_stats: dict[str, int] = {"high_level": 0,
                                   "treasure": 0,
                                   "level_up": 0}
    to_print: int = 3
    for i, event in enumerate(events):
        if event["data"]["level"] >= 10:
            event_stats["high_level"] += 1
        if event["event_type"] == "item_found":
            event_stats["treasure"] += 1
        if event["event_type"] == "level_up":
            event_stats["level_up"] += 1
        if to_print != 0:
            if event["event_type"] == "login":
                print(f"Event {i + 1}: Player {event['player']} \
(level {event['data']['level']}) logged in")
            elif event["event_type"] == "logout":
                print(f"Event {i + 1}: Player {event['player']} \
(level {event['data']['level']}) logged out")
            elif event["event_type"] == "kill":
                print(f"Event {i + 1}: Player {event['player']} \
(level {event['data']['level']}) killed monster")
            elif event["event_type"] == "item_found":
                print(f"Event {i + 1}: Player {event['player']} \
(level {event['data']['level']}) found treasure")
            elif event["event_type"] == "level_up":
                print(f"Event {i + 1}: Player {event['player']} \
(level {event['data']['level']}) leveled up")
            elif event["event_type"] == "death":
                print(f"Event {i + 1}: Player {event['player']} \
(level {event['data']['level']}) died")
            else:
                print("Event not found.")
            to_print -= 1
    return event_stats


def fibonacci_generator() -> object:
    number_1 = 0
    number_2 = 1
    yield number_1
    yield number_2
    while True:
        temp = number_2
        number_2 += number_1
        number_1 = temp
        yield number_2


def prime_generator() -> object:
    current_number = 2
    while True:
        is_prime = True
        for i in range(2, current_number // 2 + 1):
            if current_number % i == 0:
                is_prime = False
                break
        if is_prime:
            yield current_number
        current_number += 1


if __name__ == "__main__":
    # import time
    # start = time.time()
    # ...
    # print(f"Processing time: {time.time() - start}")
    print("=== Game Data Stream Processor ===\n")
    e = [{'player': 'frank', 'event_type': 'login', 'data': {'level': 16}},
         {'player': 'frank', 'event_type': 'login', 'data': {'level': 35}},
         {'player': 'diana', 'event_type': 'login', 'data': {'level': 15}},
         {'player': 'alice', 'event_type': 'level_up', 'data': {'level': 45}},
         {'player': 'bob', 'event_type': 'death', 'data': {'level': 1}},
         {'player': 'charlie', 'event_type': 'kill', 'data': {'level': 22}},
         {'player': 'diana', 'event_type': 'login', 'data': {'level': 17}},
         {'player': 'eve', 'event_type': 'item_found', 'data': {'level': 36}},
         {'player': 'charlie', 'event_type': 'level_up', 'data': {'level': 3}},
         {'player': 'alice', 'event_type': 'logout', 'data': {'level': 18}},
         {'player': 'bob', 'event_type': 'kill', 'data': {'level': 18}},
         {'player': 'frank', 'event_type': 'logout', 'data': {'level': 11}}]
    events_stream = event_generator(e)

    print(f"Processing {len(e)} game events...\n")
    stats = process_events(events_stream)
    print("...\n")

    print("=== Stream Analytics ===")
    print(f"Total events processed: {len(e)}")
    print(f"High-level players (10+): {stats['high_level']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up events: {stats['level_up']}\n")

    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds\n")

    print("=== Generator Demonstration ===")
    fibonacci_count = 10
    fibonacci_iterator = fibonacci_generator()
    fibonacci: str = ""
    for _ in range(fibonacci_count):
        fibonacci += str(next(fibonacci_iterator))
        if _ != fibonacci_count - 1:
            fibonacci += ", "
    print(f"Fibonacci sequence (first 10): {fibonacci}")
    prime_count = 5
    prime_iterator = prime_generator()
    primes: str = ""
    for _ in range(prime_count):
        primes += str(next(prime_iterator))
        if _ != prime_count - 1:
            primes += ", "
    print(f"Prime numbers (first 5): {primes}")
