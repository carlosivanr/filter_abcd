#!/usr/bin/env python3

"""
Author : Carlos Rodriguez <crodriguez@mrn.org>
Date   : 11/02/2021
Purpose: Filters ABCD study .txt files to match a pre-existing list of subjectkeys (GUIDs).
Formats: Requires a list of subjectkeys in a .csv file with a header. Subjectkeys need to be written as NDAR_INVxxxxxxxxx.
Usage: python filter_abcd_py -p /path/to/.txt/files -f abcd_tlfb01.txt cct.txt -e baseline_year_1_arm_1 1_year_follow_up_y_arm_1 -s subjectkeys.csv
"""

import argparse
import pandas as pd
import os

# --------------------------------------------------
parser = argparse.ArgumentParser(
        description = "Filter ABCD study .txt files to match a pre-existing list of subjectkeys.",
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

parser.add_argument(
    "-p",
    "--path",
    metavar = "",
    help = "Filepath where abcd .txt files are located.",
    type = str,
    required = True)

parser.add_argument(
    "-f",
    "--files",
    metavar = "",
    help = "Files to filter",
    type = str,
    nargs = "+",
    required = True)

parser.add_argument(
    "-e",
    "--event_names",
    metavar = "",
    help = "Event names to filter, defaults to baseline_year_1_arm_1.",
    nargs = "+",
    type = str,
    default = "baseline_year_1_arm_1")

parser.add_argument(
    "-s",
    "--subjectkeys",
    help = "",
    metavar = "",
    type = str,
    required = True)

parser.add_argument(
    "-o",
    "--outpath",
    metavar = "",
    help = "Filepath to output filtered files, defaults to the current working directory.",
    type = str,
    default = os.getcwd())

args = parser.parse_args()
print(args)

if args.event_names[0] == "null":
    print("Event_names set to null, will not filter by event_names.")
else:
    print("Filtering " + args.event_names)


# --------------------------------------------------
subjects = pd.read_csv(args.subjectkeys)
subjects = list(subjects.iloc[:,0])

for i in range(len(args.files)):
    file_name = args.files[i]
    abcd = pd.read_csv(args.path + '/' + file_name, sep = '\t', low_memory = False)
    sub_index = abcd.subjectkey.isin(subjects)
    sub_index[0] = True
    filtered_subjects = abcd[sub_index]

    if args.event_names[0] != "null": 
        if "eventname" in abcd.columns:
            event_index = filtered_subjects.eventname.isin(args.event_names)
            event_index[0] = True
            filtered_subjects = filtered_subjects[event_index]
        
        
        if "visit" in abcd.columns:
            event_index = filtered_subjects.visit.isin(args.event_names)
            event_index[0] = True
            filtered_subjects = filtered_subjects[event_index]

    out_path = args.outpath + '/filtered_' + file_name[0:-3] + 'csv'
    filtered_subjects.to_csv(out_path, index = False)
