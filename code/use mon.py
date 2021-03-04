import montyhall


"""Usage
$ python montyhall.py {#doors} {#simulation}

Example:

$ python montyhall.py 3 100000
probability when you stay
0.33374
probability when you change
0.66786
"""

door_cnt = int(3)
sim_cnt = int(100)
print('probability when you stay')
print(monte_carlo(sim_cnt, door_cnt, False))
print('probability when you change')
print(monte_carlo(sim_cnt, door_cnt, True))


python montyhall.py 3 100000

if __name__ == "__main__":
    main()