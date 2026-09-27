#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER: Vlad Lopatin
# DATE CREATED: 25.08.2026                                  
# REVISED DATE: 
import os

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
     results_dic - Dictionary with 'key' as image filename and 'value' as a
     List. The list contains for following item:
         index 0 = pet image label (string)
    """
    results_dic = {}

    filename_list = os.listdir(image_dir)

    for filename in filename_list:
        if filename.startswith("."):
            continue

        lower_name = filename.lower()
        word_list = lower_name.split("_")

        pet_label = ""
        for word in word_list:
            if word.isalpha():
                pet_label += word + " "

        pet_label = pet_label.strip()

        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print("Warning: Duplicate file exists", filename)

    return results_dic
