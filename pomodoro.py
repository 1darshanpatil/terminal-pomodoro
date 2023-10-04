#!/usr/bin/env python3

import sys
import time
import subprocess


WORK_TIME = 25
BREAK_TIME = 5
ROUNDS = 4

def progress_bar(msg, time_sec):
    print(f"{msg} for {time_sec // 60} min")
    try:
        for i in range(time_sec + 1):
            perc = i * 100 // time_sec
            candle = "█" * perc + "-" * (100 - perc)
            print(f'\r{candle}: {perc}%', end='', flush=True)
            time.sleep(1)
        print("\n")
    except KeyboardInterrupt:
        # In case you stop the code from the execution.
        sys.exit(1)


def calculate_final_break(work_time, break_time, rounds):
    """
    Calculates the final break time in seconds based on the given work time, break time, and number of rounds.

    Args:
        work_time (int): The duration of each work interval in minutes.
        break_time (int): The duration of each regular break in minutes.
        rounds (int): The total number of completed pomodoro intervals (work round + break) so far.

    Returns:
        int: The calculated final break time in seconds.

    Comment:
    This function by default sets a default final break time of 30 minutes, assuming each work interval is 25 minutes and each regular break is 5 minutes for 4 completed rounds.

    Please note that this function will be further modified in the future with a statistical model to consider work, break, round, and human fatigue factors for more accurate final break time calculations.
    """
    final_break_time = 30  # mins
    final_break = final_break_time * 60  # seconds
    return final_break


def pomodoro(*args, **kwargs):
    default_values = {'-w': WORK_TIME, '-b': BREAK_TIME, '-r': ROUNDS}
    work_time = kwargs.get('-w', default_values['-w'])
    break_time = kwargs.get('-b', default_values['-b'])
    rounds = kwargs.get('-r', default_values['-r'])
    #    print(work_time, break_time, rounds)

    total_sessions = [work_time, break_time] * rounds
    total_min = sum(total_sessions)
    try:
        for work_or_break, session in enumerate(total_sessions):
            if work_or_break % 2 == 0:
                print("Round:", work_or_break // 2 + 1)

            if work_or_break % 2 == 0:
                msg = "Work Time"
                time_seconds = session * 60
                progress_bar(msg, time_seconds)
            elif work_or_break == len(total_sessions) - 1:
                msg = "Final Break"
                final_break = calculate_final_break(work_time, break_time, rounds)
                """
                This function by default sets a default final break time of 30 minutes, assuming each work interval is 25 minutes and each regular break is 5 minutes for 4 completed rounds.
                Please note that this function will be further modified in the future with a statistical model to consider work, break, round, and human fatigue factors for more accurate final break time calculations.
                """
                # I want final_break to be
                progress_bar(msg, final_break)
            else:
                msg = "Break Time"
                time_seconds = session * 60
                progress_bar(msg, time_seconds)
    finally:
        print("End!")

def help():
    print("Pomodoro Timer Help")
    print("-------------------")
    print("Usage:")
    print("  python <script_name> [OPTIONS]")
    print()
    print("Options:")
    print("  -w=<work_time>  Set the duration of each work interval in minutes. Default: 25 minutes.")
    print("  -b=<break_time> Set the duration of each regular break in minutes. Default: 5 minutes.")
    print("  -r=<rounds>     Set the total number of completed pomodoro intervals (work round + break). Default: 4.")
    print("  -h              Display this help message.")
    print()
    print("Example:")
    print("  python pomodoro.py -w=30 -b=10 -r=3")
    print("  This will start a pomodoro timer with work interval of 30 minutes, break of 10 minutes, and 3 completed rounds.")
    print()
    print("Note:")
    print("  The script will use default values if any option is not provided.")
    print("  Only -w, -b, -r options are recognized. All other parameters will be ignored.")
    print("  Press Ctrl+C during the timer to stop the script.")
    print()

def run_pomo():
    if len(sys.argv) <= 1:
        pomodoro()
    elif '-h' in sys.argv:
        help()
        sys.exit(0)
    else:
        args_dict = {}
        valid_args = {'-b', '-r', '-w'}
        for arg in sys.argv[1:]:
            key, value = arg.split("=")
            args_dict[key] = int(value)
            if key not in valid_args:
                print(f"We have ignored you arg: {key}\nFor help please try -h.\n")
        pomodoro(**args_dict)


if __name__ == "__main__":
    run_pomo()

