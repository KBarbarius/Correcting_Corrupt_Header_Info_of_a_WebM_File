# Correcting_Corrupt_Header_Info_of_a_WebM_File
The aim of this project was to repair over 500 WebM files which were not playing on any video player. I sucessully completed the project making sure that all videos were repaired and their quality maintained.

The first step I took was to try to repair the videos using 'Stellar Repair For Video', which is a subscription software used in repairing video. However, even after paying for subscription the software was unable to repair the videos fully. For a 20 seconds video it was only able to repair 5 seconds only.

After seeing unsatisactory results from the repairing softwares, I was prompt to use 'Hex Editor Heo' to see inside the files so that I can decide what is the next cause of action. While reviwing the files on the editor I noted that their WebM header Information was preceed by uncessary hexadecimal data. You can Indentify WebM file header info by the following structure "1A 45 DF A3"

With knowledge that header info should always be at the head of a file, I decide to mannualy copied the hexicadecimal data from where the header started to the end of the file into a new empty hex editor Neo file. And after saving it as WebM file it started playing.

After examining other files I saw the same structure whereby each file header info is preceded by irrevellant hexadecimal data. 

The final step was to create a script that with read the file and search where the header begins and copy the header and the data follows to the end. Ater the data was copied it was copied to a new file and saved a WebM file. To make sure the code know where the start copying rom I specified that the code will identify the header if it finds the following hexidecimal data following each other "1A 45". Please find the script on 'Correcting_Corrupt_webm_Files.py'

I have attached a sample of corrupt webm files and also those I repaired.
