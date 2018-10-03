import Athlete, re, Mark, time
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.error import URLError as urlerror

"""Uses BeautifulSoup to scrape data from Athletic.net""" 
class AthleticWebScraper: 
    
    def __init__(self, college):
        self.EVENTS = {'100mMen' : '1', '200mMen' : '2', '400mMen' : '3', '800mMen' : '4', '1600mMen' : '52', '3200mMen' : '60', '100mWomen' : '19', '200mWomen' : '20', '400mWomen' : '21', '800mWomen' : '22', '1600mWomen' : '53', '3200mWomen' : '61'}
        self.MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.YEARS = {'2014' : '49804', '2015' : '59920', '2016' : '70949', '2017' : '80153', '2018' : '89402'}
        self.Athletes = {}
        if college:
            del self.EVENTS['1600mMen']
            del self.EVENTS['3200mMen']
            del self.EVENTS['1600mWomen']
            del self.EVENTS['3200mWomen']
            self.EVENTS['1500mMen'] = '5'
            self.EVENTS['1500mWomen'] = '23'
            self.EVENTS['5000mMen'] = '79'
            self.EVENTS['5000mWomen'] = '80'
            self.YEARS = {'2014' : '49375', '2015' : '59489', '2016' : '70513', '2017' : '79715', '2018' : '88964'}
         
    """Adds a bunch of data to our athletes dictionary. Pages indexed at 0."""
    def collectMany(self, event, year, num_pages):
        if not(self.checkInput(event, year)):
            return
        allAthletes = []
        page = 0
        yearID = self.YEARS[year]
        EventID = self.EVENTS[event]
        baseURL = 'https://www.athletic.net/TrackAndField/Division/Event.aspx?DivID=' + yearID + "&Event=" + EventID + '&page='
        while page <= num_pages:
            print('On page ' + str(page))
            try:
                allAthletes.extend(self.collectPage(baseURL + str(page), event, year))
            except IndexError:
                print('We probably made it to the end: ' + str(page))
                break
            except urlerror:
                time.sleep(10)
                allAthletes.extend(self.collectPage(baseURL + str(page), event, year))
            except Exception:
                print('unsure, getting out')
                return
            page += 1
            time.sleep(.05)
        for athlete in allAthletes:
            self.addAthlete(athlete)
   
    """Takes a page and scrapes 100 athletes, return athletes in a list."""
    def collectPage(self, url, event, year):
        athletesOnPage = []
               
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
            
        page_soup = soup(page_html, 'html.parser')
        
        table = page_soup.findAll('table', {"class" : "HLData DataTable table table-hover table-striped signed-out-blur"})
        athletes = table[0].findAll('tr')
        for athlete in athletes[1 : len(athletes) - 1]:
            athletesOnPage.append(self.makeAthlete(event, year, athlete))
        return athletesOnPage
        
    def checkInput(self, event, year):
        if event not in self.EVENTS:
            print('Event not supported. Supported events are: ')
            print(self.EVENTS)
            return False
        if year not in self.YEARS:
            print('Year out of range.')
            return False
        return True
        
    """Creates a new athlete object based on web data. Adds a mark."""
    def makeAthlete(self, event, year, athleteHTML):
        data = athleteHTML.findAll('td')
        
        """Collects necessary data from HTML"""
        id = re.sub('[^0123456789]', '', data[2].a['href'])
        grade = data[1].text
        time = re.sub('[^0123456789:.(]', '', data[4].a.text)
        if '(' in time:
            time = time[0:time.find('(')]
        tds = athleteHTML.findAll('td', {'class':'text-muted'})
        state = data[5].text
        date = tds[1].text
        
        mark = Mark.Mark(event, time, grade, year, date)
        
        athlete = Athlete.Athlete(id, state) 
        athlete.addMark(mark)
        return athlete
            
    """Adds a new athlete or updates an existing one"""
    def addAthlete(self, athlete):
        if athlete.id in self.Athletes:
            self.Athletes[athlete.id].merge(athlete)
        else:
            self.Athletes[athlete.id] = athlete
        