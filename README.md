Filter_abcd is a Python program designed to work with the ABCD Study data. The ABCD Study is a prospective and longitidudinal study to track the brain, social, behavioral, and cognitive development of adolescents from 9-10 years of age for 10 years. Currently the study has enrolled close to 12,000 participants making it the largest longitudinal study of adolescent development in the United States and is supported by the National Institutes of Health.

This program filters the ABCD study .txt files by a pre-defined list of subjectkeys in the format of NDAR_INVxxxxxxxxx and was designed for analysis of unpublished data (Rodriguez, C., Vakamudi, K., Claus, E., Squeglia, L., Houck, J.). Please cite this program if you use it for your own research.

##Arguments

-p, --path Corresponds to the directory where your *.txt files are located.

-f, --files Corresponds to the files to be filtered.

-e, --event_names Corresponds to the timepoints at which data were collected. This argument can be set to null if the abcd*.txt file does not contain an eventname column (-e null).

-s, --subjectkeys Corresponds to a .csv file consisting of one column of subjectkeys/GUIDs in the format of NDAR_INVxxxxxxxxx

-o, --outpath Corresponds to the designated directory to write the output files. Files will be in .csv format and prefixed with "filtered."

##Usage

python filter_abcd_py -p /path/to/files/abcd_*.txt -f abcd_tlfb01.txt cct.txt -e baseline_year_1_arm_1 1_year_follow_up_y_arm_1 -s /path/to/subjectkeys.csv

Filters time line follow back and cash choice .txt files for baseline and year-1 follow up events for the subjects in subjectkeys.csv
