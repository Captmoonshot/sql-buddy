from sql_buddy.concept import Concept


# Create an instances of Concept
def create_concepts():
	"""Create the entire collection of SQL concepts"""

	group_by = Concept(
		name='group_by',
		definition="""Divide the rows returned from the select statement into groups.  For each group, you 
		can apply an aggregate function like sum(), min(), max(), avg().""",
		syntax="""select col_1, col_2 from table_name group by col_1, col2""",
		example="""select staff_id, count(staff_id) from payment group by staff_id""",
		related_concepts=['group_by_with_having', 'where', 'having', 'order by', 'aggregation', 'sum', 'min', 'max', 'avg']
	)

	group_by_with_having = Concept(
		name='group_by_with_having',
		definition="""We use having in place of the where clause because aggregations like sum() do not work 
		with the where clause.""",
		syntax="""select col_1, col_2, sum(col) from table_name group by col_1, col_2 
		having sum(col) > 100""",
		example="""select c.first_name, c.last_name, sum(amount) as total_spent
		from customer c inner join payment p on p.customer_id = c.customer_id
		group by c.first_name, c.last_name having sum(amount) > 200""",
		related_concepts=["group_by", "where"]
	)

	concepts_list = [group_by, group_by_with_having]

	return concepts_list













