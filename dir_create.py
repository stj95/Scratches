import argparse
import os


def make_folders(home_path, new_folders):

    for folder in new_folders:
        try:
            for suffix in ["z2", "n2", "e2"]:
                os.mkdir(home_path + "\\" + folder + suffix)

        except FileExistsError:
            continue

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('-d', '--directory', help='The directory you want to create folders in')
    parser.add_argument('-l', '--folder_list', action='append')

    args = parser.parse_args()
    print(args)
    make_folders(args.directory, args.folder_list)


