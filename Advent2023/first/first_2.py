import re


number_map = {
  "one": 1,
  "two": 2,
  "three": 3,
  "four": 4,
  "five": 5,
  "six": 6,
  "seven": 7,
  "eight": 8,
  "nine": 9,
  "zero": 0,
  "1": 1,
  "2": 2,
  "3": 3,
  "4": 4,
  "5": 5,
  "6": 6,
  "7": 7,
  "8": 8,
  "9": 9,
  "0": 0,
}

def get_digits(word) -> int:
  pattern = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))")
  digits = [match.group(1) for match in re.finditer(pattern, word)]
  val = number_map.get(digits[0])*10+number_map.get(digits[-1])
  return val

def solution(is_trial: bool=False):
  summ = 0
  file_path = r'./trial_inputs.txt' if is_trial else r'./inputs.txt'
  with open(file_path, 'r') as file:
    for line in file:
      summ+=get_digits(line)
  return summ


if __name__ == "__main__":
  print(solution(is_trial = False))
