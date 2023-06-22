fileName = input()

with open(fileName, 'r') as file:
    data = file.read()
    
lines = data.strip().split('\n')

result = {}

for i in range(0, len(lines), 2):
    seasons = int(lines[i])
    show = lines[i + 1]
    
    if seasons in result:
        result[seasons].append(show)
    else:
        result[seasons] = [show]
        
formatted_result = ''

for seasons, shows in sorted(result.items(), reverse = True):
    formatted_result += f'{seasons}: {"; ".join(shows)}\n'

with open('output_keys.txt', 'w') as file:
    file.write(formatted_result)
    
sorted_shows = sorted(set(show for shows in result.values() for show in shows), reverse=True)

with open('output_titles.txt', 'w') as file:
    file.write('\n'.join(sorted_shows) + '\n')
