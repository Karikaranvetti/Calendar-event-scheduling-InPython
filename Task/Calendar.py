import os


def command_help():
    """
    () -> str
    This function is already implemented. Please do not change it.
    Returns a help message for the system. That is...
    """

    help_me = """
    Help for Calendar. The calendar commands are

    add DATE START END DETAILS               add the event DETAILS at the specified DATE with specific START and END time
    show                                     show all events in the calendar
    delete DATE NUMBER             delete the specified event (by NUMBER) from
                                   the calendar
    quit                           quit this program
    help                           display this help message

    Examples: user data follows command:

    command: add 2018-10-12 18 19 dinner with jane
    success

    command: show
        2018-10-12 : 
            start : 08:00, 
			end : 09:00,
			title : Eye doctor
			
            start : 12:30,
			end : 13:00,
			title : lunch with sid
            
			start : 18:00,
			end : 19:00, 
			title : dinner with jane
        2018-10-29 : 
            start : 10:00,
			end : 11:00,
			title : Change oil in blue car
			
            start : 12:00,
			end : 14:00,
			title : Fix tree near front walkway
			
            start : 18:00,
			end : 19:00,
			title : Get salad stuff, leuttice, red peppers, green peppers
        2018-11-06 : 
            start : 18:00,
			end : 22:00,
			title : Sid's birthday

    command: delete 2018-10-29 10
    deleted

    A DATE has the form YYYY-MM-DD, for example
    2018-12-21
    2016-01-02

    START and END has a format HH where HH is an hour in 24h format, for example
    09
    21

    Event DETAILS consist of alphabetic characters,
    no tabs or newlines allowed.
    """
    return help_me



def command_add(date, start_time, end_time, title, calendar):     #2
    """
    (str, int, int, str, dict) -> boolean
    Add title to the list at calendar[date]
    Create date if it was not there
    Adds the date if start_time is less or equal to the end_time

    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer from 0-23 representing the start time
    end_time: An integer from 0-23 representing the start time
    title: A string describing the event
    calendar: The calendar database
    return: boolean of whether the even was successfully added

    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 10, 9, "go out with friends after test", calendar)
    False
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], \
    "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    """

    # YOUR CODE GOES HERE
    if (isinstance(calendar, dict)):
         
        if not  is_calendar_date(date):
            return False
        if not (start_time<=end_time and start_time>=0 and start_time<24 and end_time >=0 and end_time<24):
            return False

        val={"start": start_time, "end": end_time, "title": title}
        if date in calendar:
            
            calendar[date].append(val)

        else:
            calendar[date] = [val] 
        calendar[date].sort(key=lambda event: event['start'])
        return True 
    else:
        return False


def prepend(digit):
    if digit<10:
        n='0'+str(digit)+':00'
    elif digit>9:
        n=str(digit)+':00'


    return(n)

def makeTwodes(digit):
    if digit<10:
        n='0'+str(digit)
    elif digit>9:
        n=str(digit)
    return n




def command_show(calendar):             #3

    r"""
    (dict) -> str
    Returns the list of events for calendar sorted in decreasing date order
    and increasing time order within the date
    as a string, see examples below for a sample formatting
    calendar: the database of events

    Example:
    >>> calendar = {}
    >>> command_add("2018-01-15", 11, 13, "Eye doctor", calendar)
    True
    >>> command_add("2018-01-15", 8, 9, "lunch with sid", calendar)
    True
    >>> command_add("2018-02-10", 12, 23, "Change oil in blue car", calendar)
    True
    >>> command_add("2018-02-10", 20, 22, "dinner with Jane", calendar)
    True
    >>> command_add("2017-12-22", 5, 8, "Fix tree near front walkway", calendar)
    True
    >>> command_add("2017-12-22", 13, 15, "Get salad stuff", calendar)
    True
    >>> command_add("2018-05-06", 19, 23, "Sid's birthday", calendar)
    True
    >>> command_show(calendar)
    "\n2018-05-06 : \n    start : 19:00,\n    end : 23:00,\n    title : Sid's birthday\n2018-02-10 : \n    start : 12:00,\n    end : 23:00,\n    title : Change oil in blue car\n\n    start : 20:00,\n    end : 22:00,\n    title : dinner with Jane\n2018-01-15 : \n    start : 08:00,\n    end : 09:00,\n    title : lunch with sid\n\n    start : 11:00,\n    end : 13:00,\n    title : Eye doctor\n2017-12-22 : \n    start : 05:00,\n    end : 08:00,\n    title : Fix tree near front walkway\n\n    start : 13:00,\n    end : 15:00,\n    title : Get salad stuff"
    """


    dates = list(calendar.keys())
    # print(dates)
    dates.sort(reverse=True)
    # print(dates)
    text=''
    for date in dates:
        # print(date)
        text1='\n'+str(date)+' : '
        calendar[date].sort(key=lambda event: event['start'])
        # print(calendar[date])
        Ttext=''
        for i in range(len(calendar[date])):
            # print('\tstart',': {}'.format(prepend(calendar[date][i]['start'])))
            text2='\n    start : '+str(prepend(calendar[date][i]['start']))+','
            # print('\tend',': {}'.format(prepend(calendar[date][i]['end'])))
            text3='\n    end : '+str(prepend(calendar[date][i]['end']))+','
            if i==(len(calendar[date])-1):
                # print('\ttitle',':',calendar[date][i]['title'])
                text4='\n    title : '+str(calendar[date][i]['title'])
            else:
                # print('\ttitle',':',calendar[date][i]['title'],'\n')
                text4='\n    title : '+str(calendar[date][i]['title'])+'\n'
            Ttext=Ttext+text2+text3+text4
        text=text+text1+Ttext
    return text
        

