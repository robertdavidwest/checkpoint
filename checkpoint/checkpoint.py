import getpass
import shelve 
import time
import dateutil.parser
import os
import pandas as pd

# use default user directory
default_dir = "Q:/scraps/{}/checkpoints".format(getpass.getuser())

def save(variables, save_dir=None):
    """
    Parameters
    ----------
    variables: dict
        key, value listing of variables to be stored, for all variables pass locals()
    save_dir : str
        directory to store shelve. If not specified then the default will be 
        used
    """

    if not save_dir:
        save_dir = default_dir

    timestamp = time.asctime().replace(':', '-')
    filename = 'checkpoint_{}.sh'.format(timestamp)
    filepath = os.path.join(save_dir, filename)

    shelf = shelve.open(filepath, 'n')  # 'n' for new

    for key, value in variables.items():
        try:
            if '__' not in key:
                print "saving variable {}".format(key)
                shelf[key] = value
        except TypeError:
            #
            # __builtins__, my_shelf, and imported modules can not be shelved.
            #
            continue
            print 'Did not save: {0}'.format(key)
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
        load_dir = default_dir

    # get all shelf names
    shelfnames = [d for d in os.listdir(load_dir) if d[:11] == "checkpoint_"]
    if len(shelfnames) == 0:
        raise AssertionError("No checkpoint to load")

    timestamps = [d[11:] for d in shelfnames if d[:11]]

    # get valid datetimes
    datetimes = []
    for s in timestamps:
        print s.replace('-', ':')
        try:
            datetime = dateutil.parser.parse(s.replace('-', ':')[:-3])

            datetimes.append(datetime)
        except ValueError:
            print "Suffix {} is not a valid date time string input.".format(s)
            print "NaT passed instead (this has value -1)"
            datetimes.append(pd.NaT)

    # find newest file by time stamps
    idx = pd.Series(datetimes).idxmax()
    shelfname = shelfnames[idx]
    filepath = os.path.join(load_dir, shelfname)

    print "loading checkpoint {}".format(shelfname)
    shelf = shelve.open(filepath)
    print shelf.keys()
    loaded_variables = {}
    for key in shelf.keys():
        print "loading variable {}".format(key)
        loaded_variables[key] = shelf[key]
    shelf.close()

    return loaded_variables