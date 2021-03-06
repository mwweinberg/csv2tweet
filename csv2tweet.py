import csv

output = open('output.txt', 'w')

with open('input.csv') as csvfile:
    filereader = csv.DictReader(csvfile)
    for row in filereader:
        print(row)
        output.write('New certified open source hardware! The @')
        output.write(row['twitter'] + ' ')
        output.write(row['hw'] + ' ')
        output.write('(')
        output.write(row['uid'] + ') ')
        output.write('https://certification.oshwa.org/' + row['uid'].lower() + '.html')
        output.write('\n')
        output.write('\n')
        output.write("Have OSHW to certify? It's free! https://certification.oshwa.org/")
        output.write('\n')
        output.write('\n')
        output.write("Want to see other certified OSHW? Check out the full list! https://certification.oshwa.org/list.html")
        output.write('\n')
        output.write('\n')
        output.write('\n')
        output.write('\n')






output.close()
