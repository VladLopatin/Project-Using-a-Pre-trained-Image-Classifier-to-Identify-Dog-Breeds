# PROGRAMMER: Vlad Lopatin
# DATE CREATED: 25.08.2026                                  
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pet in the image, and
#          summarizes how well the CNN performed on the image classification task.

# Imports classifier function for using CNN to classify images
from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to
    the classifier labels, and adds the classifier label and the comparison of
    the labels to the results dictionary using the extend function.
    Parameters:
     images_dir - The (full) path to the folder of images that are to be
                  classified by the classifier function (string)
     results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following item
                    at index 0 : pet image label (string)
     model - CNN model architecture to be used for classifying images (string)
    Returns:
           None - results_dic is mutated by this function, results for the
           classifier function are added to results_dic as follows:
             index 1 = classifier label (string)
             index 2 = 1/0 (int) where 1 = match and 0 = no match
    """
    for filename in results_dic:
        path = images_dir + filename

        classifier_label = classifier(path, model)
        classifier_label = classifier_label.lower().strip()
        pet_label = results_dic[filename][0]

        if pet_label in classifier_label:
            match = 1
        else:
            match = 0

        results_dic[filename].append(classifier_label)
        results_dic[filename].append(match)
