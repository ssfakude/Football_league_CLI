from re import findall

def calculate_match_points(team1, team2, score1, score2):
    if score1 == score2:
        return {team1:1, team2: 1}
    elif score1 > score2:
       return {team1:3, team2: 0} 
    else:
        return {team1:0, team2: 3}


def football_legaue(file_name):
    final_results ={}
    lines = []
    try:
        with open(file_name) as f:
            lines = f.readlines()
    except:
        return "Unable to load file: Enter Correct filename and make sure it is saved in your working directory"
    for line in lines:
        match=  findall(r'(?<!\S)(?:[$]\S+|[^-?\d+\.?\d*]+)\b|-?\d+\.?\d*', line)
        #print(match) return -> ['Lions ', '3', 'Snakes ', '3']
        if len(match) != 4:
            return  f'Match: {match}, has incorrect expected values '
        team1 = match[0]
        team2 = match[2]
        if int(match[1]) < 0 or int(match[3])< 0:
            return f'The goal cannot be negative in match : {match} '
        else:
            score1 = match[1]
            score2 = match[3]
        points = calculate_match_points(team1, team2, score1, score2)
    
        if team1 not in final_results:
            final_results[team1] =  points[team1]
        else:
            final_results[team1] +=  points[team1]
        if team2 not in final_results:
                final_results[team2] =  points[team2]
        else:
            final_results[team2] +=  points[team2]

    return  sorted(final_results.items(), key=lambda x: (-x[1], x[0]))
if __name__=='__main__':

    count=1
    results=football_legaue("input.txt")
    for team in results:
        print(f'{count}. {team[0]}, {team[1]} pts')  
        count+=1
 
