r"""module entry point

UI:
    - Prisoner's dilemma
    - run simulation          ---[A]
    - setup simulation        ---[B]

    [A] - auto run every possible simulation
        - each strategy face off against itself and all other strategies
        - display full strategy statistics ranked by total score

        strategy                  | score | average | mode |
        always cooperate strategy |  500  |    3    |   5  |
        -                         |   -   |    -    |   -  |

    [B] - select strategy for slot 1 [list of strategies]
        - select strategy for slot 2 [list of strategies]
        - specify number of rounds >> _

        - run simulate with strategy
        - display statistics ranked by total score

        strategy                  | score | average | mode |
        always cooperate strategy |  500  |    3    |   5  |
        -                         |   -   |    -    |   -  |

"""

from simulation import (
    process_run_simulation,
    process_setup_simulation,
    reset_strategies,
    summarize_simulation_table,
)


print("Prisoner's dilemma")

while True:
    print(
        "   ",
        "   [1]---   run simulation        ---[-]",
        "   [2]---   create matchup        ---[-]",
        "   [3]---   close (X)             ---[-]",
        sep="\n",
    )
    user_choice = input("> ")

    if user_choice in ["3", "x", "X"]:
        break

    if user_choice in ["1"]:
        process_run_simulation()

        print(
            "   ",
            "   [1]---   Show summary?         ---[-]",
            "   [2]---   New Simulation        ---[-]",
            "   [3]---   close (X)             ---[-]",
            sep="\n",
        )
        show_pattern = input("> ")
        if show_pattern in ["1"]:
            summarize_simulation_table()

        if show_pattern in ["3", "x", "X"]:
            break
        reset_strategies()

    if user_choice in ["2"]:
        process_setup_simulation()
        reset_strategies()
