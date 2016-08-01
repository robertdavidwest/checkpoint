import getpass
import shelve 
import time
import dateutil.parser

default_dir = lambda user: "Q:/scraps/{}/checkpoints".format(user)

def save(save_dir=None):
    """
    Parameters
    ----------
    save_dir : str
        directory to store shelve. If not specified then the default will be 
        used
    """
    if not save_dir:
        # use default user directory 
        user = getpass.getuser()
        save_dir = default_dir(user)
        
    timestamp = time.asctime()
    filename = 'checkpoint_{}.sh'.format(timestamp)
    filepath = '{}/{}'.format(
    shelf = shelve.open(filepath,'n') # 'n' for new

    for key in dir():
        try:
            my_shelf[key] = globals()[key]
        except TypeError:
            #
            # __builtins__, my_shelf, and imported modules can not be shelved.
            #
            print('ERROR shelving: {0}'.format(key))
    shelf.close()


def load(load_dir=None):
    """
    Parameters
    ----------
    load_dir : str
        directory to store shelve. If not specified then the default will be 
        used
    """

    if not load_dir:
        # use default user directory 
        user = getpass.getuser()
        load_dir = default_dir(user)

    # get all shelf names
    shelfnames = [d for d in os.listdir(load_dir) if d[:11] == "checkpoint_"]
    timestamps = [d[11:] for d in shelfnames if d[:11]]

    # get valid datetimes
    datetimes = []
    for s in timestamps:
        try:
            datetime = dateutil.parser.parse(s)
            datetimes.append(datetime)
        except ValueError:
            print "Suffix {} is not a valid date time string input.".format(s)
            print "NaT passed instead (this has value -1)"
            datetimes.append(pd.NaT)
        
    # find newest file by time stamps
    idx = pd.Series(datetimes).idxmax
    shelfname = shelfnames[idx]

    my_shelf = shelve.open(shelfname)
    for key in my_shelf:
        globals()[key]=my_shelf[key]
    my_shelf.close()