#!/usr/bin/python

#for i in ${*}
#do
#  type=`exifprobe ${i} | grep "^File" | grep Type`
#  suffix=""
#
#  if [[ "${type}" =~ "UNKNOWN" ]] ; then continue
#  elif [[ "${type}" =~ "TIFF" ]] ; then suffix=".nef"
#  elif [[ "${type}" =~ "JPEG" ]] ; then suffix=".jpg"
#  else continue ; fi
#
#  date=`exifprobe -L ${i} | exifgrep -export DateTimeDigitized |\
#        cut -d "=" -f2 | tr -d "'" | tr -d ":" | tr -s " " "-"`
#  o=${date}${suffix}
#  if [ -e ${o:0:8}/${o} ] ; then o=${o/${suffix}/a${suffix}} ; fi
#  if [ -e ${o:0:8}/${o} ] ; then o=${o/a${suffix}/b${suffix}} ; fi
#  if [ -e ${o:0:8}/${o} ] ; then o=${o/b${suffix}/c${suffix}} ; fi
#
#  chmod 644 ${i}
#  mv -i -v ${i} ${o}
#  mkdir -v ${o:0:8}
#  mv -i -v ${o} ${o:0:8}
#done

#jhead -autorot *.jpg
#jhead -nf%Y%m%d-%H%M%S *.jpg
#nice -n5 ufraw-batch --out-type=jpeg --overwrite */*.nef