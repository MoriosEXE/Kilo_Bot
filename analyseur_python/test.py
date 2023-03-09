def print_bot_positions(bot_positions):
    for i, step in enumerate(bot_positions):
        print(f"Step {i+1}:")
        for j, bot_pos in enumerate(step):
            bot_name = f"Bot {j+1}"
            posx, posy = bot_pos[0], bot_pos[1]
            if i < len(bot_positions)-1:
                next_posx, next_posy = bot_positions[i+1][j][0], bot_positions[i+1][j][1]
                print(f"{bot_name} is at ({posx}, {posy}), moving to ({next_posx}, {next_posy})")
            else:
                print(f"{bot_name} is at ({posx}, {posy})")

bot_positions = [[[2, 4], [8, 12],[1,1]], [[24, 12], [32, 14],[2,2]],[[100,40],[64,62],[3,3]]]
print_bot_positions(bot_positions)