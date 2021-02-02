1 query
select stemtext, plaintext from wordform where stemtext = plaintext;

2 query
select stemtext from wordform where stemtext ILIKE 'a%';

3 query
select genretype, title from work where genretype = 'p';

4 query
select avg(totalparagraphs) from work where genretype like 't';

5 query
select totalwords, title from work where totalwords > (select avg(totalwords)from work);

6 query
select charname as "герои",
speechcount as "реплики",
workid as "произвидения"
from character_work ch
full outer join character c
on ch.charid=c.charid;

7 
select avg(speechcount) as "среднее кол.реп.герв" from character_work ch full outer join character c on ch.charid=c.charid where workid='romeojuliet';

8 
select section, sum(wordcount) from paragraph group by section order by section;

9
select charname, speechcount from character where speechcount > 15 and speechcount < 30;

10 
select title, year from work where year >= 1600;

11 
select longtitle from work where longtitle similar to '(%the %|%The%)';

12 
select section from paragraph union select section from paragraph ;

13 query
select chapterid, title, description
from work w
full outer join chapter c
on w.workid=c.workid;

14 
select paragraphnum, charname, speechcount
from character
full outer join paragraph p
on character.charid=p.charid;

15 
select paragraphnum, title, year
from work w
full outer join paragraph p
on w.workid=p.workid;
