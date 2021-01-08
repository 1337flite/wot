#!/bin/sh

DATADIR="/Users/jtan/Documents/WoT/data/clans"
TIMESTAMP=`date +%Y%m%d-%H%M%S`
PATH="${PATH}:/Users/jtan/repos/wot"


#${DATADIR}/fiddy/
#${DATADIR}/lemon/
#${DATADIR}/sabre1/
#${DATADIR}/sabre2/
#${DATADIR}/sabre3/
#${DATADIR}/valor/
#${DATADIR}/1ar/


get_sabre1_member_battls_counts >> ${DATADIR}/sabre1/${TIMESTAMP}-sabre1.csv
get_sabre2_member_battls_counts >> ${DATADIR}/sabre2/${TIMESTAMP}-sabre2.csv
get_sabre3_member_battls_counts >> ${DATADIR}/sabre3/${TIMESTAMP}-sabre3.csv
get_lemon_member_battls_counts  >>  ${DATADIR}/lemon/${TIMESTAMP}-lemon.csv
get_valor_member_battls_counts >> ${DATADIR}/valor/${TIMESTAMP}-valor.csv
get_1ar_member_battls_counts >> ${DATADIR}/1ar/${TIMESTAMP}-1ar.csv
get_fiddy_member_battls_counts >> ${DATADIR}/fiddy/${TIMESTAMP}-fiddy.csv