def command_delete(date, start_time, calendar):   #4
    """
    (str, int, dict) -> str
    Delete the entry at calendar[date][start_time]
    If calendar[date] is empty, remove this date from the calendar.
    If the entry does not exist, do nothing
    date: A string date formatted as "YYYY-MM-DD"
    start_time: An integer indicating the start of the event in calendar[date] to delete
    calendar: The calendar database
    return: a string indicating any errors, True for no errors

    Example:


    >>> calendar = {}
    >>> command_add("2018-02-28", 11, 12, "Python class", calendar)
    True
    >>> calendar == {"2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-11", 14, 16, "CSCA08 test 2", calendar)
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> calendar == {"2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], \
    "2018-02-28": [{"start": 11, "end": 12, "title": "Python class"}]}
    True
    >>> command_add("2018-03-13", 13, 13, "Have fun", calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": \
    [{"start": 14, "end": 16, "title": "CSCA08 test 2"}], "2018-02-28": [{"start": 11, "end": 12, \
    "title": "Python class"}]}
    True
    >>> command_delete("2015-01-01", 1, calendar)
    '2015-01-01 is not a date in the calendar'
    >>> command_delete("2018-03-11", 3, calendar)
    'There is no event with start time of 3 on date 2018-03-11 in the calendar'
    >>> command_delete("2018-02-28", 11, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}], "2018-03-11": [{"start": 14, "end": 16, "title": "CSCA08 test 2"}]}
    True
    >>> command_delete("2018-03-11", 14, calendar)
    True
    >>> calendar == {"2018-03-13": [{"start": 13, "end": 13, "title": "Have fun"}]}
    True
    >>> command_delete("2018-03-13", 13, calendar)
    True
    >>> calendar == {}
    True

    """

    # YOUR CODE GOES HERE



    if date in calendar:
        flag=0
        for event in calendar[date]:
            if event['start']==start_time:
                flag=1
                calendar[date].remove(event)
        if flag==0:
            # print('There is no event with start time of {} on date {} in the calendar'.format(start_time,date))
            err='There is no event with start time of {} on date {} in the calendar'.format(start_time,date)
            return err
        if len(calendar[date])==0:
            del calendar[date]
    else:
        # print('{} is not a date in the calendar'.format(date))    
        err='{} is not a date in the calendar'.format(date)
        return err

    return True


def save_calendar(calendar):    #5
    """
    (dict) -> bool
    Save calendar to 'calendar.txt', overwriting it if it already exists. The calendar events do not have
    to be saved in any particular order

    The format of calendar.txt is the following:

    date_1:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n
    date_2:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n
    date_n:start_time_1-end_time_1 description_1\tstart_time_2-end_time_2 description_2\t...\tstart_time_n-end_time_n description_n\n

    Example: The following calendar...



        2018-03-13 : 
                start : 13:00,
                end : 13:00,
                title : Have fun
        2018-03-11 : 
                start : 10:00,
                end : 12:00,
                title : Another event on this date

                start : 14:00,
                end : 16:00,
                title : CSCA08 test 2
        2018-02-28 : 
                start : 8:00,
                end : 9:00,
                title : Linux class

                start : 11:00,
                end : 12:00,
                title : Python class

     appears in calendar.txt as ...

    2018-03-13:13-13 Have fun
    2018-03-11:10-12 Another event on this date    14-16 CSCA08 test 2
    2018-02-28:08-09 Linux class    11-12 Python class

    calendar: dictionary containing a calendar
    return: True if the calendar was saved.
    """
    # YOUR CODE GOES HERE

    
    dates = list(calendar.keys()) 
    lines=list()

    for date in dates :

        Tdate=str(date)+':'
        Tevent=''

        for i in range(len(calendar[date])):
            if i==len(calendar[date])-1:
                Tevent=Tevent+makeTwodes(calendar[date][i]['start'])+'-'+makeTwodes(calendar[date][i]['end'])+' '+str(calendar[date][i]['title'])+'\n'
            else:
                Tevent=Tevent+makeTwodes(calendar[date][i]['start'])+'-'+makeTwodes(calendar[date][i]['end'])+' '+str(calendar[date][i]['title'])+'\t'

        T=Tdate+Tevent
        lines.append(T)
    f = open("calendar.txt", "w")
    for line in lines:
        f.write(line)

    return True



