import csv


def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    heaeder = next(reader)
    data = []
    print(heaeder)
    for row in reader:
      iterable = zip(heaeder, row)
      country_dict = {key: value for key, value in iterable}
      data.append(country_dict)
  return data


if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data)
