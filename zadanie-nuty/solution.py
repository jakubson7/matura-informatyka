def calc_time(bpm, note):
    return {
        "1": 240,
        "2": 120,
        "4": 60,
        "8": 30,
        "16": 15,
        "32": 7.5
    }[note] / bpm

def get_data():
    # with open("./input.txt", mode="r") as file:
    #     content = file.read()
    #     return content + " "
    return "105 16 16 2 32 2 1 8 4 32 16 2 32 16 16 4 16 4 4 4 1 16 0" + " "
def solution():
    data = get_data()
    result = ""

    for line in data.split(" 0 "):
        if line == "" or line == "\n": continue
        line = line.strip().split(" ")
        bpm = int(line[0])
        time = 0

        for note in line[1:]:
            time += calc_time(bpm, note)
        
        result += str(time) + "\n"

    return result

def write_result(result):
    with open("./output.txt", mode="w") as file:
        file.write(result)

write_result(solution())
