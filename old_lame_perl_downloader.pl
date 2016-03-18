#!/usr/bin/perl
# no comment were present in the original script, so I'm adding them today, many years later.

# a nice onliner bash command is worth more than thousands words I guess...
# for i in `seq 1 1 1028` ; do wget -v -O $i.gif `curl -ks http://www.giantitp.com/comics/oots$i.html | grep 'comics/images/' | sed 's_.*src="\(.*\)".*_http://www.giantitp.com/\1_g'` ; done ;

# .. at least I used strict ..
use strict ;

# This data needs to be filled manually... YIKES! X(
my $begin=1 ; my $end=1028 ;

# the actual crawler ... seems I wasn't aware of the rule which says that:
# "everytime you parse HTMl with a regex somewhere an innocent kitten dies"

my $i = $begin ;
for ( ; $i < $end ; $i++) {
        my $actual_image = `curl -ks http://www.giantitp.com/comics/oots0$i.html | grep 'comics/images/' ` ;
        $actual_image =~ s/.*src="(.*)".*/$1/g ;
        # classy!
        my $cmd = `wget -v -O 000$i.gif http://www.giantitp.com/$actual_image` if ( $i < 10 and $9 >=1 ) ;
        my $cmd = `wget -v -O 00$i.gif http://www.giantitp.com/$actual_image` if ( $i < 100 and $i >= 10 );
        my $cmd = `wget -v -O 0$i.gif http://www.giantitp.com/$actual_image` if ( $i < 1000 and $i >= 100 );
        my $cmd = `wget -v -O $i.gif http://www.giantitp.com/$actual_image` if ( $i < 10000 and $i >= 1000 );
        exec ($cmd);
}

# no exit code either?!? oh gosh.
