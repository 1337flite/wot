#!/usr/bin/perl
# Author: chook_on_a_stick asia server
# Initial commit 28 Nov 2020 but the scipt has been used on and off for at least 12 months.
#
# A simple perl script to take lines of data from the WoT clan personel page e.g.
# https://asia.wargaming.net/clans/wot/2000010912/players/#players&offset=0&limit=25&order=-role&timeframe=all&battle_type=default
# and format it into CSV that can be easily imported/pasted into a spreadsheet
# Needs Perl 5 (other versions may work)
# Has been tested on OSX from the terminal CLI, but should work under Linux or even windows with Cygwin 
# Or the fancy new make windows actually usable linux compatability layer (who cares what it is called?)
#
# Usage go to the clan personal page, choose the filter e.g. last 28 days, battles overall, Advances, CW batles etc
# Copy the text from the table on the report page into a file in the example below the file is called
# "sabre_last28days_cw_tables_20201128.txt "
# Then run the command
# cat sabre_last28days_cw_tables_20201128.txt | ./lines2csv.plx 
# Cut and paste the output into a speadsheet.
# You should get a column with one cell per player containing the csv record
# Use the Data->Split text to Columns (Google Sheets) or the Data->Text to Columns (Excel) function
# To break the cell's data into individual columns.
#
# As commited assumes 10 input fields/output colums, but you can change the number i
# of input fields/output columns be setting $cols to some other value.

$cols = 10;
$count = 0;
$dlvl=1;

while ( <> ){
	# If there is a blank line skip it and jump to the next iteration.
	if(/^$/){
		next;
	}
	chomp;
	$count++;
	s/,//g;		# remove commas, so we don't extraneous get commas in the CSV output
#	print ;
	$field = $_;
	
	if( 0 == $count % $cols ){
		print $field . "\n";
	}else{
		print $field . "," ;	
	}
}




sub debug($dlevel,$dstring){
	if ( $dlevel >= $dlvl){
		print $dstring ;
	}
}
