def conflicting_and_non_conflicting(meetings):
    meetings.sort(key=lambda x: x[0])

    c = []
    nc = [meetings[0]]  
    
    for i in range(1, len(meetings)):
        if meetings[i][0] < nc[-1][1]:  
            c.append(meetings[i])
        else:
            nc.append(meetings[i])

    return c, nc

# Example usage
meeting_times = [(1, 3), (2, 4), (4, 6), (5, 6), (6, 8)]
conflicting, non_conflicting = conflicting_and_non_conflicting(meeting_times)
print("Conflicting meetings:", conflicting)
print("Non-conflicting meetings:", non_conflicting)
