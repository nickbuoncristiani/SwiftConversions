import sqlite3

"""Takes in a list of I/O events ('sex + event + year') and a score for input
Set and returns an equivalent score for outputSet as well as the percentile."""
def compare(inputSet, outputSet, db, score, inputStartGrade, inputEndGrade, outputStartGrade, outputEndGrade):
    
    with sqlite3.connect(db) as conn:
        inputGradeParameter = ' WHERE grade = ' + str(inputStartGrade)
        while inputStartGrade + 1 <= inputEndGrade:
            inputGradeParameter += ' OR grade = ' + str(inputStartGrade + 1)
            inputStartGrade += 1
        outputGradeParameter = ' WHERE grade = ' + str(outputStartGrade)
        while outputStartGrade + 1 <= outputEndGrade:
            outputGradeParameter += ' OR grade = ' + str(outputStartGrade + 1)
            outputStartGrade += 1
        c = conn.cursor()
        
        query = 'SELECT score FROM ' + inputSet[0] + inputGradeParameter
        for event in inputSet[1:]:
            query += ' UNION ALL ' + 'SELECT score FROM ' + event + inputGradeParameter
        query += ' ORDER BY score;'
        c.execute(query)
        ordered = c.fetchall()
        item = list(sorted(ordered, key = lambda x: abs(x[0] - score)))[0]
        
        query2 = 'SELECT score FROM ' + outputSet[0] + outputGradeParameter
        for event in outputSet[1:]:
            query2 += ' UNION ALL ' +  'SELECT score from ' + event + outputGradeParameter
        query2 += ' Order by score;'
        c.execute(query2)
        set2 = c.fetchall()
        return set2[int(ordered.index(item) / len(ordered) * len(set2))][0], ordered.index(item) / len(ordered)
