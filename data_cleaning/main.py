from data_cleaning.filter_data import filter_data
from data_cleaning.data_manipulation import mk_move
from data_cleaning.to_hdf import to_hdf


def txt_to_h5(file_name):
    """
    takes the name of a .txt file with games from chess.com, and converts it
    to an hdf5 db.
    """
    print("txt to h5. Step 1/3. \n Please wait...")
    step1 = filter_data(file_name)  # .txt to json
    print("txt to h5... step 2/3. \n Please wait...")
    step2 = mk_move(step1)  # add additional data to json
    print("txt to h5... step 3/3. \n Please wait...")
    step3 = to_hdf(step2)  # convert to hdf

    return step3
