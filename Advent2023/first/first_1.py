import re


def get_digits(word) -> int:
  digits = re.findall(r'\d', word)
  val = int(digits[0]+digits[-1])
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
