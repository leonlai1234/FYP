# #!/bin/bash

# #Train Uploadfile0 classifier
# python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile0 classifier__uploadfile0.json


# #Train Uploadfile1 classifier
# python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile1 classifier__uploadfile1.json

# #Train Uploadfile2 classifier
# python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile2 classifier__uploadfile2.json


# #Train Uploadfile3 classifier
# python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile3 classifier__uploadfile3.json


# #Train Uploadfile4 classifier
# python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile4 classifier__uploadfile4.json


# #Train Uploadfile5 classifier
# python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile5 classifier__uploadfile5.json


# #Train Uploadfile6 classifier
# python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile6 classifier__uploadfile6.json

# #Create the nearest neighbor classifier
# python main/tools/make_nearest_neighbour_classifier.py

#Train Uploadfile0 classifier
if [[ $(find TrainData/ -type f -name "*train_pcap_uploadfile0.*") ]]; then
    python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile0 classifier__uploadfile0.json
fi

#Train Uploadfile1 classifier
if [[ $(find TrainData/ -type f -name "*train_pcap_uploadfile1.*") ]]; then
    python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile1 classifier__uploadfile1.json
fi

#Train Uploadfile2 classifier
if [[ $(find TrainData/ -type f -name "*train_pcap_uploadfile2.*") ]]; then
    python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile2 classifier__uploadfile2.json
fi

#Train Uploadfile3 classifier
if [[ $(find TrainData/ -type f -name "*train_pcap_uploadfile3.*") ]]; then
    python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile3 classifier__uploadfile3.json
fi

#Train Uploadfile4 classifier
if [[ $(find TrainData/ -type f -name "*train_pcap_uploadfile4.*") ]]; then
    python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile4 classifier__uploadfile4.json
fi

#Train Uploadfile5 classifier
if [[ $(find TrainData/ -type f -name "*train_pcap_uploadfile5.*") ]]; then
    python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile5 classifier__uploadfile5.json
fi

#Train Uploadfile6 classifier
if [[ $(find TrainData/ -type f -name "*train_pcap_uploadfile6.*") ]]; then
    python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile6 classifier__uploadfile6.json
fi

if [[ $(find TrainData/ -type f -name "*train_pcap_uploadfile7.*") ]]; then
    python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile7 classifier__uploadfile7.json
fi

if [[ $(find TrainData/ -type f -name "*train_pcap_uploadfile8.*") ]]; then
    python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile8 classifier__uploadfile8.json
fi

if [[ $(find TrainData/ -type f -name "*train_pcap_uploadfile9.*") ]]; then
    python main/tools/determine_unique_features.py objectsdb.sqlite3 Uploadfile9 classifier__uploadfile9.json
fi

#Create the nearest neighbor classifier
python main/tools/make_nearest_neighbour_classifier.py