def load_calendar():      #6
    '''
    () -> dict
    Load calendar from 'calendar.txt'. If calendar.txt does not exist,
    create and return an empty calendar. For the format of calendar.txt
    see save_calendar() above.

    return: calendar.

    '''

    # YOUR CODE GOES HERE


    calendar={}
    with open("calendar.txt") as f:
        for line in f:
            arr=line.split(':')
            date=arr[0]

            arr2=arr[1].split('\t')
            for i in range(len(arr2)):
                # print(event[0])

                arr3=arr2[i].split(' ',1)
                title=arr3[1].replace("\n", "")
                arr4=arr3[0].split('-')
                start_time=int(arr4[0])
                end_time=int(arr4[1])
                sdict={'start':start_time,'end':end_time,'title':title}

                if date in calendar:
                    calendar[date].append(sdict)
                else:
                    calendar[date] = [sdict]
    return calendar
        

def is_command(command):       #7
    '''
    (str) -> bool
    Return whether command is a valid command
    Valid commands are any of the options below
    "add", "delete", "quit", "help", "show"
    You are not allowed to use regular expressions in your implementation.
    command: string
    return: True if command is one of ["add", "delete", "quit", "help", "show"]
    false otherwise
    Example:
    >>> is_command("add")
    True
    >>> is_command(" add ")
    False
    >>> is_command("List")
    False

    '''

    # YOUR CODE GOES HERE

    data=["add", "delete", "quit", "help", "show"]  
    if command in data:
        return True
    else:
        return False   



def is_number(letter):
    if ord(letter)>47 and ord(letter)<58:
        return True
    return False

def is_calendar_date(date):      #8

    '''
    (str) -> bool
    Return whether date looks like a calendar date
    date: a string
    return: True, if date has the form "YYYY-MM-DD" and False otherwise
    You are not allowed to use regular expressions in your implementation.
    Also you are not allowed to use isdigit() or the datetime module functions.

    Example:

    >>> is_calendar_date("15-10-10") # invalid year
    False
    >>> is_calendar_date("2015-10-15")
    True
    >>> is_calendar_date("2015-5-10") # invalid month
    False
    >>> is_calendar_date("2015-15-10") # invalid month
    False
    >>> is_calendar_date("2015-05-10")
    True
    >>> is_calendar_date("2015-10-55") # invalid day
    False
    >>> is_calendar_date("2015-55") # invalid format
    False
    >>> is_calendar_date("jane-is-gg") # YYYY, MM, DD should all be digits
    False

    Note: This does not validate days of the month, or leap year dates.

    >>> is_calendar_date("2015-04-31") # True even though April has only 30 days.
    True

    '''
    # Algorithm: Check length, then pull pieces apart and check them. Use only
    # basic string
    # manipulation, comparisons, and type conversion. Please do not use any
    # powerful date functions
    # you may find in python libraries.
    # 2015-10-12
    # 0123456789

    # YOUR CODE GOES HERE




    Y,M,D=date.split('-')
    # print(Y[2],M,D) 
    # print(len(Y))
    if  ((len(Y)==4)and len(M)==2) and (len(D)==2):
        for i in range(len(Y)):
            if not is_number(Y[i]):
                return False
        for j in range(2):
            if not is_number(M[j]):
                return False
        for k in range(2):
            if not is_number(D[k]):
                return False
        if int(M)<13 and int(M)>0 and int(D)<32 and int(D)>0:
            return True
                
    
    return False  


