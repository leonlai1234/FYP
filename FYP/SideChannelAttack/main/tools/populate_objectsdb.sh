#!/bin/bash

#Remove the old database if it exists
rm objectsdb.sqlite3 || echo "Object DB never existed"

#Initialize the database
python main/tools/initialize_db.py objectsdb.sqlite3

for x in $testfilename_list
do
	echo "This is from Test file: $x"
done

for y in $trainfilename_list
do
	echo "This is from Train file: $y"
done

echo "This is the ip address entered: $ipadd"
echo "This is the total uploaded set: $totalupload"

#Populate the database with each entries
for f in $(find TrainData/ -type f -name "*train_pcap_uploadfile0.*")
do
	python main/tools/process_google_trace.py $f objectsdb.sqlite3 Uploadfile0 TRAIN
done

for f in $(find TrainData/ -type f -name "*train_pcap_uploadfile1.*")
do
	python main/tools/process_google_trace.py $f objectsdb.sqlite3 Uploadfile1 TRAIN
done

for f in $(find TrainData/ -type f -name "*train_pcap_uploadfile2.*")
do
	python main/tools/process_google_trace.py $f objectsdb.sqlite3 Uploadfile2 TRAIN
done

for f in $(find TrainData/ -type f -name "*train_pcap_uploadfile3.*")
do
	python main/tools/process_google_trace.py $f objectsdb.sqlite3 Uploadfile3 TRAIN
done

for f in $(find TrainData/ -type f -name "*train_pcap_uploadfile4.*")
do
	python main/tools/process_google_trace.py $f objectsdb.sqlite3 Uploadfile4 TRAIN
done

for f in $(find TrainData/ -type f -name "*train_pcap_uploadfile5.*")
do
	python main/tools/process_google_trace.py $f objectsdb.sqlite3 Uploadfile5 TRAIN
done

for f in $(find TrainData/ -type f -name "*train_pcap_uploadfile6.*")
do
	python main/tools/process_google_trace.py $f objectsdb.sqlite3 Uploadfile6 TRAIN
done

for f in $(find TrainData/ -type f -name "*train_pcap_uploadfile7.*")
do
	python main/tools/process_google_trace.py $f objectsdb.sqlite3 Uploadfile7 TRAIN
done

for f in $(find TrainData/ -type f -name "*train_pcap_uploadfile8.*")
do
	python main/tools/process_google_trace.py $f objectsdb.sqlite3 Uploadfile8 TRAIN
done

for f in $(find TrainData/ -type f -name "*train_pcap_uploadfile9.*")
do
	python main/tools/process_google_trace.py $f objectsdb.sqlite3 Uploadfile9 TRAIN
done