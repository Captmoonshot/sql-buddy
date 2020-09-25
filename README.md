# SQL-BUDDY

Sql-buddy is a study aid for SQL fundamentals that you can run on the terminal.  You can think of it as the command-line version of index cards you would normally use for studying a subject.

## Installation

You can install sql-buddy with pip:

    pip install sql-buddy

sql-buddy is supported by Python 3.7 and above.

## How to use

sql-buddy is a command line application.  There are two components:

1.  The first component emulates a simple collection of object that represent SQL concepts like GROUP BY:

```$ python -m sql_buddy```

Welcome to sql-buddy.  Populating In-memory Database...


Press Esc + ENTER to enter sql_buddy commands.
Press CTRL-D to quit

Type 'commands' and press Esc + ENTER to get a list of sql_buddy commands
>

As the instructions state you can type 'commands' and hit Esc + ENTER (RETURN):

> commands
    * list all: lists all the SQL concepts and queries
    * list some: list the first 10 concepts in the SQL concepts database
    * search=>{concept_name} gives you the definition, syntax, and usage of a specific SQL concept like group_by
        * i.e. search=>group_by
        * i.e. search=>order_by
        * i.e. search=>where
        * all SQL concept names must be in lowercase and have underscores in place of spaces


`> list all`


group_by: 

Divide the rows returned from the select statement into groups.  For each group, you 
        can apply an aggregate function like sum(), min(), max(), avg().


group_by_with_having: 

We use having in place of the where clause because aggregations like sum() do not work 
        with the where clause.


To search the definition, syntax, usage, and related concepts of a specific SQL concept:

`> search=>group_by`

group_by: 

Divide the rows returned from the select statement into groups.  For each group, you 
        can apply an aggregate function like sum(), min(), max(), avg().

syntax: 
select col_1, col_2 from table_name group by col_1, col2

usage: 
select staff_id, count(staff_id) from payment group by staff_id

related concepts: 
['group_by_with_having', 'where', 'having', 'order by', 'aggregation', 'sum', 'min', 'max', 'avg']


The syntax for any individual SQL concept is:

`> search=>{concept_name}`

Like Python variables concept names cannot have spaces and must be lowercase.

2. The second component is an SQL REPL straight from the `prompt-toolkit` documentation example tutorial:

[prompt-toolkit](https://python-prompt-toolkit.readthedocs.io/en/master/pages/tutorials/repl.html)

Run sql_buddy like before but with the -o flag:

`$ python -m sql_buddy -o`

And simply type SQLite queries:

```
select last_name, first_name, execution_date from deathrow limit 3;

('Brooks, Jr.', 'Charlie', '1982-12-07')

('Autry', 'James', '1984-03-14')

("O'Bryan", 'Ronald', '1984-03-31')
```

Sql-buddy comes with a csv data called tx_deathrow_full.csv that contains information about Texas deathrow inmates: [selectstarsql.com](https://selectstarsql.com/frontmatter.html).


The ideal setting for `sql-buddy` is two have two terminals open at the same time. One to utilize the first component to look up SQL concepts, and the other to run queries against an actual SQLite database table.

All data makes use of in-memory-only databases created through `sqlite3` and `sqlalchemy` methods.

For help:

`$ python -m sql_buddy -h`






