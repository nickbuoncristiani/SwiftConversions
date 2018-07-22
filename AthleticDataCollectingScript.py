import AthleticWebScraper, sqlite3, pickle, sys, requests, newScraper

"""Collects as many years of data as possible for a given event."""
def getAllData(a, event, filename):
    sys.setrecursionlimit(20000)
    for year in a.YEARS:
        print('working on ' + event + year)
        a.collectMany(event, year, 2000)
        with open(filename, 'wb') as file:
            backup = pickle.dump(a, file)
          
def go(a, filename):
    for event in a.EVENTS:
        getAllData(a, event, filename)

def addData(a, filename):
    print('adding to files')
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    try:
        for event in list(a.EVENTS.keys()):
            for year in list(a.YEARS.keys()):
                c.execute("CREATE TABLE '{}' (id text, state text, score float, grade text, date text)".format(event + year))    
                for id in a.Athletes:
                    athlete = a.Athletes[id]
                    mark = athlete.getMark(event, year)
                    if mark is None or len(mark.time) > 8:
                        continue
                    else:
                        time = mark.getSeconds()
                        state = athlete.state
                        date = mark.date
                        grade = mark.grade
                    c.execute("INSERT INTO '{}' VALUES ('{}', '{}', {}, '{}', '{}')".format(event + year, id, state, time, grade, date))
                conn.commit()
    finally:
        conn.close()