def is_natural_number(Nnum):     #9
    '''
    (str) -> bool
    Return whether str is a string representation of a natural number,
    that is, 0,1,2,3,...,23,24,...1023, 1024, ...
    In CS, 0 is a natural number
    param str: string
    Do not use string functions
    return: True if num is a string consisting of only digits. False otherwise.
    Example:

    >>> is_natural_number("0")
    True
    >>> is_natural_number("05")
    True
    >>> is_natural_number("2015")
    True
    >>> is_natural_number("9 3")
    False
    >>> is_natural_number("sid")
    False
    >>> is_natural_number("2,192,134")
    False

    '''
    # Algorithm:
    # Check that the string has length > 0
    # Check that all characters are in ["0123456789"]

    # YOUR CODE GOES HERE



    for i in range(len(Nnum)):
        if not is_number(Nnum[i]):
            return False
    return True

def parse_command(line):       #10
    '''
    (str) -> list
    Parse command and arguments from the line. Return a list
    [command, arg1, arg2, ...]
    Return ["error", ERROR_DETAILS] if the command is not valid.
    Return ["help"] otherwise.
    The valid commands are

    1) add DATE START_TIME END_TIME DETAILS
    2) show
    3) delete DATE START_TIME
    4) quit
    5) help

    line: a string command
    return: A list consiting of [command, arg1, arg2, ...].
    Return ["error", ERROR_DETAILS], if line can not be parsed.
    ERROR_DETAILS displays how to use the

    Example:
    >>> parse_command("add 2015-10-21 10 11 budget meeting")
    ['add', '2015-10-21', 10, 11, 'budget meeting']
    >>> parse_command("")
    ['help']
    >>> parse_command("not a command")
    ['help']
    >>> parse_command("help")
    ['help']
    >>> parse_command("add")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22")
    ['error', 'add DATE START_TIME END_TIME DETAILS']
    >>> parse_command("add 2015-10-22 7 7 Tims with Sally.")
    ['add', '2015-10-22', 7, 7, 'Tims with Sally.']
    >>> parse_command("add 2015-10-35 7 7 Tims with Sally.")
    ['error', 'not a valid calendar date']
    >>> parse_command("show")
    ['show']
    >>> parse_command("show calendar")
    ['error', 'show']
    >>> parse_command("delete")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("delete 15-10-22 11")
    ['error', 'not a valid calendar date']
    >>> parse_command("delete 2015-10-22 3,14")
    ['error', 'not a valid event start time']
    >>> parse_command("delete 2015-10-22 14")
    ['delete', '2015-10-22', 14]
    >>> parse_command("delete 2015-10-22 14 hello")
    ['error', 'delete DATE START_TIME']
    >>> parse_command("quit")
    ['quit']

    '''
    # HINT: You can first split, then join back the parts of
    # the final argument.
    # YOUR CODE GOES HERE

    args=line.split(' ',4)

    
    if args[0]== 'add':
        if len(args)!=5:
            # print("['error', 'add DATE START_TIME END_TIME DETAILS']")
            err=['error', 'add DATE START_TIME END_TIME DETAILS']
            return err
        elif not is_calendar_date(args[1]):
            # print("['error', 'not a valid calendar date']")
            err=['error', 'not a valid calendar date']
            return err

        args[2]=int(args[2])
        args[3]=int(args[3])
        return args
         

    elif args[0]=='show':
        if len(args)==1:
            return args
        else:
            # print("['error', 'show']")
            err=['error', 'show']
        return err
            
    elif args[0]=='delete':
        if len(args)!=3:
            # print("['error', 'delete DATE START_TIME']")
            err=['error', 'delete DATE START_TIME']
            return err
        elif not is_calendar_date(args[1]):
            # print("['error', 'not a valid calendar date']")
            err=['error', 'not a valid calendar date']
            return err
        elif not (is_natural_number(args[2]) and int(args[2])>=0 and int(args[2])<24):
            # print("['error', 'not a valid event start time']")
            err=['error', 'not a valid event start time']
            return err
        args[2]=int(args[2])
        return args
    elif args[0]=='quit':
        return args
    else:
        return ['help']
    

def user_interface():     #11  

    calendar=load_calendar()
    print('calendar loaded')
    # print(calendar) 

    while True:
        userdata = input("command:")
        fun=userdata.split(' ',4)

        if fun[0]=='add':
            command_add(fun[1], int(fun[2]), int(fun[3]),fun[4], calendar)
            # print(calendar)
            print('added')
        elif fun[0]=='show':
            command_show(calendar)
        elif fun[0]=='delete':
            if command_delete(fun[1],int(fun[2]), calendar):
                print('deleted')
        elif fun[0]=='quit':
            save_calendar(calendar)
            print('calendar saved')
            exit()



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    user_interface()
